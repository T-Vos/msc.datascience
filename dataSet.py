import pandas as pd
import numpy as np

def cut_year_title_down(title):
    # world bank columns end with [YRxxxx] EG: 1970 [YR1970]
    # This can be cut a way easily
    if title[0].isdigit() : title = title[0:4]
    return title

def drop_non_year_column(titles):
    # Get Years in dataset
    drops = []
    for title in titles:
        if not title.isdigit() : drops.append(title)
    return drops

educationData = pd.read_csv('../Data/Education_WB/edData.csv')
gdpPerCap = pd.read_csv('../Data/GDP2_WB/ad361792-9e4a-4b48-adb6-6422cf32b3fe_Data.csv')