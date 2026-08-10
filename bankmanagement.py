import numpy as np
import matplotlib.pyplot as plt



class Customer:

    def __init__(self, acc_no, name, mobile, acc_type, balance):

        self.__acc_no = acc_no
        self.__name = name
        self.__mobile = mobile
        self.__acc_type = acc_type
        self.__balance = balance


   
    def display(self):

        print("-" * 50)

        print("Account Number  :", self.__acc_no)
        print("Customer Name   :", self.__name)
        print("Mobile Number   :", self.__mobile)
        print("Account Type    :", self.__acc_type)
        print("Current Balance :", self.__balance)

        print("-" * 50)



    def search(self, acc_no):

        if self.__acc_no == acc_no:

            print("-" * 50)

            print("Account Number  :", self.__acc_no)
            print("Customer Name   :", self.__name)
            print("Mobile Number   :", self.__mobile)
            print("Account Type    :", self.__acc_type)
            print("Current Balance :", self.__balance)

            print("-" * 50)



    def deposit(self, amount):

        if amount > 0:

            self.__balance = self.__balance + amount

            print("Money deposited successfully")
            print("Current Balance :", self.__balance)

        else:

            print("Amount must be greater than 0")


  

    def withdraw(self, amount):

        if amount <= 0:

            print("Amount must be greater than 0")

        elif amount > self.__balance:

            print("Insufficient Balance")

        else:

            self.__balance = self.__balance - amount

            print("Money withdrawn successfully")
            print("Current Balance :", self.__balance)




    def update(self, name, mobile, acc_type):

        self.__name = name
        self.__mobile = mobile
        self.__acc_type = acc_type

        print("Customer information updated successfully")



    def check_account(self, acc_no):

        if self.__acc_no == acc_no:

            print("Account Found")



    def store_balance(self, balances):

        balances.append(self.__balance)




    def store_account_number(self, account_numbers):

        account_numbers.append(self.__acc_no)


class Bank:

    def __init__(self):

        self.customers = []


    def create_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            name = input("Enter Customer Name: ")

            mobile = input("Enter Mobile Number: ")

            if len(mobile) != 10:

                print("Mobile Number must be 10 digits")

            else:

                print("\nSelect Account Type")

                print("1. Savings")
                print("2. Current")

                choice = input("Enter Choice: ")

                if choice == "1":

                    acc_type = "Savings"

                elif choice == "2":

                    acc_type = "Current"

                else:

                    acc_type = "Invalid"

                if acc_type == "Invalid":

                    print("Invalid Account Type")

                else:

                    balance = float(input("Enter Opening Balance: "))

                    if balance < 0:

                        print("Balance cannot be negative")

                    else:

                        customer = Customer(
                            acc_no,
                            name,
                            mobile,
                            acc_type,
                            balance
                        )

                        self.customers.append(customer)

                        print("Account Created Successfully")

        except ValueError:

            print("Please enter valid value")


    def display_all_accounts(self):

        if len(self.customers) == 0:

            print("No accounts available")

        else:

            for customer in self.customers:

                customer.display()




    def search_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            found = 0

            for customer in self.customers:

                if customer.get_account_number == acc_no:

                    customer.search(acc_no)

                    found = 1

            if found == 0:

                print("Account not found")

        except ValueError:

            print("Invalid Account Number")




    def update_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            found = 0

            for customer in self.customers:

                if customer.get_account_number == acc_no:

                    name = input("Enter New Name: ")

                    mobile = input("Enter New Mobile Number: ")

                    if len(mobile) == 10:

                        print("1. Savings")
                        print("2. Current")

                        choice = input("Enter Account Type: ")

                        if choice == "1":

                            acc_type = "Savings"

                        elif choice == "2":

                            acc_type = "Current"

                        else:

                            acc_type = "Invalid"

                        if acc_type != "Invalid":

                            customer.update(
                                name,
                                mobile,
                                acc_type
                            )

                            found = 1

                        else:

                            print("Invalid Account Type")

                    else:

                        print("Mobile Number must be 10 digits")

            if found == 0:

                print("Account not found")

        except ValueError:

            print("Invalid input")



    def delete_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            found = 0

            for customer in self.customers:

                if customer.get_account_number == acc_no:

                    self.customers.remove(customer)

                    print("Account deleted successfully")

                    found = 1

            if found == 0:

                print("Account not found")

        except ValueError:

            print("Invalid Account Number")
  
    
    def deposit_money(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            found = 0

            for customer in self.customers:

                if customer.get_account_number == acc_no:

                    amount = float(
                        input("Enter Deposit Amount: ")
                    )

                    customer.deposit(amount)

                    found = 1

            if found == 0:

                print("Account not found")

        except ValueError:

            print("Please enter valid amount")



    def withdraw_money(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            found = 0

            for customer in self.customers:

                if customer.get_account_number == acc_no:

                    amount = float(
                       input("Enter Withdraw Amount: ")
                    )
                    customer.withdraw(amount)
                    found = 1
            if found == 0:
                print("Account not found")
        except ValueError:
            print("Please enter valid amount")
    def balance_analysis(self):
        if len(self.customers) == 0:
            print("No accounts available")
        else:
            balances = []
            for customer in self.customers:
                customer.store_balance(balances)
            balance_array = np.array(balances)
            print("\n========== BALANCE ANALYSIS ==========")
            print("Total Balance   :", np.sum(balance_array))
            print("Average Balance :", np.mean(balance_array))
            print("Maximum Balance :", np.max(balance_array))
            print("Minimum Balance :", np.min(balance_array))
    def graphical_report(self):
        if len(self.customers) == 0:
            print("No accounts available")
        else:
            account_numbers = []
            balances = []
            for customer in self.customers:

                customer.store_account_number(
                    account_numbers
                )
                customer.store_balance(
                    balances
                )
            plt.bar(account_numbers, balances)
            plt.xlabel("Account Number")
            plt.ylabel("Current Balance")
            plt.title("Bank Account Balance Report")
            plt.show()
bank = Bank()

choice = 0
while choice != 10:
    print("\n")
    print("          BANK MANAGEMENT SYSTEM")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Search Account")
    print("4. Update Account")
    print("5. Delete Account")
    print("6. Deposit Money")
    print("7. Withdraw Money")
    print("8. Balance Analysis")
    print("9. Graphical Report")
    print("10. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            bank.create_account()
        elif choice == 2:
            bank.display_all_accounts()
        elif choice == 3:
            bank.search_account()
        elif choice == 4:
            bank.update_account()
        elif choice == 5:
            bank.delete_account()
        elif choice == 6:
            bank.deposit_money()
        elif choice == 7:
            bank.withdraw_money()
        elif choice == 8:
            bank.balance_analysis()
        elif choice == 9:
            bank.graphical_report()
        elif choice == 10:
            print("Thank you for using Bank Management System")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter number only")