

class Human():
    def __init__(self, id_number:str, name:str, age:int, priority:bool, blood_type:str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def __str__(self):
        return f"{self.name}: \nId:{self.id_number}. Age:{self.age}. Priority: {self.priority}. Blood Type: {self.blood_type}."

class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
    
    def find_in_queue(self, person):
        for index, value in enumerate(self.humans):
            if value == person:
                return index
    
    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
        return self.humans

    def get_next(self):
        if len(self.humans) > 0:
            return self.humans[0]
        else:
            return None
    
    def get_next_blood_type(self, blood_type):
        if len(self.humans) > 0:
            for person in self.humans:
                if person.blood_type == blood_type:
                    return person
        else:
            return None
            
    def sort_by_age(self):
        sorted_list =[]
        for person in self.humans:
            if person.priority:
                sorted_list.append(person)
                # self.humans.remove(person)

        for index in range(1, len(self.humans)):
            temp_person = self.humans[index]
            j = index - 1
            while temp_person.age > self.humans[j].age and j >= 0:
                self.humans[j + 1] = self.humans[j]
                j -= 1
            self.humans[j + 1] = temp_person
        
        for person in self.humans:
            if person not in sorted_list:
                sorted_list.append(person) 
        self.humans = sorted_list

human1 = Human('FD3571', 'John', 18, True, 'AB')
human2 = Human('FD3572', 'May', 78, True, 'A')
human3 = Human('FD3573', 'Will', 98, False, 'B')
human4 = Human('FD3574', 'Ken', 26, False, 'A')
human5 = Human('FD3575', 'Ichi', 35, False, 'B')
human6 = Human('FD3576', 'Nike', 69, False, 'O')
human7 = Human('FD3577', 'Jack', 73, False, 'O')
human8 = Human('FD3578', 'Kate', 27, False, 'O')
human9 = Human('FD3579', 'Mary', 33, False, 'AB')
human10 = Human('FD3580', 'Jackie', 42, False, 'B')
human11 = Human('FD3581', 'Mark', 48, False, 'A')
human11 = Human('FD3582', 'Vano', 13, False, 'AB')
new_queue = Queue()
new_queue.add_person(human1)
new_queue.add_person(human2)
new_queue.add_person(human3)
new_queue.add_person(human4)
new_queue.add_person(human5)
new_queue.add_person(human6)
new_queue.add_person(human7)
new_queue.add_person(human8)
new_queue.add_person(human9)
new_queue.add_person(human10)
new_queue.add_person(human11)

# for i in new_queue.humans:
#     print(i)

print(new_queue.find_in_queue(human2))
print(new_queue.get_next())
print(new_queue.get_next_blood_type("B"))
new_queue.sort_by_age()
for i in new_queue.humans:
    print(i)