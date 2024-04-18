import os
from azure.storage.blob import BlobServiceClient, BlobClient
from dotenv import load_dotenv
import pandas as pd
load_dotenv()


"""
conn_str = os.environ.get("CONNECTION_STRING")
coordinates_sas = os.environ.get('COORDINATES_SAS')


storage_service = BlobServiceClient.from_connection_string(conn_str=conn_str)
blob_client = storage_service.get_blob_client(container='preliminarydata', blob='ntnu24data/Dudgeon_coordinates.csv')
"""

coordinates_sas = os.environ.get('COORDINATES_SAS')
print(coordinates_sas)
dataframe = pd.read_csv(coordinates_sas, sep=";")

degree_to_meter_factor = 111100
WT_X = dataframe['Longitude'].to_numpy()*degree_to_meter_factor # estimate
WT_Y = dataframe['Latitude'].to_numpy() *degree_to_meter_factor  # estimate

