#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%

def get_weather_dataset(year):
    sql_query = f""" SELECT * FROM `bigquery-public-data.noaa_gsod.gsod{year}` """
    df = pd.read_gbq(sql_query, project_id = "xxxx")
    return df

#%%
df = []
for year in range(2019, 2023):
    df.append(get_weather_dataset(year))