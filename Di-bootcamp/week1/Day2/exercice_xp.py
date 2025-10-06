# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:
#     Creating dictionaries
#     Zip function or dictionary comprehension
# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys 
# and the second list contains the corresponding values.
# Lists:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dictionary=zip(keys,values)
print(list(my_dictionary))

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:
#     Looping through dictionaries
#     Conditionals
#     Calculations

# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
#     Family members’ ages are stored in a dictionary.
#     The ticket pricing rules are as follows:
#         Under 3 years old: Free
#         3 to 12 years old: $10
#         Over 12 years old: $15
# Family Data:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

#     Loop through the family dictionary to calculate the total cost.
#     Print the ticket price for each family member.
#     Print the total cost at the end.
total_price=0
for first_name in family:
    age=family[first_name]
    if age<=3: price=0
    elif age<=12: price=10
    else: price=15
    total_price=total_price + price
    print(f"the price for {first_name} is {price}")

# print(f"total_price: {total_price}")

# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.


# 🌟 Exercise 3: Zara
# Key Python Topics:
#     Creating dictionaries
#     Accessing and modifying dictionary elements
#     Dictionary methods like .pop() and .update()
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

#     Create a dictionary called brand with the provided data.
zara_dictionnary={"name": "Zara", "creation_date": 1975, "creator_name": "Amancio Ortega Gaona", 
"type_of_clothes": ("men", "women", "children", "home"), "international_competitors": ("Gap", "H&M", "Benetton"),
"number_stores": 7000, "major_color": {"France": "blue", "Spain": "red", "US": ("pink", "green")}}

#     Modify and access the dictionary as follows:
#         Change the value of number_stores to 2.

zara_dictionnary["number_stores"]=2

#         Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"here are the different types of clothes : {zara_dictionnary["type_of_clothes"]}")

#         Add a new key country_creation with the value Spain.

#         Check if international_competitors exists and, if so, add “Desigual” to the list.
if zara_dictionnary["international_competitors"]!=None:
    zara_dictionnary["international_competitors"]=zara_dictionnary["international_competitors"]+('Desigual',)

#         Delete the creation_date key.
zara_dictionnary.pop("creation_date")

#         Print the last item in international_competitors.
print(zara_dictionnary["international_competitors"][-1])
#         Print the major colors in the US.
print(zara_dictionnary["major_color"]["US"])

#         Print the number of keys in the dictionary.
print(len(zara_dictionnary))

#         Print all keys of the dictionary.
print(zara_dictionnary.keys())


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. 
more_on_zara={"creation_date": 1975, "number_stores": 10000}

# Merge this dictionary with the original brand dictionary and 
# print the result.
zara_dictionnary.update(more_on_zara)
print(zara_dictionnary)

# 🌟 Exercise 4 : Some Geography
# Goal: Create a function that describes a city and its country.
# Key Python Topics:
#     Functions with multiple parameters
#     Default parameter values
#     String formatting


# Step 1: Define a Function with Parameters
#     Define a function named describe_city().
#     This function should accept two parameters: city and country.
#     Give the country parameter a default value, such as “Unknown”.
def describe_city(city,country="unknnown"):

# Step 2: Print a Message
#     Inside the function, set up the code to display a sentence like “ is in “.
#     Replace <city> and <country> with the parameter values.
    print(f"{city} is in {country}")

# Step 3: Call the Function
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#     Call the describe_city() function with different city and country combinations.
#     Try calling it with and without providing the country argument to see the default value in action.
#     Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
# Expected Output:
# Reykjavik is in Iceland.
# Paris is in Unknown.


# 🌟 Exercise 5 : Random
# Goal: Create a function that generates random numbers and compares them.
# Key Python Topics:
#     random module
#     random.randint() function
#     Conditional statements (if, else)
# Step 1: Import the random Module
import random
#     At the beginning of your script, use import random to access the random number generation functions.
# Step 2: Define a Function with a Parameter
#     Create a function that accepts a number between 1 and 100 as a parameter.
def random_100(user_number):
    random_number=random.randint(1,100)
    # Step 3: Generate a Random Number
