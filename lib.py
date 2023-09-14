import pandas as pd
import polars as pl
import matplotlib.pyplot as plt

# For Pandas
# describe
def pd_desc(df):
    return df.describe()

# visualization: bar plot
def pd_visual(df): 
    df.plot(kind="hist")
    plt.xticks(rotation = 90)
    plt.ylabel('Frequency')
    plt.xlabel(df.name)
    plt.show()
    
# For Polars
# describe
def polars_desc(df):
    return df.describe()

# visualization: histgram
def polars_visual(df):
    plt.hist(df["Model Year"])



