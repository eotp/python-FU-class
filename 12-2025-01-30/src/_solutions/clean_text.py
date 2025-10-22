def clean_text(text, pattern=['\n', 'Schließen', '\r']):
    for p in pattern: 
        text = text.replace(p, ' ') # remove our specified patterns
    text = text.strip() # remove leading and tailing whitespace

    if text.startswith('Anmeldung'): # make sure we didn't get a "Anmeldungs-Link" by accident
        pass
    return text