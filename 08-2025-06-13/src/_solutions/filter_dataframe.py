def filter_dataframe(df, threshold):
    # build pandas Series containing column name as index and ratio as value
    ratios = ((df.isnull().sum() / df.shape[0]) * 100).round(2)
    # get column names (index) for which ratio is under threshold
    columns_to_keep = ratios.loc[ratios <= threshold].index
    # get column names (index) for which ratio is over threshold
    columns_to_drop = ratios.loc[ratios > threshold].index
    # print dropped columns just to give info
    print(f"Dropped columns: {list(columns_to_drop)}")
    # return DataFrame only containing desired columns
    return df[columns_to_keep].copy()