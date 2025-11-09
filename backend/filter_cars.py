import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "ToyotaCarDataset.csv")
df = pd.read_csv(csv_path)

def filter_cars(filters):
    df_filtered = df.copy()

    if "bodyType" in filters:
        df_filtered = df_filtered[
            df_filtered["Vehicle Style"]
            .str.lower()
            .str.contains(filters["bodyType"].lower(), na=False)
        ]

    if "fuel" in filters:
        if filters["fuel"].lower() == "gas":
            pass
        elif filters["fuel"] == "electric":
            df_filtered = df_filtered[df_filtered["Engine Fuel Type"].str.lower().str.contains(filters["fuel"].lower(),na=False)]
        elif filters["fuel"] == "hybrid":
            df_filtered = df_filtered[df_filtered["Market Category"].str.lower().str.contains(filters["fuel"].lower(),na=False)]
        
        
    if "transmission" in filters:
        df_filtered = df_filtered[
            df_filtered["Transmission Type"]
            .str.lower()
            .str.contains(filters["transmission"].lower(), na=False)
        ]
    
    if "minMSRP" in filters:
        df_filtered = df_filtered[df_filtered["MSRP"] >= filters["minMSRP"]]
    if "maxMSRP" in filters:
        df_filtered = df_filtered[df_filtered["MSRP"] <= filters["maxMSRP"]]

    if "minMPG" in filters:
        df_filtered = df_filtered[df_filtered["city mpg"] >= filters["minMPG"]]
    if "maxMPG" in filters:
        df_filtered = df_filtered[df_filtered["city mpg"] <= filters["maxMPG"]]

    return df_filtered

#print(filter_cars({"bodyType":"SUV","maxMSRP":30000})[:5])
