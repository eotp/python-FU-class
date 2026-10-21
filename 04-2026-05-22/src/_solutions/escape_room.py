class Escape_Room:
    def __init__(self):
        
        self.room1 = 'You see an empty room. There´s a door to the North.'
        self.room1_id = True
        
        self.room2 = 'You see an almost identical room. There´s a key on the floor'
        self.room2_id = False
        self.key = False
        
    def __str__(self):
        return f'Welcome to the Escape room!'

    def walk(self,direction):
        if self.room1_id == True:
            if direction == 'North':
                self.room1_id = False
                self.room2_id = True
                print('You enter a new room')
                print(self.room2)
            else:
                print('You can´t go that way!')
       
            
        elif self.room2_id == True:
            if direction == 'South':
                self.room1_id = True
                self.room2_id = False
                print('You enter a new room')
                print(self.room1)
            else:
                print('You can´t go that way!')
            
    def look(self):
        if self.room1_id == True:
            print(self.room1)
        if self.room2_id == True:
            print(self.room2)
            
    def take(self,item):
        if self.room1_id == True:
            print('There´s nothing here!')
        if self.room2_id == True:
            print('You take the key!')
            self.key = True
            
    def open(self,door):
        if self.room2_id == True:
            print('There´s nothing here!')
        elif self.room1_id == True:
            if self.key == True:
                print('You open the door and escape the room! Thanks for playing the game!')
            else:
                print('You should take the key!')

