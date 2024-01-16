## Importing the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt

def ROI (df, frequency=10):
    """
    This function takes in a dataframe and returns the Zipcodes with the best ROI for a given frequency. eg 3 year best ROI for the last 3 years
    """ 
    zipcode_roi = {}
    zipcodes = zipcodes = list(df["ZipCode"].unique())
    end_date = df.index[-1]
    start_date = df.index[-1] - pd.DateOffset(years=frequency)
    for zipcode in zipcodes:
        roi = ((df[df["ZipCode"] == zipcode].loc[end_date]["value"] - df[df["ZipCode"] == zipcode].loc[start_date]["value"])  / df[df["ZipCode"] == zipcode].loc[start_date]["value"]) * 100
        zipcode_roi[zipcode] = roi
    return zipcode_roi

