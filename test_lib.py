"""
Test goes here
"""

from lib import pd_desc, mean, median, std

import pandas as pd

def test_desc_df():
    data = { '1': [1,2,3],
             '2': [3,4,5],
             '3': [6,7,8]
            }
    
    df = pd.DataFrame(data)
    # mean
    assert pd_desc(df).loc["mean", "1"] == 2.0
    assert mean(df['1']) == 2.0
    
    # median
    assert pd_desc(df).loc["50%", "2"] == 4.0
    assert median(df['2']) == 4.0
    
    # standard deviation
    assert pd_desc(df).loc["std", "3"] == 1.0
    assert std(df['3']) == 1.0