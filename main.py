#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#%%
my_credentials = "./secrets/my_credentials.json"
def get_weather_dataset(year):
    """This function runs a query on Google BigQuery from the noaa_gsod gsod dataset and returns a dataframe based on the year.

    Args:
        year (int): the year in which we want to obtain the weather data

    Returns:
        pandas.DataFrame: the data that pertains to a particular year
    """
    weather_query = f""" SELECT * FROM `bigquery-public-data.noaa_gsod.gsod{year}` """
    weather_df = pd.read_gbq(weather_query, credentials = my_credentials)
    return weather_df
def get_station_data(state):
    """This function runs a query on Google BigQuery from the noaa_gsod station dataset and returns a dataframe based on the state.

    Args:
        state (string): filters the station dataset based on state

    Returns:
        pandas.DataFrame: the data that pertains to a particular state
    """
    state_query = """SELECT * FROM `bigquery-public-data.noaa_gsod.stations` WHERE state = :state"""
    station_data = pd.read_gbq(state_query, credentials = my_credentials)
    return station_data
#%%
weather_data = {year: get_weather_dataset(year) for year in range(1990, 2024)}