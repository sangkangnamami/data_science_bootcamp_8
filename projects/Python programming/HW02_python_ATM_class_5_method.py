## HW02 - class ATM at least 5 methods : balance, account name, account number, fn/deposit, withdraw, OTP request, authenthication, promptpay, qrcode

# intialize value

class ATM:
    def __init__(self, balance, account_name, account_num, currency): # attribute
        self.balance = balance
        self.account_name = account_name
        self.account_num = account_num
        self.currency = currency

    ## ATM function
    # 1) deposit function
    def deposit(self):
        print(f"Your balance is: {self.balance}")

        while True:
            try:
                deposit_amount = int(input("Your account ready for deposit. Please input the amount (0-9 only): "))
                print("We are counting your money, wait a momoent...")
                self.balance += deposit_amount
                print(f"Your total balance is: {self.balance}")
                print("Thank you very much. See you next time")

                while True:
                    deposit_slip = input("Do you want the slip? (Y/N only): ")
                    if deposit_slip == "Y" or deposit_slip == "y":
                        print("Please take your slip")
                        print("Thank you very much. See you next time")
                        return
                    elif deposit_slip == "N" or deposit_slip == "n":
                        print("Thank you very much. See you next time")
                        return
                    else:
                        print("Please type 'Y/N' only")

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

    # 2) withdraw function
    def withdraw(self):
        print(f"Your balance is: {self.balance} and this is your withdrawable amount")

        while True:
            try:
                withdraw_amount = int(input("Your account ready for withdraw. Please input the amount (0-9 only): "))

                if (0 < withdraw_amount <= self.balance):
                    print("We are preparing your money, wait a moment...")
                    self.balance -= withdraw_amount
                    print("Please take your money in the cashout channel below")
                    print(f"Your total balance is: {self.balance}")

                    while True:
                        withdraw_slip = input("Do you want the slip? (Y/N only): ")
                        if (withdraw_slip == "Y" or withdraw_slip == "y"):
                            print("Please take your slip")
                            print("Thank you very much. See you next time")
                            return
                        elif (withdraw_slip == "N" or withdraw_slip == "n"):
                            print("Thank you very much. See you next time")
                            return
                        else:
                            print("Please type 'Y/N' only")
                else:
                    print("Sorry, your account balance not enough for withdraw or withdraw = 0")
                    print("Please try again")

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

    # 3) withdraw_without_card function
    def withdraw_without_card(self):
        print(f"Your balance is: {self.balance} and this is your withdrawable amount")
        print("Please input the withdraw amount in your mobile")
        print("Please scan the qrcode here by your mobile phone")
        print("###############")
        print("##           ##")
        print("##   #####   ##")
        print("##   #####   ##")
        print("##   #####   ##")
        print("##           ##")
        print("###############")

        while True:
            scan_status = input("Tell us if you already scan (Y/N only): ")
            if (scan_status == "Y" or scan_status == "y"):
                print("We are preparing your money, wait a moment...")
                print("Please take your money in the cashout channel below")
                print(f"Your total balance is: {self.balance - 1000}") # assume: withdraw in mobile phone is 1000

                while True:
                    withdraw_slip = input("Do you want the slip? (Y/N only): ")
                    if (withdraw_slip == "Y" or withdraw_slip == "y"):
                        print("Please take your slip")
                        print("Thank you very much. See you next time")
                        return
                    elif (withdraw_slip == "N" or withdraw_slip == "n"):
                        print("Thank you very much. See you next time")
                        return
                    else:
                        print("Please type 'Y/N' only")

            elif (scan_status == "N" or scan_status == "n"):
                print("Your task is failed. Please try again")
                return

    # 4) transfer function
    def transfer(self):
        print(f"Your balance is: {self.balance} and this is your transferable amount")

        while True:
            transfer_acc_num = input("Plese input the account number for transfer (0-9 only, 10 digits): ")
            print("Loading...")

            if (transfer_acc_num.isdigit() and len(transfer_acc_num) == 10 and int(transfer_acc_num) != self.account_num):
                print("We are preparing your transaction, wait a moment...")
                print(f"Your destination account is {transfer_acc_num}")

                while True:
                    try:
                        transfer_amount = int(input("Your account ready for transfer. Please input the transfer amount (0-9 only): "))
                        if (0 < transfer_amount <= self.balance):
                            self.balance -= transfer_amount
                            print("We are processing your task, wait a moment...")
                            print("Done.")
                            print(f"Your total balance is: {self.balance}")

                            while True:
                                transfer_slip = input("Do you want the slip? (Y/N only): ")
                                if (transfer_slip == "Y" or transfer_slip == "y"):
                                    print("Please take your slip")
                                    print("Thank you very much. See you next time")
                                    return
                                elif (transfer_slip == "N" or transfer_slip == "n"):
                                    print("Thank you very much. See you next time")
                                    return
                                else:
                                    print("Please type 'Y/N' only")

                        else:
                            print("Sorry, your account balance not enough for withdraw or withdraw = 0")
                            print("Please try again")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

            else:
                print("Sorry, destination account number is wrong")
                print("Please try again")

    # 5) exchange function
    def exchange(self):
        foreign_currency = {
            "USD": 0.028,
            "CNY": 0.20,
            "YEN": 4.23,
            "EUR": 0.026,
            "GBP": 0.023
        }
        print(f"Your balance is: {self.balance} and this is your transferable amount")
        exchange_to = input(f"Which currency for exchange {foreign_currency}: ")
        print(f"Your select exchange is {exchange_to}")
        print(f"We are converting THB to {exchange_to}, wait a moment...")
        new_balance = self.balance * foreign_currency[exchange_to]
        print(f"You balance is {new_balance} with {exchange_to} currency")
        print("Thank you very much. See you next time")


# assume
account1 = ATM(50000, "Saranpol C.", 1234567890, "THB")
account2 = ATM(80000, "Chakadkarn S.", 9876543210, "THB")



# run this
account1.deposit()
account1.withdraw()
account1.withdraw_without_card()
accoun1.transfer()
account1.exchange()
