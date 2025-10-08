# Exercise 1: Birthday Look-up
#     Create a variable called birthdays. Its value should be a dictionary.
# birthdays={}

# #     Initialize this variable with the birthdays of 5 people of your choice. 
# # For each entry in the dictionary, the key should be the person’s name, 
# # and the value should be their birthday. 
# # Tip: Use the format "YYYY/MM/DD".
# birthdays.update(
#     {"François":"05/11/1963",
#     "Dominique":"05/07/1962",
#     "Isabelle":"28/12/65",
#     "Catherine":"11/11/59",
#     "Brigitte":"14/05/58"})

# user_name=input("what's your name ? ")

# print("welcome",user_name)


# #     Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”
# #         Ask the user to give you a person's name and store the answer in a variable.
# #         Get the birthday of the name provided by the user.
# #         Print out the birthday with a nicely-formatted message.


# # Exercise 2: Birthdays Advanced

# #     Before asking the user to input a person's name, print out all of the names 
# #       in the dictionary.
# #     If the person that the user types is not found in the dictionary, 
# # print an error message 
# # (“Sorry, we don’t have the birthday information for person's name”).
# print ("here is the list of names I've got: ")
# print (birthdays.keys())

# answer=input("please give me a name ")

# if answer in birthdays:
#     print(f"the birthday date of {answer} is {birthdays[answer]}")
# else:
#     print(f"I haven't got the birthday date of {answer}")

# # Exercise 3: Check the index
# # Instructions
# # Using this variable
# # names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name=input("what's your name ? ")
# if user_name in names: print(names.index(user_name))
# # Ask a user for their name, if their name is in the names list, 
# # print out the index of the first occurence of the name.
# # Example: if input is 'Cortana' we should be printing the index 1


# # Exercise 4: Double Dice

#     Create a function that will simulate the rolling of a dice. Call it throw_dice. 
import random
def throw_dice():
    return random.randint(1,6)

#     It should return an integer between 1 and 6.
#     Create a function called throw_until_doubles.
#     It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, i.e., until we reach doubles.
#     For example: (1, 2), (3, 1), (5, 5) → then stop throwing, because doubles were reached.
#     This function should return the number of times it threw the dice in total. In the example above, it should return 3.
#     Create a main function. It should throw doubles 100 times (i.e., call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).
#     After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
#     Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
history={}

def main():
    total_throws=0
    i=0
    for i in range(100):
        throw_dice1=throw_dice()
        throw_dice2=throw_dice()
        total_throws+=1
        while throw_dice1!=throw_dice2:
            throw_dice1=throw_dice()
            throw_dice2=throw_dice()
            total_throws+=1
        history.update({i:total_throws})
        total_throws=0

main()
sum_throws=0
for key in history:
    sum_throws+=history[key]    
print("Total throws:",sum_throws)
print("Average throws to reach doubles:",round(sum_throws/100,2))   
#     Finally, call your main function to run the program.



 

# For example:

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):

# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)

# Then my output would show something like this:

# Total throws: 8
# Average throws to reach doubles: 2.67.
