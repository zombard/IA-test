list=[("name", "Elie"), ("job", "Instructor")]
my_dic={} 

# create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} 
# (Note: The order does not matter).

# 2. Given two lists: ["CA", "NJ", "RI"] and
# ["California", "New Jersey", "Rhode Island"], 
# return a dictionary that looks like this: 
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

# 3. Create a dictionary where the keys are vowels in the alphabet 
# and the values are 0. 
# Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).


# 4. Create a dictionary where the key is the position of the letter in the alphabet, 
# and the value is the letter itself. You should return something like this:

animals_farm_list=["rabbit", "cat", "dog"]
for i, animal in enumerate(animals_farm_list):
    print(f"i : {i} ")
    animals_farm_list[i]=animal + "s"
print(animals_farm_list)
enum=enumerate(animals_farm_list)
print(enum)