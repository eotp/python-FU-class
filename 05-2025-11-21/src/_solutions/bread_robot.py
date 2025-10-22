import time

def positionieren(Länge_Brot, Stücke_Brot):
    
    # Position knife and cut
    for i in range(1, Stücke_Brot + 1):
        
        # Break loop if condition is met  
        if (2 * i >= Länge_Brot):
            print('Brot zu kurz!')
            break
        
        elif (i != Stücke_Brot + 1):
            print(f'Bewege Messer an Position {2 * i} cm ', end='')
            print('Schneide', end='')
            time.sleep(0.5)

        # Create progress bar
        for j in range(1, 4):  
            print('.', end='', flush=True)  
            time.sleep(0.5)
            
        if (i == Stücke_Brot):
            print()
            print('Schneidvorgang beendet!')
        print()
           

def brotschneider():
    
    Brot = float(input('Länge des Brots in cm: '))
    Stücke = int(input('Wieviele Stücke sollen vom Brot geschnitten werden? '))  

    positionieren(Brot, Stücke)

brotschneider()