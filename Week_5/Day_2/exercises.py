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

class Account:
    def __init__(self, account_owner, balance):
        self.account_owner = account_owner
        self.balance = balance

        self.details_dict = {self.account_owner: self.balance}


class Owner(Account):
    def __init__(self, account_owner, balance, card_num, pw):
        super().__init__(account_owner, balance)
        self.card_num = card_num
        self.pw = pw
        # self.account_numbers.append([card_num])

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def withdraw(self):
        while True:
            amount = int(input("Enter amount you wish to withdraw: $"))
            if amount > self.balance:
                print(f"You do not have ${amount} in your account to withdraw. Try again.")
                continue
            elif amount < 0:
                print(f"You must enter a valid withdrawal amount. Try again.")
                continue
            else:
                self.balance -= amount
                print(f"Successful withdrawal of ${amount}. Your new balance is ${self.balance}")

            again = input("Enter 1 to make another withdrawal, or 2 to exit: ")
            if again == "1":
                continue
            else:
                break

    def deposit(self):
        while True:
            amount = int(input("Enter amount you wish to deposit: $"))
            if amount < 0:
                print(f"You must enter a valid deposit amount. Try again.")
                continue
            else:
                self.balance += amount
                print(f"Successful deposit of ${amount}. Your new balance is ${self.balance}")

            again = input("Enter 1 to make another deposit, or 2 to exit: ")
            if again == "1":
                continue
            else:
                break
    def choose_action(self):
        action = input("Enter 1 for withdrawal, 2 for deposit, 3 to get balance: ")
        if action == '1':
            self.withdraw()
        elif action == '2':
            self.deposit()
        elif action == '3':
            self.get_balance()
        else:
            print("Invalid entry. Goodbye.")

    def check_owner_info(self):
        in_card_num = int(input("Enter your card number: "))
        in_pword = input("Enter your password: ")
        trial = 1
        while trial < 3:
            if in_card_num == self.card_num and in_pword == self.pw:
                self.choose_action()
                break
            else:
                print("Card number or password incorrect.")
                trial += 1
                continue
        if trial == 3:
            print("Too many attempts. Your card has been destroyed.")
            self.card_num = None


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.owners = []

    def create_account(self, account_owner, balance, card_num, pw):
        if len(self.owners) < 10:
            owner = Owner(account_owner, balance, card_num, pw)
            self.owners.append(owner)
            return owner

        else:
            print(f"There are already 10 accounts in {self.bank_name} bank.")
            print("Please try again later.")

    def get_bank_balance(self):
        total_in_bank = 0
        for item in self.owners:
            total_in_bank += item.balance
        print(f"Total amount of money in bank: ${total_in_bank}")
        return total_in_bank



if __name__ == '__main__':
    bank = Bank("Huntington")
    mitch1 = bank.create_account("Mitch1",1000,123,'pw123')
    mitch2 = bank.create_account("Mitch2",999,456,'pw456')
    # mitch3 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch4 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch5 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch6 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch7 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch8 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch9 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch10 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch11 = bank.create_account("Mitch",1000,123,'pw123')
    # mitch10.check_owner_info()
    mitch1.deposit()
    bank.get_bank_balance()
