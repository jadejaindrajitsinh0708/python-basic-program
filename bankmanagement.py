import numpy as np
import matplotlib.pyplot as plt


print("="* 50)
print("Welcome To The Bank Management System")
print("="*50)


class Customer:

    def __init__(self, acc_no, name, mobile, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.mobile = mobile
        self.acc_type = acc_type
        self.balance = balance


    def display(self):
        print("--------------------")
        print("Account No :", self.acc_no)
        print("Name       :", self.name)
        print("Mobile     :", self.mobile)
        print("Type       :", self.acc_type)
        print("Balance    :", self.balance)



class Bank:

    def __init__(self):
        self.accounts = []



    def add_account(self, customer):
        self.accounts.append(customer)
        print("Account Created Successfully")


    def show_all(self):

        for c in self.accounts:
            c.display()



    def search(self, acc_no):

        for c in self.accounts:
            if c.acc_no == acc_no:
                return c

        return None



    def update(self):

        acc = int(input("Enter Account Number: "))

        customer = self.search(acc)

        if customer:

            customer.name = input("Enter New Name: ")

            print("Updated Successfully")

        else:
            print("Account Not Found")


    def delete(self):

        acc = int(input("Enter Account Number: "))

        customer = self.search(acc)

        if customer:

            self.accounts.remove(customer)

            print("Deleted Successfully")

        else:
            print("Account Not Found")


    def deposit(self):

        acc = int(input("Account Number: "))

        customer = self.search(acc)

        if customer:

            amount = int(input("Amount: "))

            customer.balance += amount

            print("Deposit Successful")


    
    def withdraw(self):

        acc = int(input("Account Number: "))

        customer = self.search(acc)

        if customer:

            amount = int(input("Amount: "))

            if amount <= customer.balance:

                customer.balance -= amount

                print("Withdraw Successful")

            else:
                print("Insufficient Balance")



    def report(self):

        names = []
        balances = []


        for c in self.accounts:

            names.append(c.name)
            balances.append(c.balance)


        data = np.array(balances)

        print("Total Balance :", np.sum(data))
        print("Average Balance :", np.mean(data))


        plt.bar(names, balances)

        plt.xlabel("Customer")
        plt.ylabel("Balance")

        plt.title("Bank Balance Report")

        plt.show()





bank = Bank()




bank.add_account(Customer(101,"Rahul","9876543210","Saving",25000))

bank.add_account(Customer(102,"Amit","9988776655","Current",40000))

bank.add_account(Customer(103,"Priya","9876501234","Saving",35000))

bank.add_account(Customer(104,"Neha","9123456789","Saving",18000))

bank.add_account(Customer(105,"Karan","9012345678","Current",50000))



while True:

    print("""
1. Create Account
2. View All Account
3. Update Account
4. Delete Account
5. Deposit
6. Withdraw
7. Report Graph
8. Exit
""")


    choice = input("Enter Choice: ")


    if choice == "1":

        acc = int(input("Account No: "))
        name = input("Name: ")
        mobile = input("Mobile: ")
        typ = input("Type: ")
        bal = int(input("Balance: "))

        bank.add_account(
            Customer(acc,name,mobile,typ,bal)
        )


    elif choice == "2":

        bank.show_all()


    elif choice == "3":

        bank.update()


    elif choice == "4":

        bank.delete()


    elif choice == "5":

        bank.deposit()


    elif choice == "6":

        bank.withdraw()


    elif choice == "7":

        bank.report()


    elif choice == "8":

        print("Thank You")

        break


    else:

        print("Invalid Choice")