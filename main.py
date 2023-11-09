#%%
from pathlib import Path
import pandas as pd
import numpy as np
import tqdm
import matplotlib.pyplot as plt
import os
#%%
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path.cwd() / "secrets" / "my_credentials.json")
def get_weather_dataset(year, state):
    """This function runs a query on Google BigQuery from the noaa_gsod gsod dataset and returns a dataframe based on the year. The data is filtered by year and by state.

    Args:
        year (int): the year in which we want to obtain the weather data

    Returns:
        pandas.DataFrame: the data that pertains to a particular year and state
    """
    weather_query = f"""
SELECT * EXCEPT (wban, stn, usaf, country, state, call) FROM `bigquery-public-data.noaa_gsod.gsod{year}` AS gsod{year} 
INNER JOIN `bigquery-public-data.noaa_gsod.stations` AS stations ON gsod{year}.wban = stations.wban WHERE state = {state}
"""
    weather_df = pd.read_gbq(weather_query, progress_bar_type = "tqdm")
    return weather_df
#%%
# Gather the datasets for the weather of each year from 1990 to 2023
weather_data = {year: get_weather_dataset(year, "IL") for year in range(1990, 2024)}
weather_combined = 