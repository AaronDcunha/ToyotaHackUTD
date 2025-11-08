import pandas as pd
import os

df = pd.read_csv("backend\ToyotaCarDataset.csv")

def filter_cars(filters):
    df_filtered = df.copy()

    if "bodyType" in filters:
        df_filtered = df_filtered[
            df_filtered["Vehicle Style"]
            .str.lower()
            .str.contains(filters["bodyType"].lower(), na=False)
        ]

    if "fuel" in filters:
        df_filtered = df_filtered[
            df.filtered["Engine Fuel Type"].str.lower().str.contains(filters["fuel"].lower(),na=False)]
        
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
