# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
for i in range(4) : print("hello world")


# 🌟 Exercise 2 : Some Math

# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

print((99^3)*8)

# 🌟 Exercise 3 : What’s your name ?

# Write code that asks the user for their name and determines 
# whether or not you have the same name, print out a funny message based on the outcome.

# name_guest=input("what's your name ? ")
# my_name= "François"
# if name_guest==my_name: print ("that's funny, we have the same name !")


# 🌟 Exercise 4 : Tall enough to ride a roller coaster
#     Write code that will ask the user for their height in centimeters.
#     If they are over 145cm print a message that states they are tall enough to ride.
#     If they are not tall enough print a message that says they need to grow some more to ride.

# height_guest=input("what's your height in centimeters ? ")
# if int(height_guest) > 145 : 
#     print("you're tall enough to ride !")
# else: 
#     print("you need to grow some more to ride.")


# 🌟 Exercise 5 : Favorite Numbers
# Key Python Topics:
#     Sets
#     Adding/removing items in a set
#     Set concatenation (using union)

# Instructions:
#     Create a set called my_fav_numbers and populate it with your favorite numbers.
#     Add two new numbers to the set.
#     Remove the last number you added to the set.
#     Create another set called friend_fav_numbers and populate it 
#     with your friend’s favorite numbers.
#     Concatenate my_fav_numbers and friend_fav_numbers to create a new set 
#     called our_fav_numbers.
#         Note: Sets are unordered collections, 
#     so ensure no duplicate numbers are added.

my_fav_numbers={1,3.14,-18,35}
my_fav_numbers.add(-15)
my_fav_numbers.add(77)
print(my_fav_numbers)
my_fav_numbers.remove(77)
print(my_fav_numbers)
friend_fav_numbers={7,3.14,10.4,90}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 6: Tuple
# Key Python Topics:
#     Tuples (immutability)
# Instructions:
#     Given a tuple of integers, try to add more integers to the tuple.
#     Hint: Tuples are immutable, meaning they cannot be changed after creation. 
#     Think about why you can’t add more integers to a tuple.
tuple_of_integers=(1,3,4,6)


# 🌟 Exercise 7: List Manipulation
# Key Python Topics: Lists
#     List methods: append, remove, insert, count, clear


# Instructions:

#     You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#     Remove "Banana" from the list.
#     Remove "Blueberries" from the list.
#     Add "Kiwi" to the end of the list.
#     Add "Apples" to the beginning of the list.
#     Count how many times "Apples" appear in the list.
#     Empty the list.
#     Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# 🌟 Exercise 8 : Sandwich Orders
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"].

#     The deli has run out of pastrami, use a while loop to remove all occurrences of Pastrami sandwich from sandwich_orders.

#     We need to prepare the orders of the clients:

#     Create an empty list called finished_sandwiches.
#     One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
#     After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
print(sandwich_orders)
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
finished_sandwiches=[]
sandwich_orders_initial=sandwich_orders[:] #conservation de la liste initiale pour que la boucle se passe bien
sandwich=""
while sandwich in sandwich_orders_initial:
    print(sandwich)
    finished_sandwiches.append(sandwich)
    print(finished_sandwiches)
    sandwich_orders.remove(sandwich)
    print(sandwich)


