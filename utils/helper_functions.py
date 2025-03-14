
from scipy.stats import chi2_contingency, spearmanr
import pandas as pd

def compute_year_correlation(df_counts, start_year, end_year):
    ''' This function creates a series from a year-frequency value counts object and returns a zero filled sorted version, along with the correlation statistics
    parameters:
    df_counts: pd.Series
        A pandas Series with years as index and frequency counts as values

    start_year: int
        The starting year for the correlation analysis

    end_year: int
        The ending year for the correlation analysis

    returns:
        tuple containing:
        - filled_counts (pd.Series): The series with missing years filled with zero counts
        - rho (float): The Spearman correlation coefficient
        - p (float): The p-value corresponding to the Spearman correlation


    '''

    if start_year>end_year:
        raise ValueError('start_year cannot be greater than end_year')
    

    df_counts_sorted = df_counts.sort_index()
    filled_counts = df_counts_sorted.reindex(range(start_year,end_year+1),fill_value=0)

    rho, p = spearmanr(filled_counts.index,filled_counts)

    return filled_counts, rho, p


