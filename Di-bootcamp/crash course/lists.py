my_list=[1, 2, 3, 4]
i=0
while i in range(len(my_list)):
    print(my_list[i])
    i=i+1
i=0
while i in range(len(my_list)):
    print(my_list[i]*20)
    i=i+1
i=0
my_list =["Elie", "Tim", "Matt"]
first_letter=[]
while i in range(len(my_list)):
    first_letter.extend(my_list[i][0])
    i=i+1
print(first_letter)

 #     Given two lists [1, 2, 3, 4] and [3, 4, 5, 6],
   #  return a new list that contains only the values present in both lists: [3, 4].
    
i=0
my_list =[1, 2, 3, 4, 5, 6]
new_list=[]
while i in range(len(my_list)):
    if my_list[i]%2==0:
        new_list.extend(str(my_list[i]))
    i=i+1
print(new_list)

list_1 =[1, 2, 3, 4]
list_2 =[3, 4, 5, 6]
print(list(set(list_1).intersection(set(list_2))))

#     Given a list of words , 
   # return a new list with each word reversed and in lowercase: 
   # ["eile", "mit", "ttam"].

my_list =["Elie", "Tim", "Matt"]
new_list=[]
i=0
while i in range(len(my_list)):
    lr=list(my_list[i])
    lr.reverse()
    lrc=""
    j=0
    while j in range(len(lr)):
         lrc=lrc+lr[j]
         j=j+1
    lrc=lrc.lower()
    print(lrc) 
    new_list.extend(lrc)
    i=i+1    
print(new_list)

   
  #     Given two strings "first" and "third", 
   # return a new list of the letters that are present 
   # in both strings: ["i", "r", "t"].
list1= "first" 
list2= "third" 
ll=list(set(list_1).intersection(set(list_2)))

   #     For all numbers between 1 and 100, 
   # return a list of the numbers that are divisible by 
   #     12: [12, 24, 36, 48, 60, 72, 84, 96].

  
   #     Given the string "amazing", return a list 
   # with all the vowels removed: ["m", "z", "n", "g"].
   #     Generate a list with the following value: 
   # [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
   #     Generate a list with the following structure:
