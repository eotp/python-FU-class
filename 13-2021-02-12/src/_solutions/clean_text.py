def clean_text(l, pattern):
    rv = []
    for s in l:
        for p in pattern:
            s = s.replace(p, ' ')
        s = s.strip()
        if s.startswith('Anmeldung'):
            pass
        else:
            rv.append(s)
    try:
        return rv[1]
    except:
        print(f'An exception occured!\n')
        pass
clean_text(txt, ['\n', 'Schließen', '\r'])
