# class Pet:
#     def __init__(self, species, name, color):
#         self.species = species
#         self.name = name
#         self.color = color
#
#     def eat(self):
#         print("eating mice")
#     def sleep(self):
#         print("18 hrs / day")
#     def talk(self):
#         print(f"MEOW! My name is {self.name}")


# class House:
#     def __init__(self, address, num_rooms, paint_color):
#         self.address = address
#         self.num_rooms = num_rooms
#         self.paint_color = paint_color


class House:
    def __init__(self, city, num_rooms, landlord):
        self.city = city
        self.num_rooms = num_rooms
        self.landlord = landlord

        self.rent = 1000 * self.num_rooms
        # rent will be diff for every house that we create, based on the num of rooms
        if city == "TLV":
            self.rent *= 2


    def sign_contract(self, name, date):
        if self.landlord == "Moti":
            self.rent *= 2
        print(f"Rental agreement between {name} and {self.landlord} for NIS {self.rent} ")

    def complain_about_broken_window(self):
        print(f"{self.landlord} says 'Sorry, I can\'t help'")


myHouse = House("TLV", 2, "Eyal")
yourHouse = House("JLEM", 4, "Shlomo")
myHouse.rent = 4000
yourHouse.rent = 4000
myHouse.num_rooms = 2
yourHouse.num_rooms = 4
myHouse.sign_contract("Mitch", "today")
all_houses = [myHouse, yourHouse]

if myHouse.rent == yourHouse.rent:
    print("True")