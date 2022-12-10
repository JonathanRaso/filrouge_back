from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline, prepare_sample
from database.connection import db_connection, insert_sample

class Payload(BaseModel):
    echantillon: str
    elem_ch_1: float
    elem_ch_2: float
    elem_ch_3: float
    elem_ch_4: float
    elem_ch_5: float
    elem_ch_6: float
    elem_ch_7: float
    elem_ch_8: float
    elem_ch_9: float
    elem_ch_10: float
    elem_ch_11: float
    elem_ch_12: float
    elem_ch_13: float
    elem_ch_14: float
    elem_ch_15: float
    elem_ch_16: float
    elem_ch_17: float
    elem_ch_18: float
    elem_ch_19: float
    elem_ch_20: float
    elem_ch_21: float
    elem_ch_22: float
    elem_ch_23: float
    elem_ch_24: float
    elem_ch_25: float
    elem_ch_26: float
    elem_ch_27: float
    elem_ch_28: float
    elem_ch_29: float
    elem_ch_30: float
    elem_ch_31: float
    elem_ch_32: float
    elem_ch_33: float
    elem_ch_34: float
    elem_ch_35: float
    elem_ch_36: float
    elem_ch_37: float
    elem_ch_38: float
    elem_ch_39: float
    elem_ch_40: float
    rc28j_moy: float
    d_0_1: float
    d_0_2: float
    d_0_5: float
    d_0_8: float
    d_0_9: float
    d_3_2: float
    d_4_3: float
    param_rr_1: float
    param_rr_2: float
    param_rr_3: float

# Instantiate FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenue dans l'API de prédiction de la résistance à la compression du béton"}

@app.post("/predict")
def predictions(payload: Payload):
    predicted_rc = predict_pipeline(payload)
    data = prepare_sample(payload, predicted_rc)
    conn = db_connection()
    insert_sample(data, conn)
    return predicted_rc

