def fahrenheit_to_kelvin(F):
    """
    Function to compute Fahrenheit from Kelvin
    """
    K = (F-32.0)*5/9 + 273.15
    return K

def kelvin_to_celsius(K):
    '''
    Function to compute Celsius from Kelvin
    '''
    C = K - 273.15
    return C

def fahrenheit_to_celsius(F):
    '''
    Function to compute Celsius from Fahrenheit
    '''
    K = fahrenheit_to_kelvin(F)
    C = kelvin_to_celsius(K)
    return C