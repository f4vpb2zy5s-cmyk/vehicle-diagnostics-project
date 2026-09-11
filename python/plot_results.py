import pandas as pd
import matplotlib.pyplot as plt

# Messdaten laden
data = pd.read_csv("data/vehicle_data.csv")

# Grenzwerte
MIN_LAMBDA = 0.95
MAX_LAMBDA = 1.05

# Diagramm erstellen
plt.figure(figsize=(12, 6))

# Lambda-Wert über der Zeit
plt.plot(
    data["time_s"],
    data["lambda"],
    label="Lambda signal"
)

# Grenzwerte
plt.axhline(
    MAX_LAMBDA,
    linestyle="--",
    label="Upper limit"
)

plt.axhline(
    MIN_LAMBDA,
    linestyle="--",
    label="Lower limit"
)

# Zeitpunkt der DTC-Bestätigung
plt.axvline(
    154,
    linestyle="--",
    label="DTC confirmed"
)

# Beschriftungen
plt.xlabel("Time [s]")
plt.ylabel("Lambda value")
plt.title("Lambda Signal - Vehicle Diagnostics")

plt.legend()
plt.grid()

# Diagramm speichern
plt.savefig(
    "results/lambda_diagnostics.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()