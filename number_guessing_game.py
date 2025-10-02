import random
random_number = random.randint(1, 100)
i=0
number_of_attempts=7
# def number_guessing_game():
for i in range(number_of_attempts):
    i=i+1
    if i==1:
        print("vous avez", number_of_attempts, "essais pour deviner un nombre entre 1 et 100")
        n=int(input("entrez un nombre: "))
        if n<random_number:
            print("too low")
        elif n>random_number:
            print("too high")
        else:
            print("congratulations ! you have guessed")
            break
    elif i==7:
        print("you have done the maximum number of attempts")
        print("the number was:", random_number)
        break
    else:
        n=int(input("faites une nouvelle tentative "))
        if n<random_number:
            print("too low")
        elif n>random_number:
            print("too high")
        else:
            print("congratulations ! you have guessed")
            break
print("the number was:", random_number)
