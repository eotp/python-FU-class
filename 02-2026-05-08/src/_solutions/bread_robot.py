import time

def positionieren(Länge_Brot, Stücke_Brot):
    # Position knife and cut
    for i in range(1, Stücke_Brot + 1):
        if Länge_Brot < 4:
            print('Brot zu kurz!')
            break
        else:
            print(f'Bewege Messer an Position {2 * i} cm ', end='')
            print('Schneide', end='')
            time.sleep(0.5)

        # Create progress bar
        for j in range(1, 4):  
            print('.', end='', flush=True)  
            time.sleep(0.5)

        print()

        # Break loop if condition is met
        if 2 * i >= Länge_Brot:
            break
        elif i == Stücke_Brot:
            break
        

def brotschneider():

    
    Brot = int(input('Länge des Brots in cm: '))
    Stücke = int(input('Wieviele Stücke sollen vom Brot geschnitten werden? '))
    

    positionieren(Brot, Stücke)

brotschneider()