from Week_5.Day_4.menu_manager import MenuManager

def load_manager():
    manager = input("Enter manager name: ")
    print(f"Welcome {manager}")
    menu1 = MenuManager()
    show_user_menu(menu1)


def show_user_menu(menu):
    print("MENU")
    choice = input("(a) Add an item \n(d) Delete an item \n(v) View menu \n(x) Exit \n:")
    possible_choices = ['a','d','v','x']
    if choice.lower() in possible_choices:
        if choice.lower() == 'a':
            while True:
                category = input("Enter item category (starters, entres, deserts, drinks: ")
                item = input("Enter item name: ")
                price = input(f"Enter price for {item}: ")
                try:
                    menu.add_item(category=category.lower(), name=item.lower(), price=price.lower())
                except:
                    print("Error - spelling must be exact. Try again...")
                    continue
                c = input(f"You are adding {item} to {category} for NIS {price}. \nEnter 'c' to confirm, 'e' to edit, or 'x' to cancel: ")
                if c.lower() == 'c':
                    menu.save_to_file()
                    break
                elif c.lower() == 'e':
                    continue
                else:
                    break
        elif choice.lower() == 'd':
            while True:
                item = input("Enter item to delete: ")
                removed = menu.remove_item(name=item.lower())
                if not removed:
                    print(f"Error: {item} not found on menu. Check spelling and try again...")
                    continue
                else:
                    c = input(f"You are about to delete {item}. \nEnter 'c' to confirm, 'e' to edit, or 'x' to cancel: ")
                    if c.lower() == 'c':
                        menu.save_to_file()
                        break
                    elif c.lower() == 'e':
                        continue
                    else:
                        break
        elif choice.lower() == 'v':
            menu.display_menu()

        elif choice.lower() == 'x':
            print(f"Goodbye.")
    else:
        print("Invalid input. Goodbye.")


if __name__ == '__main__':
    load_manager()
