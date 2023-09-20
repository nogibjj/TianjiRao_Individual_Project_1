# import pandas as pd
# import polars as pl
import matplotlib.pyplot as plt

# For Pandas
# describe
def pd_desc(df):
    return df.describe()

# mean
def mean(df):
    return df.mean()

# median
def median(df):
    return df.median()

# std
def std(df):
    return df.std()


# # visualization: bar plot
def pd_visual(df, render=True): 
    df.plot(kind="hist")
    plt.xticks(rotation = 90)
    plt.ylabel('Frequency')
    plt.xlabel(df.name)
    if render:
        plt.show()
    else:
        plt.savefig('histgram.png')
    
# # For Polars
# # describe
# def polars_desc(df):
#     return df.describe()

# # visualization: histgram
# def polars_visual(df):
#     plt.hist(df["Model Year"])