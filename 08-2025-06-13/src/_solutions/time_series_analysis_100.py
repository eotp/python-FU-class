## Solution Challenge 10
def data_url(country):
    '''
    Function to build url for data retrieval
    '''
    BASE_URL = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Regional/TAVG/"
    SUFFIX_URL = "-TAVG-Trend.txt"
    return(BASE_URL + country + SUFFIX_URL)