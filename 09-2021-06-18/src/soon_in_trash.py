# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:39:35 2021

@author: Study
"""

import numpy as np

class TTT:
    def __init__(self):
        self.board = np.zeros((3,3))
        self.turn = 'Player'      
        
    def choice_possible(self, i,j):
        if self.board[i,j] == 0: return True
        else: return False
        
    def print_board(self):
        print("-------------------")
        for i in range(len(self.board)):
            s = "|"
            for j in range(len(self.board)):
                s += " " + str(self.board[i,j]) + " |"
            print(s)
            print("-------------------")
    
    def players_turn(self):
        while True:
            player_choice = input("Please enter row and column to place Cross (SEPERATED BY COMMA, e.g.: 1,2): ")
            row, col = player_choice.split(',')
            row = int(row)
            col = int(col)
            if self.choice_possible(row, col):
                self.board[row, col] = 1
                break
            else:
                print('This field is already occupied. Please choose another one')
                            
    def check_win(self):
        row_sum = self.board.sum(axis=1)
        col_sum = self.board.sum(axis=0)
        diag_sum = self.board.diagonal().sum()
        mirr_diag_sum = np.fliplr(self.board).diagonal().sum()
        
        ## Schauen ob jemand gewonnen hat
        if (
            np.any(row_sum == 3) or np.any(row_sum == -3) or
            np.any(col_sum == 3) or np.any(col_sum == -3) or 
            np.any(diag_sum == 3) or np.any(diag_sum == -3) or
            np.any(mirr_diag_sum == 3) or np.any(mirr_diag_sum == -3)
        ):  
            print(f'{self.turn} won')
            self.print_board()
            return True
              
        ## Schauen ob alle Felder belegt sind
        if not 0 in self.board:
            print(f'All fields taken, thus draw.')
            return True         
        return False   
    
    def ai_turn(self):
        while True:
            row = np.random.randint(0,3)
            col = np.random.randint(0,3)
            if self.choice_possible(row, col):
                self.board[row, col] = -1
                break    
    
    def play(self):
        while True:
            self.turn = 'Player'
            self.players_turn()
            if self.check_win(): break
            self.print_board() 
            
            self.turn = 'AI'
            print("AI's Choice:")
            self.ai_turn()
            if self.check_win(): break
            self.print_board()           
            
            
if __name__ == '__main__':
    ttt = TTT()
    ttt.play()