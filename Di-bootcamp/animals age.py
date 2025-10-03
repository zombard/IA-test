
human_age=0

while int(human_age)<1 :
    human_age=input("depuis combien de temps (en années entères) avez vous les deux animaux ?")

human_age=int(human_age)
cat_age=0
dog_age=0
i=0

while i<human_age:
    i=i+1
    if i==1:
        cat_age=15
        dog_age=15
    elif i==2:
        cat_age=cat_age+9
        dog_age=dog_age+9
    else:
        cat_age=cat_age+4
        dog_age=dog_age+5

    
print(human_age,cat_age,dog_age)
#humanYears >= 1 and humanYears are whole numbers only

#Cat Years 15 cat years for first year +9 cat years for second year +4 
# at years for each year after that

#Dog Years 15 dog years for first year +9 dog years for second year 
# +5 dog years for each year after that