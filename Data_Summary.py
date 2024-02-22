# 2. Data Summary:
# - Objective: Develop functions to print key statistical summaries of the data, including metrics like the average and most frequent values.
# - Tools: Utilize NumPy and Pandas to generate these summaries.


import pandas as pd

def Data_Summary(data):
    """
    Print key statistical summaries of the data.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing the data.
    Return:
        Data Summary including metrics like the average and most frequent values
    """
    # Summary statistics
    summary = data.describe()
    print("Summary Statistics:",summary)
   
    
    # Average values
    average = data.mean()
    print("Average Values:")
    print(average)
    
    # Most frequent values
    most_frequent = data.mode().iloc[0]
    print("Most Frequent Values:")
    print(most_frequent)
  

# Example usage:
data = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                     'B': [2, 3, 4, 5, 6],
                     'C': [3, 4, 5, 6, 7]})

Data_Summary(data)