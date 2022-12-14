from fastapi.testclient import TestClient
from main import app

# Unit test
client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue dans l'API de prédiction de la résistance à la compression du béton"}

def test_post_sample():
    response = client.post("/predict", json={"echantillon": "string","elem_ch_1": 0,"elem_ch_2": 0,"elem_ch_3": 0,
                                             "elem_ch_4": 0,"elem_ch_5": 0,"elem_ch_6": 0,
                                             "elem_ch_7": 0,"elem_ch_8": 0,"elem_ch_9": 0,
                                             "elem_ch_10": 0,"elem_ch_11": 0,"elem_ch_12": 0,
                                             "elem_ch_13": 0,"elem_ch_14": 0,"elem_ch_15": 0,
                                             "elem_ch_16": 0,"elem_ch_17": 0,"elem_ch_18": 0,
                                             "elem_ch_19": 0,"elem_ch_20": 0,"elem_ch_21": 0,
                                             "elem_ch_22": 0,"elem_ch_23": 0,"elem_ch_24": 0,
                                             "elem_ch_25": 0,"elem_ch_26": 0,"elem_ch_27": 0,
                                             "elem_ch_28": 0,"elem_ch_29": 0,"elem_ch_30": 0,
                                             "elem_ch_31": 0,"elem_ch_32": 0,"elem_ch_33": 0,
                                             "elem_ch_34": 0,"elem_ch_35": 0,"elem_ch_36": 0,
                                             "elem_ch_37": 0,"elem_ch_38": 0,"elem_ch_39": 0,
                                             "elem_ch_40": 0,"rc28j_moy": 0,"d_0_1": 0,"d_0_2": 0,
                                             "d_0_5": 0,"d_0_8": 0,"d_0_9": 0,"d_3_2": 0,"d_4_3": 0,
                                             "param_rr_1": 0,"param_rr_2": 0,"param_rr_3": 0})
    assert response.status_code == 200

def test_post_sample_with_missing_columns():
    response = client.post("/predict", json={"echantillon": "string","elem_ch_1": 0,"elem_ch_2": 0,"elem_ch_3": 0,
                                            "elem_ch_4": 0,"elem_ch_5": 0,"elem_ch_6": 0,
                                            "elem_ch_7": 0,"elem_ch_8": 0,"elem_ch_9": 0,
                                            "elem_ch_13": 0,"elem_ch_14": 0,"elem_ch_15": 0,
                                            "elem_ch_16": 0,"elem_ch_17": 0,"elem_ch_18": 0,
                                            "elem_ch_19": 0,"elem_ch_20": 0,"elem_ch_21": 0,
                                            "elem_ch_22": 0,"elem_ch_23": 0,"elem_ch_24": 0,
                                            "elem_ch_25": 0,"elem_ch_26": 0,"elem_ch_27": 0,
                                            "elem_ch_28": 0,"elem_ch_29": 0,"elem_ch_30": 0,
                                            "elem_ch_31": 0,"elem_ch_32": 0,"elem_ch_33": 0,
                                            "elem_ch_34": 0,"elem_ch_35": 0,"elem_ch_36": 0,
                                            "elem_ch_37": 0,"elem_ch_38": 0,"elem_ch_39": 0,
                                            "elem_ch_40": 0,"rc28j_moy": 0,"d_0_1": 0,"d_0_2": 0,
                                            "d_0_5": 0,"d_0_8": 0,"d_0_9": 0,"d_3_2": 0,"d_4_3": 0,
                                            "param_rr_1": 0,"param_rr_2": 0,"param_rr_3": 0})
    assert response.status_code != 200