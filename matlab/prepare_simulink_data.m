clear;
clc;

data = readtable("data/vehicle_data.csv");

lambda_signal = timeseries( ...
    data.lambda, ...
    data.time_s ...
);

disp("Lambda signal prepared for Simulink.");