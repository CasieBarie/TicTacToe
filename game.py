from player import Player
from field import Field
import time

#Clear console en reset color   cls()
import os
def cls():
    print("\033[0;37m.")
    os.system('cls' if os.name=='nt' else 'clear')

class Game:
    players = None
    currentPlayer = 0
    turns = 0
    board = None
    state = "busy"
    point = True
    
    #constructor
    def __init__(self, player1, player2):
        #set spelers
        self.players = [player1, player2]
        #Bord waarde
        self.board = Field()

    def play(self):
        self.turns = 0
        self.state = "busy"
        self.currentPlayer = 0
        self.board = Field()
        self.point = True
        while self.state == "busy":
            cls()
            self.play_move()
            self.check_winner_draw()
            self.check_winner()

    def play_move(self):
        #Print current state of the board
        self.board.print_board()
        #Setup variables for input
        validInput = False
        pos = ""
        while validInput == False:
            #Ask player for input
            pos = self.players[self.currentPlayer].ask_input()
            #Validate input in the same if statement
            if self.board.validate_input(pos):
                #If this is correct then continue
                validInput = True
            else:
                if pos == "0,0" or pos == "0,1" or pos == "0,2" or pos == "1,0" or pos == "1,1" or pos == "1,2" or pos == "2,0" or pos == "2,1" or pos == "2,2":
                    cls()
                    print("\033[1;31mThis space is already occupied! \033[0;37mTry again!")
                    self.board.print_board()
                else:
                    cls()
                    print("\033[1;31mI don't recognize this! \033[0;37mTry again!")
                    self.board.print_board()
        self.board.use_input(pos, self.players[self.currentPlayer].character)
        self.currentPlayer = 1 if self.currentPlayer == 0 else 0

    #Check winner
    def check_winner(self):
        winner = self.board.get_winner();
        for i in range(0, len(self.players)):
            if self.players[i].character == winner:
                if self.point == True:
                    self.players[i].score += 1
                    self.point = False
                self.state = "over"
                cls()
                self.board.print_board()
                print("Game Over!  " + self.players[i].name + "[" + self.players[i].character + "] won this game, congratulations!")

    #Check draw
    def check_winner_draw(self):
        winnerdraw = self.board.get_draw();
        if(winnerdraw == "draw"):
            self.state = "over"
            cls()
            self.board.print_board()
            print("Game Over! It's a draw")