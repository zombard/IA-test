# Create a file called operators.py

# Create 2 functions : addOperator(x,y) that returns the addition of 2 numbers, 
# and divideOperator(x,y) that returns the division of 2 numbers
# Create another file called calculator.py, and import the operators module. Call the 2 functions and display the results

# Do this process 3 times :

#     once by importing the whole module
#     the second time by importing specific functions
#     the third time by using alias
from functions import add_oper, divideOperator

x, y = 10, 4
print(add_oper(5,10), divideOperator(x,y))

