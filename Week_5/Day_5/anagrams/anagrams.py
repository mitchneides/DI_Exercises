from Week_5.Day_5.anagrams import anagram_checker

def load_anagram_checker():
    print("Welcome to Anagram Checker.")
    ana = anagram_checker.AnagramChecker()
    show_user_menu(ana)


def show_user_menu(anagram):
    while True:
        choice = input("\nEnter a word to check for anagrams, or 'x' to exit: ")
        choice = choice.strip().upper()
        if choice == 'X':
            print("Goodbye.")
            break
        else:
            if anagram.is_valid_word(choice):
                print(f"Anagrams for {choice}: {anagram.get_anagrams(choice)}")
            elif " " in choice:
                print(f"Only 1 word can be entered. Try again.")
                continue
            elif choice.isalpha() == False:
                print(f"Only letters can be entered. Try again.")
                continue
            else:
                print(f"{choice} is not a valid word. Check spelling and try again.")
                continue



if __name__ == '__main__':
    load_anagram_checker()