def convert2meter(s, input_unit="in"):
    
    def convert_girth(s):
        return s*0.0254

    def convert_height(s):
        return s*0.3048

    def convert_volume(s):
        return s*0.0283168
    '''
    Function to convert inches, feet and cubic feet to meters and cubic meters 
    '''
    if input_unit == "in":
        return convert_girth(s)
    elif input_unit == "ft":
        return convert_height(s)
    elif input_unit == "cft":
        return convert_volume(s)
    else:
        print("Error: Input unit is unknown.")