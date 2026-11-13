import requests

url = "http://localhost:9696/predict"

patient = {
    "age": 48,
    "blood_pressure": 80,
    "urine_specific_gravity": 1.020,
    "urine_albumin_level": 1,
    "urine_sugar_level": 0,
    "random_blood_glucose": 121,
    "blood_urea": 36,
    "serum_creatinine": 1.2,
    "sodium": 137,
    "potassium": 4.5,
    "hemoglobin": 15.4,
    "packed_cell_volume": 44,
    "white_blood_cell_count": 7800,
    "red_blood_cell_count": 5.2,
    "red_blood_cell_status": "normal",
    "pus_cell_status": "normal",
    "pus_cell_clumps": "notpresent",
    "bacteria": "notpresent",
    "hypertension": "yes",
    "diabetes_mellitus": "yes",
    "coronary_artery_disease": "no",
    "appetite": "good",
    "pedal_edema": "no",
    "anemia": "no"
}

response = requests.post(url, json=patient)
response.raise_for_status()

print(response.json())