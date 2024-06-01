from wake_estimator import WakeEstimatorTI
from data_filter import get_filtered_data
from py_wake.superposition_models import LinearSum
from util import timestamp_to_datetime_index
from dudgeon import WT_X, WT_Y, NAMES
from tqdm import tqdm
import pandas as pd

ws_params_filename = './temp/estimate_entry_params.csv'
wse_filename = './data/windspeed_estimates.csv'


def _save_to_file():
    data = get_filtered_data(turbine_set=['A05'], include_ti=False)['A05']
    data.to_csv(ws_params_filename)

def _read_file():
    data = pd.read_csv(ws_params_filename)
    return timestamp_to_datetime_index(data)

def _get_column_list():
    return [f'DOW-{name}-WSE' for name in NAMES]


def create_estimated_ws_set(ws, wd, ts):
    wse_list = []
    wake_estimator = WakeEstimatorTI(superpositionModel=LinearSum)
    for ws_i, wd_i in tqdm(zip(ws,wd), total=len(ws), desc="Generating WS estimates"):
        wse_i_results = wake_estimator.predict(X=[ws_i, wd_i])
        wse_list.append(wse_i_results)

    ti_df = pd.DataFrame(data=wse_list, columns=_get_column_list(), index=ts)
    ti_df.index.name = 'timestamp'
    ti_df.to_csv(wse_filename)

if __name__ == '__main__':
    #_save_to_file()
    param_df = _read_file()
    ws = param_df['WindSpeed'].to_numpy()
    wd = param_df['WindDirection'].to_numpy()
    ts = param_df.index.to_numpy()
    create_estimated_ws_set(ws, wd, ts)

