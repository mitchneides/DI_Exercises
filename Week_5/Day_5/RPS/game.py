def show_main_menu():
    # print("\nWelcome to RPS\n \nMenu:")
    user_choice = input("(g) Play a new game \n(x) Exit \n: ")
    return user_choice


def main():
    while True:
        choice = show_main_menu()
        if choice.lower() == 'x':
            break
        elif choice.lower() == 'g':
            pass #play game
        else:
            print("Invalid response. Try again:")
            continue

show_main_menu()