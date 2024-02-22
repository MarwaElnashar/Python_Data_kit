# 3. Handling Missing Values:
# - Objective: Create functions for addressing missing values, offering solutions to either remove or impute them based on set strategies.
# - Tools: Employ methods that ensure data integrity.


def remove_missing_values(data,strategy):
    """ Remove missing values from the DataFrame.
    Parameters: data, strategy
    Supported strategies are 'remove', 'mean', 'median', and 'mode'

    Return data without null value
    """
    if strategy == 'remove':
        data= data.dropna()
    elif strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])  # Use the first mode if multiple modes exist
    else:
        raise ValueError("Invalid imputation strategy. Supported strategies are 'remove', 'mean', 'median', and 'mode'.")


