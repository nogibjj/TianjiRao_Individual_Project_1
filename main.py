from lib import pd_desc
import pandas as pd

def summary_desc():
    df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    # return [mean(df), median(df), std(df)]
    return pd_desc(df)