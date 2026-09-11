import pandas as pd

# Messdaten laden
data = pd.read_csv("data/vehicle_data.csv")

# Diagnoseparameter
MIN_LAMBDA = 0.95
MAX_LAMBDA = 1.05
MAX_COOLANT_TEMP = 105

FAULT_CONFIRMATION_TIME = 5

diagnostic_results = []

# --------------------------------------------------
# Lambda-Diagnose
# --------------------------------------------------

lambda_counter = 0
lambda_fault_detected = False

for _, row in data.iterrows():

    lambda_fault = (
        row["lambda"] < MIN_LAMBDA or
        row["lambda"] > MAX_LAMBDA
    )

    if lambda_fault:
        lambda_counter += 1
    else:
        lambda_counter = 0

    if lambda_counter >= FAULT_CONFIRMATION_TIME:

        diagnostic_results.append({
            "fault_code": "SIM_LAMBDA_HIGH",
            "description": "Lambda signal outside diagnostic threshold",
            "time_s": row["time_s"],
            "rpm": row["rpm"],
            "speed_kmh": row["speed_kmh"],
            "coolant_temp_C": row["coolant_temp_C"],
            "throttle_percent": row["throttle_percent"],
            "lambda": row["lambda"]
        })

        lambda_fault_detected = True
        break


# --------------------------------------------------
# Kühlmitteltemperatur-Diagnose
# --------------------------------------------------

coolant_fault = data[
    data["coolant_temp_C"] > MAX_COOLANT_TEMP
]

if len(coolant_fault) > 0:

    row = coolant_fault.iloc[0]

    diagnostic_results.append({
        "fault_code": "SIM_COOLANT_HIGH",
        "description": "Coolant temperature too high",
        "time_s": row["time_s"],
        "rpm": row["rpm"],
        "speed_kmh": row["speed_kmh"],
        "coolant_temp_C": row["coolant_temp_C"],
        "throttle_percent": row["throttle_percent"],
        "lambda": row["lambda"]
    })


# --------------------------------------------------
# Diagnosebericht erstellen
# --------------------------------------------------

if len(diagnostic_results) > 0:

    report = pd.DataFrame(diagnostic_results)

    report.to_csv(
        "results/diagnostic_report.csv",
        index=False
    )

    print("Diagnostic report generated.\n")
    print(report)

else:

    print("No faults detected.")