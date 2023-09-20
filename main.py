from lib import pd_desc, pd_visual
import pandas as pd

def summary_desc():
    df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    # return [mean(df), median(df), std(df)]
    return pd_desc(df)

def visual():
    df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    pd_visual(df["Model Year"])