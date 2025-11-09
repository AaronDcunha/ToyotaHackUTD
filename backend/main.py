from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Any

from ai_query import extract_toyota_filters
from filter_cars import filter_cars
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ManualFilters(BaseModel):
    bodyType: Optional[str] = None
    fuel: Optional[str] = None
    transmission: Optional[str] = None
    minMSRP: Optional[int] = None
    maxMSRP: Optional[int] = None
    minMPG: Optional[int] = None
    maxMPG: Optional[int] = None
    year: Optional[int] = None

class AIQuery(BaseModel):
    query: str

def df_to_list(df):
    return df.to_dict(orient="records")

@app.get("/")
def root():
    return {"message": "Backend runs!"}

@app.post("/result/ai")
def result_ai(payload: AIQuery):

    user_query = payload.query

    ai_filters = extract_toyota_filters(user_query)
    print(ai_filters)
    df_filtered = filter_cars(ai_filters)
    df_filtered = df_filtered[:20]
    df_clean = df_filtered.replace({np.nan: None})

    return df_clean.to_dict(orient="records")

    #print(df_filtered[:10])
    #return cars

@app.post("/result/manual")
def result_manual(filters: ManualFilters):
    print(filters)
    filters_dict = {k: v for k, v in filters.dict().items() if v is not None}
    print(filters_dict)
    print("Manual filters:", filters_dict)

    df_filtered = filter_cars(filters_dict)
    df_filtered = df_filtered[:20]
    #cars = df_filtered.to_dict(orient="records")
    print(df_filtered)
    df_clean = df_filtered.replace({np.nan: None})

    return df_clean.to_dict(orient="records")

    #return cars