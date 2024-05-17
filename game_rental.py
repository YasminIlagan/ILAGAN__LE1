import os 

game_library = {
    "Donkey Kong" : {"Quantity" : 3, "Cost" : 2},
    "Super Mario Bros" : {"Quantity" : 5, "Cost" : 2},
    "Tetris" : {"Quantity" : 2, "Cost" : 1},
}

user_account ={"Yasmin" :{"password" : "Ilagan", "balance": 100000, "points": 100000}}

user_rented = {}

admin_username = "admin"
admin_password = "adminpass"

def display_available_games(username):
    print(f"Available Games: {game_library}")
    rentalmain(username)

def sign_up():
    while True:
        try:
            username = input("Enter New Username (leave blank to go back): ")
            balance = 0
            points = 0
            if not username:
                main()
            if username in user_account:
                print("This username is already taken. Please choose another one.")
                continue
            while True:
                try: 
                    password = input("Create Password (at least 8 characters): ")
                    if len(password) < 8:
                        print("Password should be at least 8 characters long.")
                        continue
                    if len(password) > 8:
                        user_account[username] = {"password" : password, "balance" : balance, "points" : points}  
                        print("Registration successful.")
                        main()
                    else:
                        print("Invalid input.")
                        continue 
                except ValueError as e:
                    print(e)
                    sign_up()
        except ValueError as e:
            print(e)
            sign_up()
    
def returnitem(username):
    print("Return Item")
    item_to_return = input("Enter the name of the item you want to return: ")
    quantity_of_item = int(input("Enter the quantity of item to return: "))
    game_library[item_to_return]['Quantity'] += quantity_of_item
    print(f"Successfully returned {item_to_return}, Quantity: {quantity_of_item}")
    rentalmain(username)

def sign_in():
    print("Sign In")
    while True:
        try:
            username = input("Enter username (leave blank to go back): ")
            if not username:
                main()
            password = input("Enter password: ")
            if user_account.get(username) and user_account[username]['password'] == password:
                print("Login Successful")
                rentalmain(username)
            else:
                print("Invalid username or password")
        except ValueError as e:
            print(e)
            main()

def rent(username):
    while True:
        try:
            print("Rent a game")
            print(game_library)

            gamename = input("Select Game (leave blank to go back): ")
            if not gamename:
                rentalmain(username)
            if game_library[gamename]['Quantity'] <= 0:
                print("Cannot Rent")
            if game_library[gamename]['Quantity'] >= 0:
                print("1. Pay using Balance")
                print("2. Pay using points: ")
                pay = int(input("Choose how to pay: "))

                if pay == 1:
                    if user_account[username]['balance'] <= 0:
                        print("Not enough balance to rent. Top up")
                        rent(username)
                    else:
                        user_account[username]['balance'] -= game_library[gamename]['Cost']
                        if game_library[gamename]['Cost'] >=2:
                            user_account[username]['points'] += 1
                            game_library[gamename]['Quantity'] -=1
                            print(f"Rented Successfully. User Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']} ")
                            user_rented[username] = {"Rented Game" : gamename}
                        else:
                            return
                if pay == 2:
                    if user_account[username]['points'] <= game_library[gamename]['Cost']:
                        print("Not enough points to rent.")
                        continue
                    else:
                        user_account[username]['points'] -= game_library[gamename]['Cost']
                        game_library[gamename]['Quantity'] -=1
                        print(f"Rented Successfully. User Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']} ")
                        return
                else:
                    return
        except ValueError as e:
            rentalmain(username)

def main():
    while True:
        try:
            print("Welcome to Game Rental Store")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Sign In as Administrator")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            while True:
                if choice == 1:
                    sign_up()
                if choice == 2:
                    sign_in()
                if choice == 3:
                    admin()
                else:
                    return
        except ValueError as e:
            print("")

def rentalmain(username):
    print(f"Welcome to Game Rental Store {username}")
    print("1. Rent")
    print("2. Return")
    print("3. Top-Up")
    print("4. Display Games")
    print("5. Check Points and Balance")
    print("6. Log Out")
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            rent(username)
        if choice == 2:
            returnitem(username)
        if choice == 3:
            top_up(username)
        if choice == 4:
            display_available_games(username)
        if choice == 5:
            checkpoints(username)
        if choice == 6:
            main()
        else:
            rentalmain(username)

