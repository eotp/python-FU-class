def schneiden():
    import time
    print('Schneide', end = '')
    for i in range(3):
        
        time.sleep(1)    
        print('.',end = '', flush = True)

def positionieren_und_schneiden(brot_laenge, brot_scheiben):

    brot_laenge = int(float(brot_laenge))
    brot_scheiben = int(brot_scheiben)
    
    anzahl_scheiben = brot_laenge//2

    if anzahl_scheiben > brot_scheiben:
        anzahl_scheiben = brot_scheiben
    
    for i in range(1,anzahl_scheiben + 1):
        print('')
        print(f'Positioniere Messer bei {2*i} cm')
        schneiden()
    
    print('Schneidvorgang abgeschlossen!')

brot_laenge = input('Wie lange ist das Brot in cm?')

brot_scheiben = input('Wieviele Scheiben sollen abgeschnitten werden')

positionieren_und_schneiden(brot_laenge, brot_scheiben)