class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        new_item = {"name": name, "price": price, "spice_level": spice, "gluten_index": gluten}
        self.menu.append(new_item)
    
    def update_item(self, name, price, spice, gluten):
        new_item = {"name": name, "price": price, "spice_level": spice, "gluten_index": gluten}
        for index, value in enumerate(self.menu):
            if new_item["name"] == value["name"]:
                self.menu[index].update(new_item)

    def remove_item(self, name):
        removed = False
        for index, value in enumerate(self.menu):
            if name == value["name"]:
                self.menu.pop(index)
                print("Menu updated")
                removed = True
                break
        if removed == False:
            print("Item not found.")
        
menu = [
    {"name":"Soup","price": 10,"spice_level": "B","gluten_index" : False},
    {"name":"Hamburger","price": 15,"spice_level": "A","gluten_index" : True},
    {"name":"Salad","price": 18,"spice_level": "A","gluten_index" : False},
    {"name":"French Fries","price": 5,"spice_level": "C","gluten_index" : False},
    {"name":"Beef bourguignon","price": 25,"spice_level": "B","gluten_index" : True}
]

my_restaurant = MenuManager(menu)
my_restaurant.add_item("Beef", 500, "C", False)
print(f"{my_restaurant.menu}")
my_restaurant.update_item("Beef", 300, "B", False)
print(f"{my_restaurant.menu}")
my_restaurant.remove_item("Salad")
print(f"{my_restaurant.menu}")
my_restaurant.remove_item("Salad")
print(f"{my_restaurant.menu}")