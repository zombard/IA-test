# Exercise 1: Pets
# Key Python Topics:
#     Inheritance
#     Class instantiation
#     Lists
#     Polymorphism

# Instructions:
# Use the provided Pets and Cat classes to create a Siamese breed, 
# instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Step 1: Create the Siamese Class

#     Create a class called Siamese that inherits from the Cat class.
#     You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.

class siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Step 2: Create a List of Cat Instances
#     Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
#     Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
#     Give each cat a name and age.
all_cats = []
bengal_obj = Bengal("bengal", 3)
chartreux_obj = Chartreux("chartreux", 4)
siamese_obj = siamese("siamese", 5)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]


# Step 3: Create a Pets Instance
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

sarah_pets = Pets(all_cats)


#     Create an instance of the Pets class called sara_pets, 
# passing the all_cats list as an argument.


# Step 4: Take Cats for a Walk
#     Using the sara_pets instance, 
# walk the cats by calling the walk() method.
#     This should invoke the walk() method for each cat 
# in the all_cats list.
#     Example: sara_pets.walk()
sarah_pets.walk()
#     This should print:



#     Call the walk() method on the sara_pets instance.
#     This should print the result of calling the walk() method on each cat in the list.


# Example:
class Pets():
    def __init__(self, animals):
       self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):

        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#     Step 1: Create the Siamese class

#     Step 2: Create a list of cat instances

#     Step 3: Create a Pets instance of the list of cat instances

sara_pets = Pets(all_cats)

#     Step 4: Take cats for a walk

sara_pets.walk()


# 🌟 Exercise 2: Dogs

# Goal: Create a Dog class with methods for barking, running speed, and fighting.


# Key Python Topics:

#     Classes and objects
#     Methods
#     Attributes


# Instructions:

# Step 1: Create the Dog Class

#     Create a class called Dog with name, age, and weight attributes.
#     Implement a bark() method that returns “ is barking”.
#     Implement a run_speed() method that returns weight / age * 10.
#     Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.


# Step 2: Create Dog Instances

#     Create three instances of the Dog class with different names, ages, and weights.


# Step 3: Test Dog Methods

#     Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.


# Example (Conceptual, No Direct Solution):

class Dog():
    def __init__(self, name, age, weight):
#         # ... code to initialize attributes ...
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(self.name + " is barking")
#         # ... code to return bark message ...

    def run_speed(self):
        print(self.weight / self.age * 10)
#         # ... code to return run speed ...

    def fight(self, other_dog):
        print(f"{self.name} is fighting {other_dog.name}")
#         # ... code to determine and return winner ...

# # Step 2: Create dog instances
# #... your code here
dog1 = Dog("Buddy", 3, 20)
dog2 = Dog("Max", 4, 25)
dog3 = Dog("Rocky", 2, 15)


# # Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


# 🌟 Exercise 3: Dogs Domesticated

# Goal: Create a PetDog class that inherits from Dog and adds 
# training and tricks.


# Key Python Topics:

#     Inheritance
#     super() function
#     *args
#     Random module


# Instructions:

# Step 1: Import the Dog Class

#     In a new Python file, import the Dog class 
# from the previous exercise.


# Step 2: Create the PetDog Class
class petdog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(" all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            import random
            print(f"{self.name} {random.choice(tricks)}")
#     Create a class called PetDog that inherits from the Dog class.
#     Add a trained attribute to the __init__ method, with a default value of False.
#     trained means that the dog is trained to do some tricks.
#     Implement a train() method that prints the output of bark() and sets trained to True.
#     Implement a play(*args) method that prints “ all play together”.
#     *args on this method is a list of dog instances.
#     Implement a do_a_trick() method that prints a random trick if trained is True.
#     Use this list for the ramdom tricks:
#     tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#     Choose a rendom index from it each time the method is called.


# Step 3: Test PetDog Methods

#     Create instances of the PetDog class and test the train(), 
# play(*args), and do_a_trick() methods.


# Example:

# # In a new file
# # import the Dog class

# class PetDog(Dog):
#     def __init__(self, name, age, weight): <mark> no need to put the details in the function, you are giving the solution</mark>
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         print(self.bark())
#         self.trained = True

#     def play(self, *args):
#         # ... code to print play message ...

#     def do_a_trick(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         if self.trained:
#             tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#             print(f"{self.name} {random.choice(tricks)}")

# # Test PetDog methods
# my_dog = PetDog("Fido", 2, 10)
# my_dog.train()
# my_dog.play("Buddy", "Max")
# my_dog.do_a_trick()


# 🌟 Exercise 4: Family and Person Classes

# Goal:

# Practice working with classes and object interactions by modeling a family and its members.


# Key Python Topics:

#     Classes and objects
#     Instance methods
#     Object interaction
#     Lists and loops
#     Conditional statements (if/else)
#     String formatting (f-strings)


# Instructions:

# Step 1: Create the Person Class

#     Define a Person class with the following attributes:
#     first_name
#     age
#     last_name (string, should be initialized as an empty string)
#     Add a method called is_18():
#     It should return True if the person is 18 or older, otherwise False.


# Step 2: Create the Family Class

#     Define a Family class with:
#         A last_name attribute
#         A members list that will store Person objects (should be initialized as an empty list)


#     Add a method called born(first_name, age):
#         It should create a new Person object with the given first name and age.
#         It should assign the family’s last name to the person.
#         It should add this new person to the members list.


#     Add a method called check_majority(first_name):
#         It should search the members list for a person with that first_name.
#             If the person exists, call their is_18() method.
#         If the person is over 18, print:
#             "You are over 18, your parents Jane and John accept that you will go out with your friends"
#         Otherwise, print:
#             "Sorry, you are not allowed to go out with your friends."


#     Add a method called family_presentation():
#         It should print the family’s last name.
#         Then, it should print each family member’s first name and age.


# Expected Behavior:

# Once implemented, your program should allow you to:

#     Create a family with a last name.
#     Add members to the family using the born() method.
#     Use check_majority() to see if someone is allowed to go out.
#     Display family information with family_presentation().
