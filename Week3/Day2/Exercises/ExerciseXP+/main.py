# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# 2. Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.
# ---------------------------------------------------------------------------------

# ANSWER

class Family:
    def __init__ (self, members, lastname):
        self.members = members
        self.lastname = lastname

    def born (self, **child):
        self.members.append(child)
        print("Congratulation!")

    def is_18 (self, name):
        for index, item in enumerate(self.members):
            if name == self.members[index]['name']:
                if self.members[index]['age'] >= 18:
                    self.members[index]['is_child'] = True
                    return True
                else:
                    self.members[index]['is_child'] = False
                    return False

    def family_presentation(self):
        sentence = f"Family {self.lastname} has:\n"
        for index, item in enumerate(self.members):
            for key in self.members[index]:
                if key == "name":
                    sentence = sentence + self.members[index][key] + "\n"
        return sentence
# members = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]

# family1 = Family(members, "Levi")
# family1.born(name='Petya', age=16, gender='Male', is_child=True)
# family1.born(name='Vasya', age=21, gender='Male', is_child=True)
# family1.born(name='Kosta', age=18, gender='Male', is_child=True)
# family1.born(name='Roma', age=14, gender='Male', is_child=True)

# print(family1.is_18("Sarah"))
# print(family1.is_18("Petya"))
# print(family1.is_18("Vasya"))
# print(family1.is_18("Kosta"))
# print(family1.is_18("Roma"))
# print(family1.members[5])
# print(family1.family_presentation())

# ---------------------------------------------------------------------------------
# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.
# ---------------------------------------------------------------------------------

# ANSWER

class TheIncredibles(Family):
    def __init__(self, members, lastname):
        super().__init__(members, lastname)

    
    def use_power(self):
        for member in self.members:
            age = member.get('age')
            if age is None or age < 18:
                raise Exception('You are not over 18 years old.')
            else:
                print(member['power'])

    def incredible_presentation(self):
        self.family_presentation()
        print(f'Incredible Names and Powers of "{self.lastname}" family:')
        for member in self.members:
            print(member['name'], '-', member['power'])

members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

awesome_family = TheIncredibles(members, "Gigachads")
awesome_family.use_power()
awesome_family.incredible_presentation()
awesome_family.born(name='Jack', age=5, gender='Male', is_child=True, power='Unknown Power')
awesome_family.incredible_presentation()