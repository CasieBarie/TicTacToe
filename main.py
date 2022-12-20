from player import Player
from game import Game
from welcome import Welcome

#delay time.sleep(seconds)
import time

#Clear console en reset color   cls()
import os


def cls():
    print("\033[0;37m.")
    os.system('cls' if os.name == 'nt' else 'clear')


#TicTacToe start message
welcome = Welcome()
welcome.logo()

#Players name and character select
cls()
player1 = Player()
player1.name = input("Player 1, What is your name? \033[1;34m")
player1.score = 0
player1.character = input(
    "\033[0;37m" + player1.name +
    ", which character do you want to play with? \033[1;34m")
while len(player1.character) >= 2 or len(player1.character) == 0:
    cls()
    print(
        "\033[1;31mYour character may only consist of one letter! \033[0;37mTry again!"
    )
    player1.character = input(
        player1.name +
        ", which character do you want to play with? \033[1;34m")
cls()
player2 = Player()
player2.name = input("Player 2, What is your name? \033[1;34m")
player2.score = 0
player2.character = input(
    "\033[0;37m" + player2.name +
    ", which character do you want to play with? \033[1;34m")
while len(player2.character) >= 2 or len(
        player2.character) == 0 or player1.character == player2.character:
    while len(player2.character) >= 2 or len(player2.character) == 0:
        cls()
        print(
            "\033[1;31mYour character may only consist of one letter! \033[0;37mTry again!"
        )
        player2.character = input(
            player2.name +
            ", which character do you want to play with? \033[1;34m")
        cls()
    while player1.character == player2.character:
        cls()
        print("\033[1;31mYou can't have the same sign! \033[0;37mTry again")
        player2.character = input(
            player2.name +
            ", which character do you want to play with? \033[1;34m")
        cls()

#Color player1
if player1.character == "X":
    player1.character = "\033[1;31mX\033[0;37m"
else:
    if player1.character == "O":
        player1.character = "\033[1;34mO\033[0;37m"
    else:
        player1.character = "\033[1;32m" + player1.character + "\033[0;37m"

#Color player2
if player2.character == "X":
    player2.character = "\033[1;31mX\033[0;37m"
else:
    if player2.character == "O":
        player2.character = "\033[1;34mO\033[0;37m"
    else:
        player2.character = "\033[1;33m" + player2.character + "\033[0;37m"

#Ask fot information
cls()
infoquestion = input(
    "Would you like more information before you start? \033[1;34m")
while infoquestion != "Yes" and infoquestion != "yes" and infoquestion != "No" and infoquestion != "no":
    cls()
    print("\033[1;31mI don't recognize this answer! \033[0;37mTry again!")
    infoquestion = input(
        "Would you like more information before you start? \033[1;34m")
if infoquestion == "yes" or infoquestion == "Yes":
    cls()
    welcome.info()

#Start game
game = Game(player1, player2)
doesPlay = True
while doesPlay == True:
    cls()
    print("Welcome " + player1.name + " and " + player2.name + "!")
    input("\nPress Enter to start! ")
    game.play()
    #Ask to start again
    print("The score is: " + str(player1.score) + "-" + str(player2.score))
    answer = input("\nDo you want to play again? \033[1;34m")
    while answer != "Yes" and answer != "yes" and answer != "No" and answer != "no":
        cls()
        game.board.print_board()
        game.check_winner_draw()
        game.check_winner()
        print("The score is: " + str(player1.score) + "-" + str(player2.score))
        print(
            "\n\033[1;31mI don't recognize this answer! \033[0;37mTry again!")
        antwoord = input("Do you want to play again? \033[1;34m")
    if answer == "No" or answer == "no":
        #Stop game
        doesPlay = False
        cls()
        if player1.score == player2.score:
            #draw
            print("The final score is: " + str(player1.score) + "-" +
                  str(player2.score))
            print("Its a draw")
            time.sleep(3)
            print("\nGoodbye!")
            os._exit(0)
        else:
            if player1.score <= player2.score:
                #Player2 win
                print("The final score is: " + str(player1.score) + "-" +
                      str(player2.score))
                print(player2.name + "[" + player2.character + "]" +
                      " has won! Congratulations!")
                time.sleep(3)
                print("\nGoodbye!")
                os._exit(0)
            else:
                #Player1 win
                print("The final score is: " + str(player1.score) + "-" +
                      str(player2.score))
                print(player1.name + "[" + player1.character + "]" +
                      " has won! Congratulations!")
                time.sleep(3)
                print("\nGoodbye!")
                os._exit(0)
    else:
        doesPlay = True