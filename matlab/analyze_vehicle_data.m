% Vehicle Diagnostics Project
% MATLAB analysis of simulated vehicle data

clear;
clc;
close all;

%% Daten laden

data = readtable("data/vehicle_data.csv");

%% Erste Daten anzeigen

disp("First rows of vehicle data:");
disp(head(data));

%% Grundlegende Statistik

mean_rpm = mean(data.rpm);
max_rpm = max(data.rpm);

mean_speed = mean(data.speed_kmh);
max_speed = max(data.speed_kmh);

mean_coolant = mean(data.coolant_temp_C);
max_coolant = max(data.coolant_temp_C);

fprintf("Mean RPM: %.1f rpm\n", mean_rpm);
fprintf("Maximum RPM: %.1f rpm\n", max_rpm);

fprintf("Mean speed: %.1f km/h\n", mean_speed);
fprintf("Maximum speed: %.1f km/h\n", max_speed);

fprintf("Mean coolant temperature: %.1f °C\n", mean_coolant);
fprintf("Maximum coolant temperature: %.1f °C\n", max_coolant);

%% Lambda-Grenzwerte

lambda_min = 0.95;
lambda_max = 1.05;

lambda_fault = ...
    data.lambda < lambda_min | ...
    data.lambda > lambda_max;

%% Anzahl fehlerhafter Messwerte

fault_count = sum(lambda_fault);

fprintf("\nLambda values outside threshold: %d\n", fault_count);

%% Ersten auffälligen Messwert finden

first_fault_index = find(lambda_fault, 1);

if ~isempty(first_fault_index)

    fprintf("First abnormal lambda value at: %.0f s\n", ...
        data.time_s(first_fault_index));

    fprintf("Lambda value: %.3f\n", ...
        data.lambda(first_fault_index));

else

    fprintf("No abnormal lambda values detected.\n");

end

%% Lambda Signal plotten

figure;

plot(data.time_s, data.lambda);
hold on;

yline(lambda_max, "--");
yline(lambda_min, "--");

xlabel("Time [s]");
ylabel("Lambda");
title("Lambda Signal Analysis");

grid on;
legend("Lambda", "Upper Threshold", "Lower Threshold");

%% Ergebnis speichern

exportgraphics( ...
    gcf, ...
    "results/matlab_lambda_analysis.png", ...
    "Resolution", 300 ...
);