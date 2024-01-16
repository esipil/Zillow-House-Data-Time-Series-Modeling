## Importing the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def state_roi(df, state):
    df = df[df["State"] == state].resample("MS")["value"].mean()
    end_date = df.index[-1]
    start_date = df.index[-1] - pd.DateOffset(years=10)
    roi = ((df.loc[end_date] - df.loc[start_date]) / df.loc[start_date]) * 100
    return roi

def top_10_states_on_roi (ten_yrs_df):
    states_list = list(ten_yrs_df["State"].unique())
    state_roi_dict = {}
    for state in states_list:
        state_roi_dict[state] = state_roi(ten_yrs_df, state)
    top_10 = sorted(state_roi_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10

def state_cagr(df, state):
    df = df[df["State"] == state].resample("MS")["value"].mean()
    end_date = df.index[-1]
    start_date = df.index[-1] - pd.DateOffset(years=10)
    num_years = (end_date - start_date).days / 365.25  # Adjust for leap years
    cagr = ((df.loc[end_date] / df.loc[start_date]) ** (1/num_years)) -1
    return cagr * 100

def top_10_states_on_cagr(df):
    states_list = list(df["State"].unique())
    state_cagr_dict = {}
    for state in states_list:
        state_cagr_dict[state] = state_cagr(df, state)
    top_10 = sorted(state_cagr_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10

def plot_top_10(top_10_roi, top_10_cagr):
    states_roi, values_roi = zip(*top_10_roi)
    states_cagr, values_cagr = zip(*top_10_cagr)

    # Create bar plots in the same figure with improved aesthetics
    fig, ax = plt.subplots(figsize=(12, 8))

    # Bar plot for ROI
    bar_width = 0.4
    index_roi = np.arange(len(states_roi))
    ax.bar(index_roi, values_roi, width=bar_width, color='#3498db', alpha=0.7, label='ROI', edgecolor='black', linewidth=0.8)

    # Bar plot for CAGR
    index_cagr = index_roi + bar_width
    ax.bar(index_cagr, values_cagr, width=bar_width, color='#2ecc71', alpha=0.7, label='CAGR', edgecolor='black', linewidth=0.8)

    # Customize x-axis ticks and labels
    ax.set_xticks(index_roi + bar_width / 2)
    ax.set_xticklabels(states_roi, fontsize=12, rotation=45, ha='right')

    # Set labels and title
    ax.set_ylabel('Percentage', fontsize=14)
    ax.set_title('Top 10 States by ROI and CAGR', fontsize=16)
    ax.legend(fontsize=12)

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add grid
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()

def state_roi_20yrs(df, state):
    df = df[df["State"] == state].resample("MS")["value"].mean()
    end_date = df.index[-1]
    start_date = df.index[-1] - pd.DateOffset(years=20)
    roi = ((df.loc[end_date] - df.loc[start_date]) / df.loc[start_date]) * 100
    return roi

def state_cagr_20yrs(df, state):
    df = df[df["State"] == state].resample("MS")["value"].mean()
    end_date = df.index[-1]
    start_date = df.index[-1] - pd.DateOffset(years=20)
    num_years = (end_date - start_date).days / 365.25  # Adjust for leap years
    cagr = ((df.loc[end_date] / df.loc[start_date]) ** (1/num_years)) -1
    return cagr * 100

def top_20_states_on_roi (df):
    states_list = list(df["State"].unique())
    state_roi_dict = {}
    for state in states_list:
        state_roi_dict[state] = state_roi_20yrs(df, state)
    top_20 = sorted(state_roi_dict.items(), key=lambda x: x[1], reverse=True)[:20]
    return top_20

def top_20_states_on_cagr(df):
    states_list = list(df["State"].unique())
    state_cagr_dict = {}
    for state in states_list:
        state_cagr_dict[state] = state_cagr_20yrs(df, state)
    top_20 = sorted(state_cagr_dict.items(), key=lambda x: x[1], reverse=True)[:20]
    return top_20



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

