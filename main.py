#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#%%
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./secrets/my_credentials.json"
def get_weather_dataset(year):
    """This function runs a query on Google BigQuery from the noaa_gsod datasets and returns a dataframe based on the year.

    Args:
        year (int): the year in which we want to obtain the weather data

    Returns:
        pandas.DataFrame: the data that pertains to a particular year
    """
    sql_query = f""" SELECT * FROM `bigquery-public-data.noaa_gsod.gsod{year}` """
    df = pd.read_gbq(sql_query)
    return df

#%%
weather_data = {year: get_weather_dataset(year) for year in range(1990, 2024)}