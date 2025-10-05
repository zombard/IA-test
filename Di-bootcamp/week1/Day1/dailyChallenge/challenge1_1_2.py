
#     Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#     Display a little cake as seen below:

#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !
x=int(input("date: ")) #nombre de bougies
i=0
top_cake_end="        "
a=(11-x)//2    #nombre d'underscores avant les iii
b=11-x-a      #nombre d'underscores après les iii
i=0
while i in range(11):
    if i<a:
        top_cake_end=top_cake_end+"_"
    elif i<a+x:
        top_cake_end=top_cake_end+"i"
    else:
        top_cake_end=top_cake_end+"_"
    i+=1

print(top_cake_end)
print("       |:H:a:p:p:y:|")
print("     __|___________|__")
print("    |^^^^^^^^^^^^^^^^^|")
print("    |:B:i:r:t:h:d:a:y:|")
print("    |                 |")
print("    ~~~~~~~~~~~~~~~~~~~")

