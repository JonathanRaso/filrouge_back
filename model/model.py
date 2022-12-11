import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime

# get base path
BASE_DIR = Path(__file__).resolve(strict=True).parent

# load model
with open(f"{BASE_DIR}/sgd_model.sav", "rb") as f:
    model = joblib.load(f)

def predict_pipeline(sample):
    # get sample values inside df (interim df, not the shape we want)
    interim_df = pd.DataFrame(sample)

    # get columns and values
    columns = interim_df[0].values
    values = interim_df[1].values

    # create df with the right shape
    data = pd.DataFrame(data=[values], columns=columns)

    # columns to use
    colunms_kept = ['elem_ch_1', 'elem_ch_2', 'elem_ch_5', 'elem_ch_6',
                    'elem_ch_8','elem_ch_9', 'elem_ch_16', 'elem_ch_17',
                    'elem_ch_21', 'elem_ch_25','elem_ch_26', 'elem_ch_27',
                    'elem_ch_28', 'elem_ch_29', 'elem_ch_30','elem_ch_31',
                    'elem_ch_32', 'elem_ch_36', 'elem_ch_38', 'd_0_1',
                    'd_0_2', 'd_0_5', 'd_0_8', 'd_3_2', 'param_rr_3']

    # keep the columns we need to get prediction
    X = data[colunms_kept]

    # predict concrete compressive strength
    y_pred = model.predict(X)

    # return prediction
    return (y_pred[0])


def prepare_sample(sample, predicted_rc):
    # get sample values inside df (interim df, not the shape we want)
    interim_df = pd.DataFrame(sample)
    # get columns and values
    columns = interim_df[0].values
    values = interim_df[1].values
    # create df with the right shape
    data = pd.DataFrame(data=[values], columns=columns)
    data["prediction_rc28j"] = predicted_rc
    data["prediction_date"] = datetime.now()
    return data

