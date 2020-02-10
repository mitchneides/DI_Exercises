# 1
#
# class Family:
#     def __init__(self, lastName):
#         self.lastName = lastName
#         self.members = []
#
#     def add_member(self,name,age,sex,is_child):
#         member_info = {
#             'name': name,
#             'last name': self.lastName,
#             'age': age,
#             'sex': sex,
#             'is child': is_child
#         }
#         return self.members.append(member_info)
#
#     def born(self,name,sex):
#         print(f"{name} was born to the {self.lastName} family!")
#         self.add_member(name,0,sex,True)
#
#     def display_family(self):
#         parents = []
#         kids = []
#         for dict in range(len(self.members)):
#             if self.members[dict]['is child'] == False:
#                 parents.append(self.members[dict]['name'])
#             else:
#                 kids.append(self.members[dict]['name'])
#
#         print()
#         print(f"Meet the {self.lastName} family!")
#         print()
#         print("Parents: ")
#         print(*parents)
#         print()
#         print("Kids: ")
#         print(*kids)
#         print()
#
#     def is_18(self,name):
#         for dict in range(len(self.members)):
#             if self.members[dict]['name'] == name:
#                 age = self.members[dict]['age']
#                 if age>=18:
#                     print(f"{name} is over 18 years old.")
#                     return True
#                 else:
#                     print(f"{name} is not over 18 years old.")
#                     return False
#
#
# # fam1 = Family("Bromson")
# # fam1.add_member("Scott",58,'male',False)
# # fam1.add_member("Kathy",56,'female',False)
# # fam1.add_member("Brett",27,'male',True)
# # fam1.add_member("Noah",25,'male',True)
# # fam1.born("McGaily","female")
# # fam1.display_family()
#
#
# 2
#
# class TheIncredibles(Family):
#
#     # def add_power(self,name,power):
#     #     for dict in range(len(self.members)):
#     #         if self.members[dict]['name'] == name:
#     #             self.members[dict]['power'] = power
#
#     def add_member(self,name,age,sex,is_child,heroName, power):
#         member_info = {
#             'name': name,
#             'last name': self.lastName,
#             'age': age,
#             'sex': sex,
#             'is child': is_child,
#             'hero name': heroName,
#             'super power': power
#         }
#         return self.members.append(member_info)
#
#     def born(self,name,sex,heroName,power):
#         print(f"{name} was born to the {self.lastName} family!")
#         self.add_member(name,0,sex,True,heroName,power)
#
#     def use_power(self,name):
#         for dict in self.members:
#             if dict['name'] == name:
#                 age = dict['age']
#                 power = dict['super power']
#
#         if age<18:
#             print(f"{name} is too young for this.")
#         else:
#             print(f"{name} is using {power} to fight evil.")
# #
# # fam = TheIncredibles('Incredibles')
# # fam.add_member("Bob",40,'male',False)
# # fam.add_power("Bob","Super-strength")
# # fam.display_family()
# # print(fam.members)
#
# fam = TheIncredibles('Parr')
# fam.add_member("Bob",40,'male',False,"Mr. Incredible","Super-strength")
# fam.add_member("Helen",39,'female',False,"Elastigirl","Stretchiness")
# fam.add_member("Violet",14,'female',True,"Violet","Force-fields")
# fam.add_member("Dash",10,'male',True,"Dash","Super-speed")
# fam.born("Jack-Jack",'male','Jack-Jack','shapeshifter')
# # fam.display_family()
# # print(fam.members)
# fam.use_power('Dash')

# 3


class BankAccount:
    def __init__(self, owner, balance, card_num=None, pw=None):
        self.owner = owner
        self.balance = balance
        self.card_num = card_num
        self.pw = pw
        self.allow_access = False

    def deposit(self, amount):
        while True:
            if amount > 0:
                self.balance += amount
                print(f"Your balance is now: ${self.balance}")


    def withdraw(self, amount):
        while True:
            if (self.balance - amount) < 0:
                print(f"You do not have ${amount} in your account to withdraw.")
            else:
                self.balance -= amount
                print(f"Your balance is now: ${self.balance}")


class Owner(BankAccount):

    def get_credit_card(self,num):
        self.card_num = num

    def get_pw(self,pw):
        self.pw = pw

    def check_owner_info(self):
        guess_num = 1
        while guess_num<3:
            card_number = int(input("Enter your credit card number: "))
            password = input("Enter your password: ")
            if (password == self.pw) and (card_number == self.card_num):
                self.allow_access = True
                WithdrawOrDeposit = int(input("Enter 1 for withdrawal, 2 for deposit: "))
                if WithdrawOrDeposit == 1:
                    amount = int(input("Enter the amount you wish to withdraw: "))
                    self.withdraw(amount)
                elif WithdrawOrDeposit == 2:
                    amount = int(input("Enter the amount you wish to deposit: "))
                    self.deposit(amount)
                else:
                    print("You did not enter a valid command. Goodbye")
                return
            else:
                print("Credentials incorrect.")
                guess_num += 1

        print("Too many attempts. Your card has been destroyed.")
        self.card_num = None


person = Owner("mitch",1000,123,'hello123')
person.check_owner_info()
