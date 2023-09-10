class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = animals = {}

    def add_animal(self, name, qty = 1):
        if name not in self.animals:
            self.animals.update({name : qty})
        else:
            self.animals[name] += qty

    def get_info(self):
        print(f"{self.name}'s farm\n")
        for index, value in self.animals.items():
            print(f"{index} : {value}")
        print("\n    E-I-E-I-0!\n")

    def get_animal_types(self):
        types_list = []
        for index, value in self.animals.items():
            types_list.append(index)
        types_list.sort()
        return types_list

    def get_short_info(self):
        types = self.get_animal_types()
        print (f"McDonald's farm has {types[0]}s, {types[1]}s and {types[2]}s.")

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_animal_types())
macdonald.get_short_info()