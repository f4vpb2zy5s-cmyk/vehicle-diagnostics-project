import pandas as pd

# Messdaten einlesen
data = pd.read_csv("data/vehicle_data.csv")

# Grenzwerte für einfache Diagnose
MAX_COOLANT_TEMP = 105
MIN_LAMBDA = 0.95
MAX_LAMBDA = 1.05

print("Starting vehicle diagnostics...\n")

# Kühlmitteltemperatur prüfen
hot_engine = data[data["coolant_temp_C"] > MAX_COOLANT_TEMP]

if len(hot_engine) > 0:
    print("WARNING: Coolant temperature too high!")
    print(hot_engine[["time_s", "coolant_temp_C"]])
else:
    print("Coolant temperature: OK")

# Lambda-Wert prüfen
lambda_fault = data[
    (data["lambda"] < MIN_LAMBDA) |
    (data["lambda"] > MAX_LAMBDA)
]

if len(lambda_fault) > 0:
    print("\nWARNING: Lambda value outside allowed range!")
    print(lambda_fault[["time_s", "lambda"]])
else:
    print("Lambda value: OK")

print("\nDiagnostics completed.")