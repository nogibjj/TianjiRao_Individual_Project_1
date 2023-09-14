"""
Test goes here
"""

from lib import pd_desc, pd_visual
import pandas as pd

def test_desc_df():
    df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
    # mean
    assert pd_desc(df).loc["mean", "Electric Range"] == 70.49573804284242
    # median
    assert pd_desc(df).loc["50%", "Model Year"] == 2021.0
    # standard deviation
    assert pd_desc(df).loc["std", "Electric Range"] == 97.12873497790751


def test_bar_plot():
    df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
    # Here we can focus on the visualization of Electric Range using a histgram
    # Since the data set is too large to run in codespace, 
    # here we only use the first 500 observation as an example
    pd_visual(df["Electric Range"][:500])
    
if __name__ == "__main__":
    test_bar_plot()