# Challenge 1
#     Ask the user for a number and a length.
#     Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

# user_number, user_length =input("entrez un nombre "),input("entrez une longueur de chaine ")
# user_number=int(user_number)
# user_length=int(user_length)

# list_to_print=[]
# for i in range(user_length):
#     list_to_print.append((i+1)*user_number)
#     i+=1
# print(list_to_print)

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate 
# consecutive letters removed.
# Examples
# user's word : "ppoeemm" ➞ "poem"
# user's word : "wiiiinnnnd" ➞ "wind"
# user's word : "ttiiitllleeee" ➞ "title"
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

str_user=input("entrez une chaine de caractères: ")
new_str=str_user[0]
i=0
while i < len(str_user)-1:
    if str_user[i+1]!= str_user[i] :
        new_str+= str_user[i+1]
    # print(f"position dans la chaine {str_user[i]} caractère suivant {str_user[i+1]} indice de boucle {i}")
    # print(new_str)
    i+=1
print(new_str)


    
    
   
   
