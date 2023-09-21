from menu_item import MenuItem
from menu_manager import MenuManager
def show_user_menu():
    while True:
        choice = input("View an Item (V)\nAdd an Item (A)\nDelete an Item (D)\nUpdate an Item (U)\nShow the Menu (S)\nExit (E)")
        if choice == "V":
            item = input("Which item you want to view?(name)\n")
            manage = MenuManager()
            print(manage.get_by_name(item))
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    item = input("Which item you want to add?(name/price)\n")
    try:    
        item = item.split("/")
        new_item = MenuItem(item[0], int(item[1]))
        new_item.save()
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Item was added successfully")

def remove_item_from_menu():
    item = input("Which item you want to remove?(name)\n")
    try:
        new_item = MenuItem(item, 0)
        new_item.delete()
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Item was removed successfully")

def update_item_from_menu():
    old_item = input("Which item you want to change?(name/price)\n")
    new_item = input("And new paramethers(name/price)?\n")
    try:    
        old_item = old_item.split("/")
        new_item = new_item.split("/")
        item = MenuItem(old_item[0], int(old_item[1]))
        item.update(new_item[0],new_item[1])
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("item was updated successfully")

def show_restaurant_menu():
    manager = MenuManager()
    print(manager.all())

show_user_menu()