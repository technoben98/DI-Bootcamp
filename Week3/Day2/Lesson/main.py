# Exercise 1

# class Door:
#     def __init__(self, is_opened):
#         self.is_opened = is_opened

#     def open_door(self):
#         is_opened = True
#         return is_opened

#     def close_door(self):
#         is_opened = False
#         return is_opened

# class BlockedDoor(Door):
#     def __init__(self, is_opened):
#         super().__init__(is_opened)

#     def open_door(self):
#         is_opened = False
#         print("Door is blocked, it's not way to open it.")
#     def close_door(self):
#         is_opened = False
#         print("Door is blocked, it's not way to close it.")

# door = BlockedDoor(False)
# door.open_door()
# door.close_door()

# Exercise 2

# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
# summary = 0
# index = 0
# while index != len(my_list):
#     try:
#         summary += my_list[index]
#         index += 1
#     except:
#         print(f"({my_list[index]}) Not a int!")
#         index+=1
#         continue
    
# print(summary)

# Exercise 3

# import operators

# print(operators.add_operator(5, 8))
# print(operators.divide_operator(5, 8))

# from operators import add_operator, divide_operator

# print(add_operator(5, 8))
# print(divide_operator(5, 8))

# import operators as calc

# print(calc.add_operator(5, 8))
# print(calc.divide_operator(5, 8))

# Exercise 4

# import employees as emp
# import random as rnd

# employyes_list = []
# def employyes():
#     names = ["John", "Lea", "Emma", "Josh", "Eli"]
#     lastnames = ["Cohen", "Smith", "Doe", "Sevi", "Swtazh"]
#     jobs = ["developer", "dancer", "cowboy", "tennis player", "doctor"]

#     for index in range(10):
#         employyes_list.append(emp.Employee(rnd.choice(names), rnd.choice(lastnames), rnd.randint(18, 67) , rnd.choice(jobs), rnd.randint(10000, 45000)))
    
#     for employee in employyes_list:
#         emp.Employee.show_info(employee)

# employyes()

# Exercise 5

import employees

class Developer(employees.Employee):
    def __init__(self, firstname, lastname, age, job = "developer", salary = 15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = []

    def add_skills(self, *skills):
        for skill in skills:
            self.coding_skills.append(skill)

    def coding(self):
        sentence = f"{self.get_fullname()} skils:"
        for skill in self.coding_skills:
            sentence += f" {skill}"
        sentence += "."
        return sentence
    
    def coding_with_partner(self, other_developer):
        text = f"{self.get_fullname()} and {other_developer.get_fullname()} coding together. \n{self.coding()} \n{other_developer.coding()}"
        print(text) 
    
    def get_promotion(self, coficient):
        salary = self.salary*coficient
        return salary

developer1 = Developer("Tom", "Cruiz", 30)
developer2 = Developer("Angelina", "Jolie", 23)
developer1.add_skills("Java", "MySQL")
developer2.add_skills("HTML+CSS", "JavaScript")
developer1.coding_with_partner(developer2)
print(developer1.get_promotion(1.3))