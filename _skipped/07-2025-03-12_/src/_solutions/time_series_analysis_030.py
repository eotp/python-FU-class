## Solution Challenge 3

FILEPATH = "../data/Complete_TAVG_complete.txt"

COLUMN_NAMES = ["year", "month", "anomaly", "uncertainty"]

pd.read_csv(FILEPATH, 
            comment="%", 
            delim_whitespace=True, 
            header=None, 
            usecols=[0, 1, 2, 3], 
            names=COLUMN_NAMES)
