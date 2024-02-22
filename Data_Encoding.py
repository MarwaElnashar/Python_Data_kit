# 4. Categorical Data Encoding:
# - Objective: Design functions for encoding categorical data, allowing their conversion into numerical formats for analysis.
# - Tools: Implement encoding techniques effectively.


def Data_Encoding(data,method,column='Category'):
    """Encoding categorical data, allowing their conversion into numerical formats for analysis.
    Parameters: data, method, column
    Supported method: label_encode, one_hot_encode
    column: column name that
    
    Return data with numerical format
    """
    data_encoded = data.copy()
    if method=='label_encode':
        
        data_encoded[column] = pd.factorize(data_encoded[column])[0]
        return data_encoded
    elif method=='one_hot_encode':  
       
        data_encoded = pd.get_dummies(data_encoded, columns=[column])
        return data_encoded

# Example usage:
data = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B'],
                     'Value': [10, 20, 15, 25, 30]})

print(Data_Encoding(data,'label_encode','Category'))
print(Data_Encoding(data,'one_hot_encode','Category'))