
def fahrenheit_to_celsius(F):
    '''
    Function to compute Celsius from Fahrenheit
    '''
    K = fahrenheit_to_kelvin(F)
    C = kelvin_to_celsius(K)
    return C