#     Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
# Step 4: Compare the Numbers
    if user_number==random_number:
        print("you're lucky!")
    else:
        print("you haven't guessed")
        print(f"random number was {random_number}, your number is {user_number}")
#     If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
# Step 5: Call the Function
#     Call the function with a number between 1 and 100.
# Expected Output:
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)
random_100(67)


# 🌟 Exercise 6 : Let’s create some personalized shirts !
# Goal: Create a function to describe a shirt’s size and message, with default values.
# Key Python Topics:
#     Functions with parameters and default values
#     Keyword arguments
# Step 1: Define a Function with Parameters

#     Define a function called make_shirt().
def make_shirt(size="large",text="I love Python"):
#     This function should accept two parameters: size and text.
# Step 2: Print a Summary Message
#     Set up the function to display a sentence summarizing the shirt’s size and message.
    print(f"your shirt is {size} size and your message is {text}")
# Step 3: Call the Function
make_shirt("XL", "i'm a genius")
# Step 4: Modify the Function with Default Values
#     Modify the make_shirt() function so that size has a default value of “large” and text has a default value 
# of “I love Python”.
# Step 5: Call the Function with Default and Custom Values
#     Call make_shirt() to make a large shirt with the default message.
#     Call make_shirt() to make a medium shirt with the default message.
#     Call make_shirt() to make a shirt of any size with a different message.
make_shirt("large")
make_shirt("medium")
make_shirt("any","I'm a genius")
# Step 6 (Bonus): Keyword Arguments

#     Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).


# Expected Output:

# The size of the shirt is large and the text is I love Python.
make_shirt(size="small", text="Custom message")
# The size of the shirt is medium and the text is I love Python.
make_shirt(size="medium")
# The size of the shirt is small and the text is Custom message.
make_shirt(text="Custom message", size="small")



# 🌟 Exercise 7 : Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
# Key Python Topics:
#     Functions
#     Conditionals (if / elif)
#     Random numbers
#     Floating-point numbers (Bonus)
#     Handling seasons (Bonus)
# Step 1: Create the get_random_temp() Function
def get_random_temp():
    return random.uniform(-10,40)
#     Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
# Step 2: Create the main() Function
def main():
    temperature=get_random_temp()
    print(f"the temperature right now is {temperature}")
    if temperature<0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temperature<16:
        print("Quite chilly! Don’t forget your coat.")
    elif temperature<23:
        print("Nice weather.")
    elif temperature<32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
main()
#     Create a function called main(). Inside this function:
#         Call get_random_temp() to get a random temperature.
#         Store the temperature in a variable and print a friendly message like:
#         “The temperature right now is 32 degrees Celsius.”
# Step 3: Provide Temperature-Based Advice

#     Inside main(), provide advice based on the temperature:
#         Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
#         Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
#         Between 16°C and 23°C: e.g., “Nice weather.”
#         Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
#         Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”
# Step 4: Floating-Point Temperatures (Bonus)
#     Modify get_random_temp() to return a random floating-point number using random.uniform() 
# for more accurate temperature values.

# Step 5: Month-Based Seasons (Bonus)

#     Instead of directly generating a random temperature, ask the user for a month (1-12) 
# and determine the season using if/elif conditions.
#         Modify get_random_temp() to return temperatures specific to each season.


# Expected Output:

# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.


# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:
#     Loops
#     Lists
#     String formatting
# Instructions:

#     Write a loop that asks the user to enter pizza toppings one by one.
user_answer=""
toppings_list=[]
while user_answer!="quit":
    user_answer=input("enter a topping (type 'quit' to stop): ")
    if user_answer!="quit":
        toppings_list.append(user_answer)
        print(f"Adding {user_answer} to your pizza.")

#     Stop the loop when the user types 'quit'.
#     For each topping entered, print:
#     "Adding [topping] to your pizza."
#     After exiting the loop, print all the toppings and the total cost of the pizza.
print("your pizza has the following toppings:")
for topping in toppings_list:
    print(topping)
print(f"the total price of your pizza is ${10 + 2.5*len(toppings_list)}")
#         The base price is $10, and each topping adds $2.50.


