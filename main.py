from lib import pd_desc, mean, median, std

def summary_desc(df):
    return [mean(df), median(df), std(df)]

def desc_pd(df):
    return pd_desc(df)