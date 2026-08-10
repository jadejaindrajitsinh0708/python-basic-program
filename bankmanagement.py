import numpy as np
import matplotlib.pyplot as plt



# Customer Class


class Customer:

    def __init__(self, acc_no, name, mobile, acc_type, balance):

        self.__acc_no = acc_no
        self.__name = name
        self.__mobile = mobile
        self.__acc_type = acc_type
        self.__opening_balance = balance
        self.__balance = balance

    # Display customer information
    def display(self):
    
  
        print("Account Number :", self.__acc_no)
        print("Customer Name  :", self.__name)
        print("Mobile Number  :", self.__mobile)
        print("Account Type   :", self.__acc_type)
        print("Opening Balance:", self.__opening_balance)
        print("Current Balance:", self.__balance)


    # Deposit money
    def deposit(self, amount):

        if amount > 0:
            self.__balance = self.__balance + amount
            print("Amount deposited successfully.")
            print("New Balance :", self.__balance)
        else:
            print("Amount must be greater than 0.")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > self.__balance:
            print("Insufficient balance.")

        else:
            self.__balance = self.__balance - amount
            print("Amount withdrawn successfully.")
            print("New Balance :", self.__balance)

    # Update customer information
    def update(self, name, mobile, acc_type):

        self.__name = name
        self.__mobile = mobile
        self.__acc_type = acc_type

        print("Customer information updated successfully.")

    # Get account number
    def get_account_number(self):

        return self.__acc_no

    # Get current balance
    def get_balance(self):

        return self.__balance



# Bank Class


class Bank:

    def __init__(self):

        self.customers = []

    # Create Account
    def create_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            # Check duplicate account number
            for customer in self.customers:

                if customer.get_account_number() == acc_no:
                    print("Account number already exists.")
                    return

            name = input("Enter Customer Name: ")

            mobile = input("Enter Mobile Number: ")

            if len(mobile) != 10:
                print("Mobile number must contain 10 digits.")
                return

            print("\nSelect Account Type")
            print("1. Savings")
            print("2. Current")

            choice = input("Enter choice: ")

            if choice == "1":
                acc_type = "Savings"

            elif choice == "2":
                acc_type = "Current"

            else:
                print("Invalid account type.")
                return

            balance = float(input("Enter Opening Balance: "))

            if balance < 0:
                print("Balance cannot be negative.")
                return

            customer = Customer(
                acc_no,
                name,
                mobile,
                acc_type,
                balance
            )

            self.customers.append(customer)

            print("\nAccount created successfully.")

        except ValueError:

            print("Please enter valid numeric values.")

    # Read / Display All Accounts
    def display_all_accounts(self):

        if len(self.customers) == 0:

            print("No accounts found.")

        else:

            for customer in self.customers:

                customer.display()

    # Search Account
    def search_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            for customer in self.customers:

                if customer.get_account_number() == acc_no:

                    customer.display()
                    return

            print("Account not found.")

        except ValueError:

            print("Invalid account number.")

    # Update Account
    def update_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            for customer in self.customers:

                if customer.get_account_number() == acc_no:

                    name = input("Enter New Name: ")
                    mobile = input("Enter New Mobile Number: ")

                    if len(mobile) != 10:
                        print("Mobile number must contain 10 digits.")
                        return

                    print("1. Savings")
                    print("2. Current")

                    choice = input("Enter Account Type: ")

                    if choice == "1":
                        acc_type = "Savings"

                    elif choice == "2":
                        acc_type = "Current"

                    else:
                        print("Invalid account type.")
                        return

                    customer.update(name, mobile, acc_type)

                    return

            print("Account not found.")

        except ValueError:

            print("Invalid input.")

    # Delete Account
    def delete_account(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            for customer in self.customers:

                if customer.get_account_number() == acc_no:

                    self.customers.remove(customer)

                    print("Account deleted successfully.")

                    return

            print("Account not found.")

        except ValueError:

            print("Invalid account number.")

    # Deposit
    def deposit_money(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            for customer in self.customers:

                if customer.get_account_number() == acc_no:

                    amount = float(input("Enter Deposit Amount: "))

                    customer.deposit(amount)

                    return

            print("Account not found.")

        except ValueError:

            print("Please enter a valid amount.")

    # Withdraw
    def withdraw_money(self):

        try:

            acc_no = int(input("Enter Account Number: "))

            for customer in self.customers:

                if customer.get_account_number() == acc_no:

                    amount = float(input("Enter Withdraw Amount: "))

                    customer.withdraw(amount)

                    return

            print("Account not found.")

        except ValueError:

            print("Please enter a valid amount.")

    # Balance Analysis using NumPy
    def balance_analysis(self):

        if len(self.customers) == 0:

            print("No accounts available.")

            return

        balances = []

        for customer in self.customers:

            balances.append(customer.get_balance())

        balance_array = np.array(balances)

        print("\n========== Balance Analysis ==========")

        print("Total Balance :", np.sum(balance_array))

        print("Average Balance :", np.mean(balance_array))

        print("Maximum Balance :", np.max(balance_array))

        print("Minimum Balance :", np.min(balance_array))

    # Graphical Report using Matplotlib
    def graphical_report(self):

        if len(self.customers) == 0:

            print("No accounts available.")

            return

        account_numbers = []
        balances = []

        for customer in self.customers:

            account_numbers.append(customer.get_account_number())
            balances.append(customer.get_balance())

        plt.bar(account_numbers, balances)

        plt.xlabel("Account Number")
        plt.ylabel("Current Balance")
        plt.title("Bank Account Balance Report")

        plt.show()


# ==========================================
# Main Program
# ==========================================

bank = Bank()


while True:

    print("\n")
    print("=" * 60)
    print("             BANK MANAGEMENT SYSTEM")
    print("=" * 60)

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

    print("=" * 60)

    choice = input("Enter your choice: ")

    if choice == "1":

        bank.create_account()

    elif choice == "2":

        bank.display_all_accounts()

    elif choice == "3":

        bank.search_account()

    elif choice == "4":

        bank.update_account()

    elif choice == "5":

        bank.delete_account()

    elif choice == "6":

        bank.deposit_money()

    elif choice == "7":

        bank.withdraw_money()

    elif choice == "8":

        bank.balance_analysis()

    elif choice == "9":

        bank.graphical_report()

    elif choice == "10":

        print("Thank you for using Bank Management System.")
        break

    else:

        print("Invalid choice. Please try again.")