
# Using map and filter, 
# try to say hello to everyone who's name is less than or equal to 4 letters

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# salut=filter(lambda s: len(s)<=4, people)
# print(list(people))

# print(list(salut))

# salut=map(lambda s: f"hello +{s}", salut)

# print(list(salut))

class robot():
    def __init__(self, name, color, weight):

class person():
    def __init__(self, name, personality, isSitiing, robotOwned):

class Computer():   
    def __init__(self, name):

        """
        This is a totally useless function
        """
        print("I am a computer, my name is", self.name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")
