# Exercise 1

# PI = 3.14
# class Circle:
#     def __init__(self, radius = 1.0):
#         self.radius = radius

#     def calculate_perimeter(self):
#         perimeter = 2 * PI * self.radius
#         return perimeter
    
#     def calculate_area(self):
#         area = PI * self.radius**2
#         return area

#     def print_definion(self):
#         print("A circle is a round-shaped figure that has no corners or edges. In geometry, a circle can be defined as a closed shape, two-dimensional shape, curved shape. A few things around us that are circular in shape are a car tire, a wall clock that tells time, and a lollipop.")

#     def get_info(self):
#         self.print_definion()
#         print(f"Circle radius: {self.radius}.\nCircle perimeter: {self.calculate_perimeter()}.\nCircle area: {self.calculate_area()}.")

# my_circle = Circle(3)
# my_circle.get_info()



# Exercise 2
import random

class MyList:
    def __init__(self, letters):
        self.letters = letters
    
    def reverse_list(self):
        self.sort_list().reverse()
        return self.letters
    
    def sort_list(self):
        self.letters.sort()
        return self.letters
    
    def new_list(self):
        new_list = [random.randint(0, 500) for x in self.letters]
        print(new_list)
    
list1 = ["b", 'a', 'd', 'x', 't']
first_list = MyList(list1)
print(first_list.reverse_list())
print(first_list.sort_list())
first_list.new_list()