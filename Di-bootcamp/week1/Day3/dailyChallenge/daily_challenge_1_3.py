# Step 1: Create the Farm Class
#     Create a class called Farm.
#     This class will represent a farm and its animals.
# Step 2: Implement the __init__ Method
#     The Farm class should have an __init__ method.
#     It should take one parameter: farm_name.
#     Inside __init__, create two attributes: name to store the farm’s name 
# and animals to store the animals (initialize as an empty dictionary).

class farm():
    def __init__(self,farm_name):
        self.name=farm_name
        animals_of_the_farm={}
        self.animals=animals_of_the_farm
  
# Step 3: Implement the add_animal Method
#     Create a method called add_animal.
#     It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
#     The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
    def add_animals(self, animal_name, number_of_animals=1):
        if animal_name in self.animals:
            self.animals[animal_name]+=number_of_animals
        else:
            self.animals[animal_name]=number_of_animals


#     If count is not provided, it should default to 1.  
#     If the animal_type already exists in the animals dictionary, increment its count by count.
#     If it doesn’t exist, add it to the dictionary as the key and with the given count as value.


# Step 4: Implement the get_info Method

#     Create a method called get_info.
#     It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
#     Format the output to match the provided example.
#     Use string formatting to align the animal names and counts into columns.
    def get_info(self):
        info=f"{self.name} farm\n"
        for animal, count in self.animals.items():
            info+=f"{animal} : {count}\n"
        info+="E-I-E-I-0!"
        return info



# Step 5: Test Your Code

#     Create a Farm object and call the add_animal and get_info methods.
#     Verify that the output matches the provided example.


# Example:

# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...

#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...

#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...


# # Test the code 
macdonald = farm("McDonald")
macdonald.add_animals('cow', 5)
macdonald.add_animals('sheep')
macdonald.add_animals('sheep')
macdonald.add_animals('goat', 12)

print(macdonald.get_info())
# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!
