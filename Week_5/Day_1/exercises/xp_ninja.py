# class MenuManager:
#     def __init__(self):
#
#         self.menu = {}
#
#     def add_item(self, name, price, spice_level, has_gluten):
#         item = {
#             name: {
#                 'name': name,
#                 'price': price,
#                 'spice_level': spice_level,
#                 'has_gluten': has_gluten
#             }
#         }
#
#         self.menu.update(item)
#
#
#     def update_item(self, name, price, spice_level, has_gluten):
#         menu_items = []
#         for item in self.menu:
#             menu_items.append(item)
#         if name in menu_items:
#             self.menu[name] = {
#                     'name': name,
#                     'price': price,
#                     'spice_level': spice_level,
#                     'has_gluten': has_gluten
#                 }
#             return self.menu
#         else:
#             print(f"{name} is not on the menu.")
#             return self.menu
#
#
#     def delete_item(self, name):
#         try:
#             self.menu.pop(name)
#             return self.menu
#         except:
#             print(f"{name} is not on the menu.")
#             return self.menu
#
#
#
#
# if __name__ == '__main__':
#     menu1 = MenuManager()
#     menu1.add_item('burger', 40, 'A', True)
#     menu1.add_item('salad', 30, 'A', False)
#     print(menu1.menu)
#     menu1.update_item('burger', 60, 'B', True)
#     print(menu1.menu)
#     menu1.update_item('steak', 20, 'A', True)


class Farm:

    def __init__(self,name):
        self.name = name
        self.animal_dict = {}

    def add_animal(self, name, count=1):
        animal_list = []
        for key in self.animal_dict:
            animal_list.append(key)
        if name not in animal_list:
            item = {
                name: count
            }
            self.animal_dict.update(item)
            return self.animal_dict
        else:
            self.animal_dict[name] += count
            return self.animal_dict

    def display_animals(self):
        print(f"{self.name}'s Farm")
        keys = list(self.animal_dict.keys())
        values = list(self.animal_dict.values())
        for c,item in enumerate(self.animal_dict):
            if self.animal_dict[item]>1:
                keys[c] = keys[c]+"s"

        for c,item in enumerate(keys):
            print(f"{item}: {values[c]}")


    def get_animal_type(self):
        keys = list(self.animal_dict.keys())
        print(keys)
        return keys

    def get_short_info(self):
        keys = list(self.animal_dict.keys())
        for c,item in enumerate(self.animal_dict):
            keys[c] = keys[c]+"s"

        animal_string = ''
        for animal in keys:
            animal_string+=animal+', '

        print(f"{self.name}'s Farm has {animal_string[0:len(animal_string)-2]}.")





if __name__ == '__main__':
    farm1 = Farm("McDonald")
    farm1.add_animal('pig')
    farm1.add_animal('cow',3)
    farm1.add_animal('cow',2)
    farm1.add_animal('hen',2)
    farm1.add_animal('chicken',20)
    farm1.add_animal('goat',6)
    farm1.display_animals()
    farm1.get_animal_type()
    farm1.get_short_info()

