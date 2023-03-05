import pandas as pd
import numpy as np

def is_weekend(row):
    if row["day_week"] > 4:
        return 1
    else:
        return 0

def date_transform(df):
    date = pd.DataFrame({"time" : []})
    date["time"] = pd.to_datetime(df["running_time"])
    date["month"] = date["time"].dt.month
    date["quarter"] = date["time"].dt.quarter
    date["day_week"] = date["time"].dt.dayofweek
    date["weekend"] = date.apply(is_weekend, axis=1)
    date["minute"] = date["time"].dt.minute.to_numpy(dtype=np.float32) #minute of the day
    date["hour"] = date["time"].dt.hour.to_numpy(dtype=np.float32)
    #date["hour"] = date["time"].dt.hour.to_numpy(dtype=np.int32) #hour of the day
    df = df.join(date)
    return df