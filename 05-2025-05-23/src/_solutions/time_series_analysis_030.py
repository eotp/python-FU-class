## Solution Challenge 3

FILEPATH = "../data/Complete_TAVG_complete.txt"

# step 1: pd.read_csv(FILEPATH) # note this causes an ParserError, comment out that line
# step 2: pd.read_csv(FILEPATH, comment="%")
# step 3: pd.read_csv(FILEPATH, comment="%", sep=r'\s+')
# step 4: pd.read_csv(FILEPATH, comment="%", sep=r'\s+', header=None)
# step 5: pd.read_csv(FILEPATH, comment="%", sep=r'\s+', header=None, usecols=[0, 1, 2, 3])

COLUMN_NAMES = ["year", "month", "anomaly", "uncertainty"]
pd.read_csv(FILEPATH, comment="%", sep=r'\s+', header=None, usecols=[0, 1, 2, 3], names=COLUMN_NAMES)
