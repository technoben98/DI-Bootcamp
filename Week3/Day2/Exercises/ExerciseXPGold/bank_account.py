import sys

class BankAccount:
    def __init__(self, balance, username, password, authenticated = False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated
    
    def deposit(self,money):
        try:
            if self.authenticate == True:
                if money > 0:
                    balance = balance + money
                else:
                    raise ValueError
            else:
                raise Exception
        except ValueError:
            print("You cant to add negative number or zero to account!")
        except Exception:
            print("You have to authenticate!")

    def withdraw(self, money):
        try:
            if self.autauthenticated == True:
                if money > 0:
                    balance = balance - money
                else:
                    raise ValueError
            else:
                raise Exception
        except ValueError:
            print("You cant to add negative number or zero to account!")
        except Exception:
            print("You have to authenticate!")

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        return self.authenticate

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance = 0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, money):
        try:
            if self.minimum_balance >= money:
                return super().withdraw()
            else:
                raise Exception
        except Exception:
            print("Not enought money on your balance!")

class ATM:
    def __init__(self, account_list, try_limit):
        try:    
            account_list_true = True
            for i in account_list:
                if not isinstance(i, BankAccount) or not isinstance(i, MinimumBalanceAccount):
                    account_list_true == False
            if account_list_true == True:
                self.account_list = account_list
            else:
                raise Exception
        except Exception:
            print("Not right values.")
        
        try:
            if try_limit > 0:
                self.try_limit = try_limit
        except Exception:
            print("Invalid input!")

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Log In")
            print("2. Exit")
            choice = input("select an option: ")
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.log_in(username, password)
            elif choice == "2":
                sys.exit()

    def log_in(self, username, password):
        is_loggined = False
        while is_loggined == False:
            for account in self.account_list:
                account.authenticate(username, password)
                if account.authenticated:
                    is_loggined = True
                    try:
                        if is_loggined == True:
                            self.show_account_menu(account)
                        else:
                            raise Exception
                    except Exception:
                        print("Wrong username or password!")
                        self.current_tries += 1
                        username = input("Enter your username: ")
                        password = input("Enter your password: ")
                    if self.try_limit < self.current_tries:
                        print("You tried so much!")
                        sys.exit()

    def show_account_menu(self, account):
         while True:
            print(f"Account Menu ({account.username}):")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("select an option: ")
            if choice == "1":
                amount = int(input("Enter the deposit amount: "))
                account.deposit(amount)
                print(f"Deposit of {amount} successful. New balance: {account.balance}")
            elif choice == "2":
                amount = int(input("Enter the withdrawal amount: "))
                account.withdraw(amount)
                print(f"Withdrawal of {amount} successful. New balance: {account.balance}")
            elif choice == "3":
                sys.exit()

account1 = BankAccount(250000, "user1", "pass1")
account2 = BankAccount(450000, "user2", "pass2")
account_list = [account1, account2]

atm = ATM(account_list, 3)
atm.show_main_menu()