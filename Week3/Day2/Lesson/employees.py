class Employee :

    @classmethod
    def create_best_employee(cls, salary):
        if salary > 30000:
            return cls("Kosta", "Green", 25, "developer", salary)
        else:
            print("Your salary too low")
        

    def __init__(self, firstname, lastname, age, job, salary, adress):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        self.__adress = adress

        @property
        def __adress (self) :
            return self.__adress
        
        @__adress.setter
        def adress(self, new_adress):
            if self.job == "developer":
                self.__adress = new_adress
    
    def get_fullname(self) :
        return f"{self.firstname} {self.lastname}"
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, new_promotion) :
        self.salary += new_promotion

    def show_info (self) :
        print(f"{self.get_fullname()} is {self.age} years old, his job is {self.job} and his salary is {self.salary}")
    
# new_emp = Employee.create_best_employee(34000)
# print(new_emp.__dict__)

# Program should be a function
# that contains a few lists
# list of names, of job, of salary ect...
# create a program that create 10 employees with random information
# and save them into a list
# then call the show_info method for each of them

# lst_names = ["John", "Lea", "Emma", "Josh", "Eli"]
# lst_lastnames = ["Cohen", "Smith", "Doe", "Sevi", "Swtazh"]
# lst_jobs = ["developer", "dancer", "cowboy", "tennis player", "doctor"]
# --> random age from 18 to 67
# --> random salary from 10000 to 45000

emp1 = Employee("Lea", "Doe", 25, "tenis player", 6000, "telaviv")
emp2 = Employee("John", "Snow", 20, "developer",25000, "rishon")
print(emp1.adress)
print(emp2.adress)

emp1.adress = "raanana"
emp2.adress = "raanana"

print(emp1.adress)
print(emp2.adress)