def top_up(username):
    while True:
        try:
            print("Top Up")
            print(f"Username: {username}, Current Balance: {user_account[username]['balance']}")

            topup_amt = float(input("Enter amount to top up: "))
            user_account[username]['balance'] += topup_amt
            print("Top up Successful")
            print(f"Username: {username}, New Balance: {user_account[username]['balance']}")
            rentalmain(username)
        except ValueError as e:
            rentalmain(username)

def admin():
    print("Admin login")
    username = input("Enter username (leave blank to go back): ")
    if not username:
        main()
    if username == admin_username:
        password = input("Enter password: ")
        if password == "adminpass":
            print("Log In Successful")
            adminmenu()
        else:
            print("Invalid Password or Username.")
            admin()
    else: 
        print("Try Again")
        admin()


def checkpoints(username):
    print(f"Available Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']}")

def adminmenu():
    while True: 
        try:
            print("Welcome Admin")
            print("1. Add Quantity")
            print("2. Increase Price")
            print("3. Add Game")
            print("4. View Rent History")
            print("5. Sign out")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                admin_add_quantity()
            if choice == 2:
                increase_price()
            if choice == 3:
                add_game()
            if choice == 4:
                print(user_rented)
            if choice == 5:
                main()
            else:
                print("Invalid Input.")
        except ValueError as e:
            main()

def admin_add_quantity():
    while True: 
        try:    
            print(game_library)
            game_name = input("Enter the name of the item you want to add a quantity (leave blank to go back): ")
            quantity_of_item = int(input("Enter the quantity of the game: "))
            game_library[game_name]['Quantity'] += quantity_of_item


            if not game_name:
                adminmenu()
            else:
                print("Invalid Input. Try again")
                admin_add_quantity()

                print(f"Successfully added another {quantity_of_item} copies {game_name}. ")
                print(f"Updated Library: {game_library}")
                print("1. Add quantity to another game")
                print("2. Go back")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    admin_add_quantity()
                if choice == 2:
                    adminmenu()
                else:
                    print("Invalid Input")
        except ValueError as e:
            adminmenu()

def increase_price():
    while True: 
        try:
            print("Change Price")
            print(game_library)
            print("1. Increase the price")
            print("2. Decrease the price")

            choice = int(input("Enter your choice: "))

            if not choice:
                adminmenu()
            if choice == 1:
                game_name = input("Enter the name of the item you want to increase the price (type go back to return to menu): ")
                new_price = int(input("Enter the new price of the game: "))
                game_library[game_name]['cost'] = new_price
                print("Price changed successfully.")

                print("1. To change the price of another game.")
                print("2. Go back to main menu")
                choice = int(input("Enter your choice: "))

                if not game_name:
                    adminmenu()
                if not choice:
                    adminmenu()
                if choice == 1:
                    increase_price()
                if choice == 2:
                    adminmenu()
                else:
                    print("Invalid Input")
                    increase_price()
            if choice == 2:
                game_name = input("Enter the name of the item you want to decrease the price: ")
                new_price = int(input("Enter the new price of the game: "))
                game_library[game_name]['cost'] = new_price

                print("Price changed successfully.")
                print(f"Updated Library: {game_library}")
        
                print("1. To change the price of another game.")
                print("2. Go back to main menu")
                choice = int(input("Enter your choice: "))
        
                if not choice:
                    adminmenu()
                if not game_name:
                    adminmenu()
                if choice == 1:
                    increase_price()
                if choice == 2:
                    adminmenu
            else:
                print("Invalid Input.")
                increase_price()
        except ValueError as e:
            adminmenu()

def add_game():
    while True: 
        try:
            print("Add Game")
            print(game_library)
            new_game_name = input("Input the name of the game you want to add: ")
            new_game_quantity = int(input("Input the quantity of the new game: "))
            new_game_cost = int(input("Enter the price of the new game: "))

            game_library[new_game_name] = {"Quantity" : new_game_quantity, "Cost" : new_game_cost}

            print(f"{game_library[new_game_name]} Successfully Added to Library")

            print(f"Updated Library: {game_library}")

            choice = str(input("Would you like to add another game? (y/n): "))
 
            if choice == 'y':
                add_game()
            else:
                adminmenu()
        except ValueError as e:
            adminmenu()

main()