from main import summary_desc, visual, save_to_md
# import pandas as pd

def test_summary_desc():
    result = summary_desc()
    
    # mean
    assert result.loc["mean", "Electric Range"] == 70.49573804284242

    # median
    assert result.loc["50%", "Model Year"] == 2021.0

    # standard deviation
    assert round(result.loc["std", "Electric Range"], 6) == 97.128735

def test_visual():
    visual()
    
def test_save_to_md():
    save_to_md()