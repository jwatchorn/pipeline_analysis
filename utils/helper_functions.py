
from scipy.stats import chi2_contingency, spearmanr
from collections import Counter
import string
import pandas as pd

def compute_year_correlation(df_counts : pd.Series, start_year : int, end_year : int) -> tuple:
    ''' This function creates a series from a year-frequency value counts object and returns a zero 
    filled sorted version, along with the correlation statistics
    
    Parameters
    ----------

        df_counts: pd.Series
            A pandas Series with years as index and frequency counts as values

        start_year: int
            The starting year for the correlation analysis

        end_year: int
            The ending year for the correlation analysis

    Returns
    -------

        tuple containing:
        
        filled_counts: pd.Series
            The series sorted ascending with missing years filled with zero counts
        
        rho: np.float64
            The Spearman correlation coefficient
        
        p: np.float64
            The p-value corresponding to the Spearman correlation
    '''

    #error handling for negative year spans
    if start_year>end_year:
        raise ValueError('start_year cannot be greater than end_year')
    

    #sort counts and then reindex between start and end with zero filling
    df_counts_sorted = df_counts.sort_index()
    filled_counts = df_counts_sorted.reindex(range(start_year,end_year+1),fill_value=0)

    #compute stats using scipy on the series - performed columnwise
    rho, p = spearmanr(filled_counts.index,filled_counts)

    return filled_counts, rho, p




def word_frequencies(text: str)-> dict: 
    '''This function counts the frequency of words in a string after stripping the punctuation
    
    Parameters
    ----------
    
        text: str
            a string you want to count the words within, words are deliniated by whitespace
            
    Returns
    -------
    
        Counter(words): dict-like
            A collections.Counter() dict-like object containing the words as keys and the frequencies as values
            
    '''

    #prune punctuation and replace with whitespace
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    #count words
    words = text.split()  
    return Counter(words) 




def sum_word_frequencies(series: pd.Series) -> dict:
    '''Computes the sum of word frequencies in a series containing strings, has some rudimentary error handling

    Parameters
    ----------

        series: pd.Series
            a column from a pandas dataframe or pandas series object that contains strings whose words we would like to count

    Returns
    -------

        total_word_freq: dict-like
            a Counter() object containing words as the keys and frequencies as values
    
    '''
   
    total_word_freq = Counter()
    
    #iterate through the elements of the series
    for text in series:
        
        #move to next row if empty
        if pd.isna(text):
            continue
        #otherwise update counter by calling word_frequencies
        else:
            total_word_freq.update(word_frequencies(text)) 
    
    return total_word_freq
