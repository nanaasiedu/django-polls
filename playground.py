import math as m
from math import sin

"""
I am a multi line comment!
use this website for more examples: https://learnxinyminutes.com/docs/python/
"""

m.sqrt(4)  # 4.0
sin(4.0)


# List [1, 2, 3, 1]  Dictionary { 'a': 1 }   Set set(1, 2, 3)   Tuple  (1, 2, 3)

def make_list(n):
    return list(range(0, n))


def format_cities(letter: str, cities: [str]) -> str:
    # return "Key " + letter + " : value = " + str(cities)
    return f"Key = {letter} : value = {str(cities)}"


def add_cities(city_dict, new_cities):
    for city in new_cities:
        letter = city[0]
        city_dict.setdefault(letter, set())
        city_dict[letter] = city_dict[letter] | {city}


def print_cities_dict(cities_dict):
    for key, value in cities_dict.items():
        print(format_cities(key, value))


holland_cities_dict = {'a': {'amsterdam', 'amesfoort'}, 'b': {'breda'}, 'c': {'culemborg'}}
new_cities = ['ede', 'deventer', 'franeker', 'apeldoorn', 'ede']

print("BEFORE")
print_cities_dict(holland_cities_dict)

add_cities(holland_cities_dict, new_cities)

print("AFTER")
print_cities_dict(holland_cities_dict)

if not new_cities:  # means "if not empty". Also means if not false. Remember [] is seen as false in python
    print("I AM EMPTY!!!")

for (i, new_city) in enumerate(new_cities):
    print(f"{i} : {new_city}")

# Example 2
items = {'a': 1, 'x': 2}

search_item = "x"

# Linear Search
index = -1
for i, item in enumerate(items):
    if item == search_item:
        index = i
        break

print(index)

# Search in dict

print(search_item in items)  # True


# OOP Example

class Human:
    species = "Homosapien"

    def __init__(self, name, age=0, role="unemployed"):
        self.name = name
        self.age = age
        self.role = role

    def shout(self):
        print(f"My name is {self.name} and i am a {Human.species} working as a {self.role}")

    @staticmethod
    def grunt():
        return f"{Human.species.upper()} GRUNT!!! "


person1 = Human("Andrew", 24, "Developer")
person2 = Human("Sam", 35, "Developer")
person3 = Human("Sarah", 130, "Manager")

print(person1.name)
print(person1.shout())
print(person2.shout())
print(person3.grunt())
