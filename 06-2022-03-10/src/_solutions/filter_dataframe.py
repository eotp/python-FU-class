
def filter_dataframe(df, threshold):
    p_null = round((df.isnull().sum() / df.shape[0]) * 100, 2)
    return df.drop(p_null[p_null > threshold].index, axis = 1)