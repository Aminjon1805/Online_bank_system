import pywhatkit
from main import *

def menu():
    print("1 - create account        2 - show account      3 - forgot password    4 - add money\n"
          "5 - withdraw money        6 - send money        7 - Exit\n")

    while True:
        choice = input("Which action would you choose: ")

        if choice == "1":
            name = input("Write your name: ")
            surname = input("Write your surname: ")
            phone = input("Write your phone number with country code: ")
            password  = input("Set password for your account: ")

            my_account = UserAccount(name, surname, phone, password)
            save_info(my_account)
            print("\nYour Account Saved successfully!\n")

        if choice == "2":
            name_check = input("Write your name: ")
            for i in read_info():
                if i.name == name_check:
                    i.show_user_info()
            print("\n")


        if choice == "3":
            name_check = input("Write your saved name: ")
            phone_num_check = input("Write your saved phone number: ")
            for i in read_info():
                if i.name == name_check and i.phone == phone_num_check:
                    pywhatkit.sendwhatmsg_instantly(phone_num_check, f"You code: {i.my_password}")


        if choice == "4":
            name_check = input("Write your saved name: ")
            password_check = input("Write your saved password: ")
            amount_to_add = int(input("Write amount to add: "))

            users = read_info()  # Load all users
            user_found = False

            for user in users:
                if user.name == name_check and user.my_password == password_check:
                    user.add_money(amount_to_add)
                    user_found = True
                    break

            if user_found:
                with open("data.pkl", "wb") as file:
                    pickle.dump(users, file)
                print(f"\n{amount_to_add} added to {name_check}'s account successfully!\n")
            else:
                print("\nUser not found or incorrect password!\n")

        if choice == "5":
            name_check = input("Write your saved name: ")
            password_check = input("Write your saved password: ")
            amount_to_get = int(input("Write amount to withdraw: "))

            users = read_info()  # Load all users
            user_found = False

            for user in users:
                if user.name == name_check and user.my_password == password_check:
                    user.withdraw_money(amount_to_get)
                    user_found = True
                    break

            if user_found:
                with open("data.pkl", "wb") as file:
                    pickle.dump(users, file)
                print(f"\n{amount_to_get} withdrawed from {name_check}'s account successfully!\n")
            else:
                print("\nUser not found or incorrect password!\n")

        if choice == "6":
            name_from = input("Write your name: ")
            password_to_send = input("Write your password: ")
            name_to = input("To who you wanna send(name): ")
            amount_to_sent = int(input("Amount you wanna send: "))

            users = read_info()  # Load all users
            user_found = False

            for user_from in users:
                if user_from.name == name_from and user_from.my_password == password_to_send:
                    user_from.withdraw_money(amount_to_sent)
                    user_found = True
                    break
            for user_to in users:
                if user_to.name == name_to:
                    user_to.add_money(amount_to_sent)
                    user_found = True
                    break

            if user_found:
                with open("data.pkl", "wb") as file:
                    pickle.dump(users, file)
                print(f"\n{amount_to_sent} sent from {name_from}'s account to {name_to} successfully!\n")
            else:
                print("\nUser not found!\n")



        if choice == "7":
            print("Thanks, Goodbye!")
            break


menu()


