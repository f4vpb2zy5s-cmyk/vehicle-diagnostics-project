import pandas as pd

data = pd.read_csv("data/vehicle_data.csv")

MIN_LAMBDA = 0.95
MAX_LAMBDA = 1.05
FAULT_CONFIRMATION_TIME = 5

counter = 0
fault_detected = False

for index, row in data.iterrows():

    lambda_fault = (
        row["lambda"] < MIN_LAMBDA or
        row["lambda"] > MAX_LAMBDA
    )

    if lambda_fault:
        counter += 1
    else:
        counter = 0

    if counter >= FAULT_CONFIRMATION_TIME:
        fault_detected = True

        print("DTC detected!")
        print("Code: SIM_LAMBDA_HIGH")
        print("Description: Lambda signal above diagnostic threshold")
        print()
        print("Freeze Frame:")
        print(f"Time: {row['time_s']:.0f} s")
        print(f"RPM: {row['rpm']:.0f} rpm")
        print(f"Speed: {row['speed_kmh']:.1f} km/h")
        print(f"Coolant temperature: {row['coolant_temp_C']:.1f} °C")
        print(f"Throttle: {row['throttle_percent']:.1f} %")
        print(f"Lambda: {row['lambda']:.3f}")

        break

if not fault_detected:
    print("No confirmed fault detected.")