from script import summary_desc, desc_pd

def test_summary_desc():
    df = df.read_csv('Electric_Vehicle_Population_Data.csv')
    
    # mean
    assert desc_pd(df).loc["mean", "Electric Range"] == 70.49573804284242
    assert summary_desc(df["Electric Range"])[0] == 70.49573804284242
    # median
    assert desc_pd(df).loc["50%", "Model Year"] == 2021.0
    assert summary_desc(df["Model Year"])[1] == 2021.0

    # standard deviation
    assert round(desc_pd(df).loc["std", "Electric Range"], 6) == 97.128735
    assert round(summary_desc(df["Electric Range"])[2], 6) == 97.128735

    