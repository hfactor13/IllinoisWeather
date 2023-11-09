#%%
from pathlib import Path
import pandas as pd
import numpy as np
import tqdm
import matplotlib.pyplot as plt
import os
#%%
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path.cwd() / "secrets" / "my_credentials.json")
def get_weather_dataset(start_year, end_year, state):
    """This function runs a query on Google BigQuery from the noaa_gsod gsod dataset and returns a dataframe between a start_year and an end_year. The data is filtered by state.

    Args:
        year (int): the year in which we want to obtain the weather data

    Returns:
        pandas.DataFrame: the data that pertains to a year range and state
    """
    weather_query = f"""
    SELECT gsod_combined.* EXCEPT (wban, stn, usaf, country, state, call) 
    FROM `bigquery-public-data.noaa_gsod.gsod*` as gsod_combined
    JOIN `bigquery-public-data.noaa_gsod.stations` AS stations ON gsod_combined.wban = stations.wban 
    WHERE stations.state = '{state}' AND gsod_combined.year BETWEEN {start_year} AND {end_year};
    """
    weather_df = pd.read_gbq(weather_query, progress_bar_type = "tqdm")
    return weather_df
#%%
# Gather the datasets for the weather of each year from 1990 to 2023
combined_weather_data = get_weather_dataset(1990, 2023, "IL")
combined_weather_data.replace({999.9: np.nan}, inplace = True)
combined_weather_data.replace({9999.9: np.nan}, inplace = True)