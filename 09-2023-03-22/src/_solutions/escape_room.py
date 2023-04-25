{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a5104b9a-de96-45b4-b9f5-b29de82fb3ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Escape_Room:\n",
    "    def __init__(self):\n",
    "        \n",
    "        self.room1 = 'You see an empty room. There´s a door to the North.'\n",
    "        self.room1_id = True\n",
    "        \n",
    "        self.room2 = 'You see an almost identical room. There´s a key on the floor'\n",
    "        self.room2_id = False\n",
    "        self.key = False\n",
    "        \n",
    "    def __str__(self):\n",
    "        return f'Welcome to the Escape room!'\n",
    "\n",
    "    def walk(self,direction):\n",
    "        if self.room1_id == True:\n",
    "            if direction == 'North':\n",
    "                self.room1_id = False\n",
    "                self.room2_id = True\n",
    "                print('You enter a new room')\n",
    "                print(self.room2)\n",
    "        else:\n",
    "            print('You can´t go that way!')\n",
    "            \n",
    "        if self.room2_id == True:\n",
    "            if direction == 'South':\n",
    "                self.room1_id = True\n",
    "                self.room2_id = False\n",
    "                print('You enter a new room')\n",
    "                print(self.room1)\n",
    "        else:\n",
    "            print('You can´t go that way!')\n",
    "            \n",
    "    def look(self):\n",
    "        if self.room1_id == True:\n",
    "            print(self.room1)\n",
    "        if self.room2_id == True:\n",
    "            print(self.room2)\n",
    "            \n",
    "    def take(self,item):\n",
    "        if self.room1_id == True:\n",
    "            print('There´s nothing here!')\n",
    "        if self.room2_id == True:\n",
    "            print('You take the key!')\n",
    "            self.key = True\n",
    "            \n",
    "    def open(self,door):\n",
    "        if self.room1_id == True:\n",
    "            print('There´s nothing here!')\n",
    "        if self.room2_id == True:\n",
    "            if self.key == True:\n",
    "                print('You open the door and escape the room! Thanks for playing the game!')\n",
    "            else:\n",
    "                print('You should take the key!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "482b8334-d345-4dd0-ab8b-15dff80b09ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
