import json
import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.0-flash")

def extract_toyota_filters(user_request):

    prompt = f"""
    You help extract structured search filters from a user's natural language request
    so we can filter a Toyota car dataset.

    The dataset has the following columns:
    - Model
    - Year
    - Engine Fuel Type
    - Engine HP
    - Engine Cylinders
    - Transmission Type
    - Driven_Wheels
    - Number of Doors
    - Market Category
    - Vehicle Size
    - Vehicle Style
    - highway MPG
    - city mpg
    - Popularity
    - MSRP

    User request:
    "{user_request}"

    Return a SINGLE JSON object with any of these keys when they are clearly implied:

    - model: string (partial model name, e.g. "Corolla", "RAV4")
    - minYear: integer
    - maxYear: integer

    - bodyType: string mapped from "Vehicle Style", e.g.
      "Sedan", "SUV", "Truck", "Coupe", "Hatchback", "Minivan"

    - fuel: simplified engine fuel type, one of:
      "gas", "hybrid", "electric", "diesel", "any"
      (These map to the dataset column "Engine Fuel Type", which contains values like
       "regular unleaded", "premium unleaded (recommended)", "regular unleaded (hybrid)", etc.)

    - transmission: one of ["Automatic", "Manual"] mapped from "Transmission Type"
    - drive: one of ["FWD", "RWD", "AWD", "4WD"] mapped from "Driven_Wheels"
    - minDoors: integer (from "Number of Doors")

    - minMSRP: integer (USD, from "MSRP")
    - maxMSRP: integer (USD, from "MSRP")

    - minCityMPG: integer (from "city mpg")
    - maxCityMPG: integer (from "city mpg")
    - minHighwayMPG: integer (from "highway MPG")
    - maxHighwayMPG: integer (from "highway MPG")

    ### Interpreting vague language

    If the user is vague, infer sensible numeric ranges instead of words:

    Price words:
    - "cheap", "budget", "affordable", "entry level" → set maxMSRP around 25000–30000
    - "mid range", "decent price", "not too expensive" → set maxMSRP around 30000–40000
    - "premium", "luxury", "high end" → set minMSRP around 40000

    Mileage words (apply to both city and highway, unless user is specific):
    - "excellent mileage", "super fuel efficient" → minCityMPG 40, maxCityMPG 60; minHighwayMPG 40, maxHighwayMPG 60
    - "good mileage", "fuel efficient", "decent mileage" → minCityMPG 30, maxCityMPG 40; minHighwayMPG 30, maxHighwayMPG 40
    - "okay mileage", "average mileage" → minCityMPG 20, maxCityMPG 30; minHighwayMPG 20, maxHighwayMPG 30
    - "I don't care about mileage", "mileage doesn't matter" → omit MPG fields

    If the user gives explicit numbers, use them:
    - "under $35k" → maxMSRP: 35000
    - "between 20 and 30 mpg" → minCityMPG: 20, maxCityMPG: 30, and same for highway MPG unless otherwise specified
    - "at least 30 mpg" → minCityMPG: 30 and minHighwayMPG: 30

    Body type hints (map to Vehicle Style / bodyType):
    - "SUV", "crossover" → bodyType: "SUV"
    - "sedan", "saloon" → bodyType: "Sedan"
    - "truck", "pickup" → bodyType: "Truck"
    - "small car", "compact car", "city car" → bodyType: "Hatchback" or "Sedan" (prefer "Hatchback" if unsure)
    - "coupe", "2-door sports car" → bodyType: "Coupe"

    Fuel hints (map to Engine Fuel Type):
    - "hybrid", "plug-in hybrid" → fuel: "hybrid"
    - "electric", "EV" → fuel: "electric"
    - "gas", "petrol", "regular" → fuel: "gas"
    - If fuel is not mentioned → omit fuel

    Family / capacity hints (mapped via doors / size):
    - "for my family", "family car", "kids", "stroller", "road trips" → set minDoors to at least 4
    - "7 seater", "three rows", "third row" → bodyType likely "SUV" or "Minivan" and minDoors at least 4
    - "just me", "for commuting", "small car" → you may leave doors unspecified if unclear

    Performance hints (optional, use HP if needed):
    - "sporty", "performance", "powerful", "fast" → you may set a minHP around 200 and return a field "minHP"
    - "I don't care about power" → omit HP filtering

    ### Important rules:
    - ONLY include fields that are clearly implied by the user request.
    - If a field is not mentioned or strongly implied, LEAVE IT OUT of the JSON.
    - Use integers for all numeric values.
    - Do NOT invent random constraints.
    - Output MUST be valid JSON with double quotes, no comments, and no markdown or code fences.

    Now output just the JSON object for the user request above.
    """



    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )

    #Testing
    print(response.text)

    try:
        filters = json.loads(response.text)
        return (filters)
    except json.JSONDecodeError:
        return ({})
