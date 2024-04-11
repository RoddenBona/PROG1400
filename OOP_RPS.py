import random

"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Respository: https://github.com/RoddenBona/PROG1700
Project: Object Oriented Programming: Rock Paper Scissors
Programming Language: Python 3
Version: 1
Last Edited April 11 2024
"""

options_list = ["rock", "paper", "scissors"]

#player class
class Player:
    def __init__(self,name):
        self.name = name
    def chose_move(self):
        pass

#computer player class
class HumanPlayer(Player):
    def choose_move(self):
        move = input(f"{self.name}. Enter your move 1(Rock Paper Scissors): ").lower()
        while move not in options_list:
            print("Invalid move. Please select rock, paper, or scissors")
            move = input(f"{self.name}. Enter your move 1(Rock Paper Scissors): ").lower()
        return move
    
    #make a computer player class
class CPU(Player):
    def choose_move(self):
        return random.choice(options_list)
    
class RPSgame:
    #Create the characters
    def __init__(self):
        self.player1 = HumanPlayer("Player1")
        self.player2 = CPU("Computer Player")

    def WinCondition(self, move1, move2):
        if move1 == move2:
            return "it's a tie!"
        elif move1 == "rock" and move2 == "scissors" or \
             move1 == "paper" and move2 == "rock" or \
             move1 == "scissors" and move2 == "paper":
                return f'{self.player1.name}. wins!'
        
    def PlayGame(self):
        print("Welcome to Rock Paper Scissors!!!!!!")
        move1 = self.player1.choose_move()
        move2 = self.player2.choose_move()
        print(f"{self.player1.name} chose {move1}")
        print(f"{self.player2.name} chose {move2}")

        result = self.WinCondition(move1,move2)
        print(result)

if __name__ == "__main__":
    game = RPSgame()
    game.PlayGame()