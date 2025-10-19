import pandas as pd

try:
    df = pd.read_csv("Nosample.csv")
    print(df.head())
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print("Error:", {e})
