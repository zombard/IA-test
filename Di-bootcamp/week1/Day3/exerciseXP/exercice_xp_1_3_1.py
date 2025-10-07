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