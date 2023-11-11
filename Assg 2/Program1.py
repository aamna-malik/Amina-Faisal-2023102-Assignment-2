class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Person class
person_instance = Person(name="John Doe", age=25)

# Printing out the person's details
print(f"Person's name: {person_instance.name}")
print(f"Person's age: {person_instance.age}")
