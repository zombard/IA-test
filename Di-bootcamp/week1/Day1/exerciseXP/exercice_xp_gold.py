# Exercise 1: What is the Season?
#     Ask the user to input a month (1 to 12).
#     Display the season of the month received:
#         Spring runs from March (3) to May (5)
#         Summer runs from June (6) to August (8)
#         Autumn runs from September (9) to November (11)
#         Winter runs from December (12) to February (2)

my_dictionnary={}

for i in range(12):
    if i//3==0:
        if i==0:
            my_dictionnary.update({12:"Winter"})
        else:
            my_dictionnary.update({i:"Winter"})
    if i//3==1:
        my_dictionnary.update({i:"Spring"})
    if i//3==2:
        my_dictionnary.update({i:"Summer"})
    if i//3==3:
        my_dictionnary.update({i:"Automn"})        
print(my_dictionnary)
#guest_number=input("entrez un n° de mois (entre 1 et 12) ")
print(f"The season of this month is {my_dictionnary[int(guest_number)]}")

# Exercise 2: For Loop
# Key Python Topics:
#     Loops (for) Range and indexing
# Instructions:
#     Write a for loop to print all numbers from 1 to 20, inclusive.
for i in range(20):
    print(i+1)
#     Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range(20):
    if i%2==1:
        print(i+1)
# Exercise 3: While Loop
# Key Python Topics: Loops (while), Conditionals
# Instructions:
#     Write a while loop that keeps asking the user to enter their name.
#     Stop the loop if the user’s input is your name.

my_name= "François"
user_name=""
while user_name!=my_name:
    user_name=input("what is your name ? ")
print("your name is the same as my name !!")

# Exercise 4: Check the index
# Using this variable:
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurrence 
# of the name.
# Example: if input is Cortana we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name=input("what is your name ? ")
if user_name in names:
    print(f"the index of this name is {names.index(user_name)}")

# Exercise 6: Random number
#     Ask the user to input a number from 1 to 9 (including).
#     Get a random number between 1 and 9. Hint: random module.
#     If the user guesses the correct number print a message that says “Winner”.
#     If the user guesses the wrong number print a message that says “Better luck next time.”

# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop, tally up and display total games won and lost

import random

number_to_guess=int(random.random()*9)
print(number_to_guess)
user_number=10
while user_number !=0:
    user_number=int(input("please give me a number between 1 and 9 (0 to quit): "))
    if user_number==number_to_guess:
        print("winner")
        break
    else :
        print("Better luck next time.")