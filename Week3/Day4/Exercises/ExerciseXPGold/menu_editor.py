from restaurant_menu import MenuManager

def load_manager():
    return MenuManager()

def show_user_menu():
    print("Menu:")
    print("1. Add item to menu")
    print("2. Remove item from menu")
    print("3. Show restaurant menu")
    print("4. Exit")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    manager.add_item(name, price)
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter name of item to remove: ")
    if manager.remove_item(name):
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def show_restaurant_menu():
    print("Restaurant Menu:")
    for item in manager.menu:
        print(f"{item['name']}: ${item['price']}")

manager = load_manager()

def main():
    while True:
        show_user_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_item_to_menu()
        elif choice == "2":
            remove_item_from_menu()
        elif choice == "3":
            show_restaurant_menu()
        elif choice == "4":
            manager.save_to_file()
            print("Menu saved. Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
main()