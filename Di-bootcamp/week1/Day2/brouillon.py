
# Using map and filter, 
# try to say hello to everyone who's name is less than or equal to 4 letters

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
dict_user=map(lambda s: "hello "+s if len(s) <=4 else s, people)
# dict_user= map(lambda s: "Hello " + s if len(s) <= 4 else s, people)

print(list(dict_user))
