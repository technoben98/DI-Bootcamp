import turtle

class Circle:
    
    PI = 3.14
    instances = 0
    
    def __init__(self,number, radius = 5):
        self.number = number
        self.radius = radius
        self.diameter = radius*2
        Circle.instances +1
        self.area = self.calculate_area()

    def __str__(self):
        return(f"Circle number: {self.number}. Circle radius = {self.radius}. Circle diameter = {self.diameter}. Circle area = {self.area}")

    def __add__(self,other):
        if isinstance(other, int):
            return self.radius + other
        elif isinstance(other, Circle):
            return self.radius + other.radius, self.diameter + other.diameter
        else:
            print("Wrong operation!")

    def __gt__(self, other):
        if self.area > other.area:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.area == other.area:
            return True
        else:
            return False
    
    def __lt__(self,other):
        if self.area < other.area:
            return True
        else:
            return False
        
    def calculate_area(self):
        return int(Circle.PI*(self.radius**2))
    

# Check Methods

circle1 = Circle(1,13)
circle2 = Circle(2,8)
circle3 = Circle(3,17)
circle4 = Circle(4,29)
circle5 = Circle(5,19)
circle6 = Circle(6,6)
print(circle1)
print(circle1 + circle2)
print(circle2<circle3)
print(circle2>circle3)
print(circle2==circle3)
circle_list = [circle1, circle2, circle3, circle4, circle5, circle6]
for circle in circle_list:
    print(circle)
circle_list.sort()
for circle in circle_list:
    print(circle)

# Turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
t.shape("circle")

for circle in circle_list:
    t.circle(circle.radius*5)

screen.exitonclick()