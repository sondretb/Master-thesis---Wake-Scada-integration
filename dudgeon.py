import os
from azure.storage.blob import BlobServiceClient, BlobClient
from dotenv import load_dotenv
import pandas as pd
from download_files import DATA_DIR
load_dotenv()

coords_path = os.path.join(DATA_DIR, 'Dudgeon_coordinates.csv')
dataframe = pd.read_csv(coords_path, sep=";")

def get_name_spesific(raw_name):
    return raw_name.split('-')[-1]

degree_to_meter_factor = 111100

NAMES = dataframe['Asset'].apply(get_name_spesific).to_numpy()
WT_X = dataframe['Longitude'].to_numpy()*degree_to_meter_factor # estimate
WT_Y = dataframe['Latitude'].to_numpy() *degree_to_meter_factor  # estimate






