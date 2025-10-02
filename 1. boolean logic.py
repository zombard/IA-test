first="hello world" # This is a comment
print(first)
print("I AM A COMPUTER!")
if 1<2 and 4>2:
    print("Math is fun.")
nope=()
print(nope and 1)
print(len("What's my length?"))
print(str.upper("i am shouting"))
print(int("1000"))
print(int("1000")+1)
print(f"real" "4")
print(3 * "cool")
#print(bool(1/0))
print(bool([]))
name=input("what is your name ? ")
print(name)
number=int(input("give me a number: "))
if number<0:
    print("That number is less than 0!")
elif number>0:
    print("That number is greater than 0!") 
else:
    print("You picked 0!")
string=("apple")
for i in range(5):
    l=string[i]
    if l=="l":
        print(i+1)
str=("xylophone")
print(str[-1])
for i in range(len(str)):
    l=str[i]
    if l=="y":
        print("y is in xylophone")
my_string=input("donnez moi un mot:  ")
lower_string=my_string.lower()
if my_string is lower_string:
    print("votre chaine est tout en minuscules")
else:
    print("votre chaine n'est pas tout en minuscules")