from game import *

def play(self): 
    self.get_user_item
    self.get_computer_item
    self.get_game_result

my_game=play(game)



# play(self) – the function that will be called from outside the class 
# # (ie. from rock-paper-scissors.py). It will do 3 things:
#             Get the user’s item (rock/paper/scissors) and remember it
#             Get a random item for the computer (rock/paper/scissors) and remember it
#             Determine the results of the game by comparing the user’s item 
#               and the computer’s item
#                 Print the output of the game; something like this: 
#                   “You selected rock. The computer selected paper. 
#                   You lose”, “You selected scissors. The computer selected scissors. 
#                   You drew!”
#                 Return the results of the game as a string: win;draw;loss;, 
#                   where win means that the user has won, draw means the user 
#                   and the computer got the same item, 
#                   and loss means that the user has lost.
