
# Steps
# Part I - game.py
#     game.py – this file/module should contain a class called Game. 
# def imprime(s1, s2, r):
#     print(f"your answer was {s1}; the computer answer was {s2} ; and the result is {r} four you")
list_items=("rock","paper","scissors")
import random

class game:    
# It should have 4 methods:
#         get_user_item(self) – Ask the user to select an item (rock/paper/scissors). 
# Keep asking until the user has selected one of the items – 
# use data validation and looping. Return the item at the end of the function.
# It should have 4 methods:
#         get_user_item(self) – Ask the user to select an item (rock/paper/scissors). 
# Keep asking until the user has selected one of the items – 
# use data validation and looping. Return the item at the end of the function.
    def get_user_item(self):
        user_item=input(f"please give me an item in the list {list_items} ")
        while user_item not in list_items:  
            print("your answer is not in the list")          
            user_item=input(f"please give me an item in the list {list_items} ")    
        return(user_item)
    
       
#         get_computer_item(self) – Select rock/paper/scissors at random for the computer. 
# Return the item at the end of the function. Use python’s random.choice() function
#  (read about it online).
    def get_computer_item(self):
        computer_item=random.choice(list_items)
        return(computer_item)


#         get_game_result(self, user_item, computer_item) – Determine the result of the game.
#             Parameters:
#                 user_item – the user’s chosen item (rock/paper/scissors)
#                 computer_item – the computer’s chosen (random) item (rock/paper/scissors)
#                 Return either win, draw, or loss. Where win means that the user has won,
#  draw means the user and the computer got the same item, 
# and loss means that the user has lost.

    def get_game_result(self, user_item, computer_item):
        self.user_item=user_item()
        self.computer_item=computer_item()
        if self.user_item==self.computer_item:
            result="draw"
            print(f"You selected {self.user_item}.The computer selected {self.computer_item}. You drew!")
        elif (list_items.index(self.user_item)-list_items.index(self.computer_item))%3==1:
            result="win"
            print(f"You selected {self.user_item}. The computer selected {self.computer_item}. You win!")
        else:
            result="loss"
            print(f"You selected {self.user_item}. The computer selected {self.computer_item}. You lose!")
    
my_game=game()
my_game.get_user_item()
my_game.get_computer_item()
my_game.get_game_result(my_game.get_user_item,my_game.get_computer_item)