# 1. Data Reading:
# - Objective: Implement functions that can read data from different file formats such as CSV, Excel, and JSON.
# - Tools: Use Pandas for efficient data importing.


import pandas as pd
def DataReading(filepath):
    
    """
    Read data from CSV, Excel, or JSON file.
        Parameters:
            filepath (str): The path to the file.
        Returns:
            DataFrame: A pandas DataFrame containing the data from the file.
    """
    df=pd.DataFrame()
    
    if filepath[-4:]==".csv":
       df= pd.read_csv(filepath, index_col=0)
       return df
    elif filepath[-5:]==".xlsx":
        df= pd.read_excel(filepath)
    elif filepath[-4:]==".json":
        df= read_json(filepath)
# df = DataReading("Hitters.json")
# print(df)