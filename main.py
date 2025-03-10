import pickle

class UserAccount:
    def __init__(self, name: str, surname: str, phone: str, password: str, balance = 0):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.__password = password
        self.balance = balance

    @property
    def my_password(self):
        return self.__password

    def add_money(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print("Invalid Amount!")

    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid Amount!")

    def show_user_info(self):
        pass_to_get = input("Write your password: ")
        if pass_to_get == self.__password:
            print(f"  Name: {self.name}\n  Surname: {self.surname}\n  Phone: {self.phone}\n  Balance: {self.balance}")
        else:
            print("Invalid Password!")



data_list = []

def save_info(account):
    try:
        with open("data.pkl", "rb") as file:
            data_list = pickle.load(file)
    except (FileNotFoundError, EOFError):
        data_list = []

    data_list.append(account)
    with open("data.pkl", "wb") as file:
        pickle.dump(data_list, file)


def read_info():
    try:
        with open("data.pkl", "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

# import os
#
# if os.path.exists("data.pkl"):
#     os.remove("data.pkl")
#     print("Old data deleted!")
# else:
#     print("No old data found.")

