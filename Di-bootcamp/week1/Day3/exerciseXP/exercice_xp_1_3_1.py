# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
# Step 1: Create Cat Objects
#     Use the Cat class to create three cat objects with different names and ages.
class cat():
    def __init__(self,cat_name,cat_age):
        self.name=cat_name
        self.age=cat_age

cat1 = cat("minou",2)
cat2 = cat("alpha",3)
cat3 = cat("grr",1)


# # Step 2: Create a Function to Find the Oldest Cat
# #     Create a function that takes the three cat objects as input.
# #     Inside the function, compare the ages of the cats to find the oldest one.
# #     Return the oldest cat object.
def find_oldest_cat(cat1,cat2,cat3):
    oldest = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    return oldest

oldest=find_oldest_cat(cat1, cat2, cat3)
print(type(oldest))
print(f"the oldest cat is {oldest.name}, and is {oldest.age} years old.")


# print("the odlest cat is {cat.cat_age}")
# Step 3: Print the Oldest Cat’s Details
#     Call the function to get the oldest cat.
#     Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
#     Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.


# Step 1: Create the Dog Class

#     Create a class called Dog.
class dog():
    def __init__(self,dog_name,dog_height):
        self.name=dog_name
        self.height=dog_height

#     In the __init__ method, take name and height as parameters and create corresponding attributes.
#     Create a bark() method that prints “ goes woof!”.
#     Create a jump() method that prints “ jumps cm high!”, where x is height * 2.

# Step 2: Create Dog Objects

#     Create davids_dog and sarahs_dog objects with their respective names and heights.

davids_dog=dog("Milou",4.3) 
sarahs_dog=dog("Pluto",7.1)  
 
# Step 3: Print Dog Details and Call Methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall")
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall")
def bark(dog):
    print(f"{dog.name} goes woof!")
def jump(dog):
    print(f"{dog.name} jumps {dog.height*2} cm high!")

bark(davids_dog)
jump(davids_dog)        
bark(sarahs_dog)
jump(sarahs_dog)
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}")
else:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}")

#     Print the name and height of each dog.
#     Call the bark() and jump() methods for each dog.
# Step 4: Compare Dog Sizes

# Instructions:
# Create a Song class with a method to print song lyrics line by line.
# Step 1: Create the Song Class
# ===============================================


#     Create a class called Song.
#     In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
#     Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
# Example:

# ====================================
class song:
    def __init__(self,lyrics):
        self.lyrics=lyrics

def sing_me_a_song(song):
    for line in song.lyrics:
        print(line)


stairway = song(["There’s a lady who's sure", 
"all that glitters is gold", "and she’s buying a stairway to heaven"])
sing_me_a_song(stairway)


# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
# Key Python Topics:
#     Classes and objects
#     Object instantiation
#     Methods
#     Lists
#     Dictionaries (for grouping)
#     String manipulation

# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
class Zoo:
    def __init__(self,zoo_name):
        self.name=zoo_name
        self.animals=[]
#  It takes a string parameter zoo_name, representing the name of the zoo.
#     Initialize an empty list called animals to keep track of animal names.

# 3. Add a method add_animal(new_animal):

#     This method adds a new animal to the animals list.
#     Do not add the animal if it is already in the list.

def add_animal(self,new_animal):
    if new_animal not in self.animals:
        self.animals.append(new_animal)
        print(f"{new_animal} has been added to the zoo.")
    else:
        print(f"{new_animal} is already in the zoo.")



# 4. Add a method get_animals():
def get_animals(self):
    print("Animals in the zoo:")
    for animal in self.animals:
        print(animal)
#     This method prints all animals currently in the zoo.

# 5. Add a method sell_animal(animal_sold):
def sell_animal(self,animal_sold):
    if animal_sold in self.animals:
        self.animals.remove(animal_sold)
        print(f"{animal_sold} will be sold.")
    else:
        print(f"{animal_sold} is not in the zoo.")
#     This method checks if a specified animal exists on the animals list and if so, remove from it.

# 6. Add a method sort_animals():

#     This method sorts the animals alphabetically.
#     It also groups them by the first letter of their name.
#     The result should be a dictionary where:
#         Each key is a letter.
#         Each value is a list of animals that start with that letter.
def sort_animals(self):
    sorted_animals=sorted(self.animals)
    grouped_animals={}
    for animal in sorted_animals:
        first_letter=animal[0]
        if first_letter not in grouped_animals:
            grouped_animals[first_letter]=[animal]
        else:
            grouped_animals[first_letter].append(animal)
    self.grouped_animals=grouped_animals
    print(self.grouped_animals)

# Example output:

# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }
Thoiry=Zoo("Thoiry")
Thoiry.add_animal("Giraffe")
Thoiry.add_animal("Bear")   
Thoiry.add_animal("Baboon")
Thoiry.add_animal("Lion")
Thoiry.add_animal("Zebra")
Thoiry.add_animal("Cat")
thoiry.add_animal("Cougar")



# 7. Add a method get_groups():

#     This method prints the grouped animals as created by sort_animals().

# Example output:

# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...


# Step 2: Create a Zoo Object

#     Create an instance of the Zoo class and pass a name for the zoo.


# Step 3: Call the Zoo Methods

#     Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.


# Example (No Internal Logic Provided)

# class Zoo:
#     def __init__(self, zoo_name):
#         pass

#     def add_animal(self, new_animal):
#         pass

#     def get_animals(self):
#         pass

#     def sell_animal(self, animal_sold):
#         pass

#     def sort_animals(self):
#         pass

#     def get_groups(self):
#         pass

# # Step 2: Create a Zoo instance
# brooklyn_safari = Zoo("Brooklyn Safari")

# # Step 3: Use the Zoo methods
# brooklyn_safari.add_animal("Giraffe")
# brooklyn_safari.add_animal("Bear")
# brooklyn_safari.add_animal("Baboon")
# brooklyn_safari.get_animals()
# brooklyn_safari.sell_animal("Bear")
# brooklyn_safari.get_animals()
# brooklyn_safari.sort_animals()
# brooklyn_safari.get_groups()


