import json


class MenuManager:

    def __init__(self):
        with open('menu.json','r') as file:
            menu = json.load(file)
        self.menu = menu

    def add_item(self, category, name, price):
        self.menu[category][name] = price
        return self.menu

    def remove_item(self, name):
        removed = False
        for category in self.menu.keys():
            for item in self.menu[category]:
                if item == name:
                    del self.menu[category][item]
                    removed = True
                    return removed
        return removed

    def display_menu(self):
        for category in self.menu.keys():
            print(f"\n{category}:")
            for item in self.menu[category]:
                print(f"   {item} (NIS {self.menu[category][item]})")

    def save_to_file(self):
        with open("menu.json", "w") as file:
            json.dump(self.menu, file)


if __name__ == '__main__':

    menu = MenuManager()
    # print(menu.menu)
    # print(menu.remove_item('burger'))
    # print(menu.menu)
    # menu.save_to_file()
    # menu.add_item(category='entres', name='burger', price=60)
    # menu.save_to_file()
    menu.display_menu()
