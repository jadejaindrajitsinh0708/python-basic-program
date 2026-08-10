import matplotlib.pyplot as mtp

s = [
    {
        "name": "Virendra",
        "account_number": "12345",
        "mobile_num": "9876543210",
        "type": "Saving",
        "city": "Jamnagar",
        "balance": 45850,
        "history": []
    },
    {
        "name": "Rahul",
        "account_number": "23456",
        "mobile_num": "9123456780",
        "type": "Current",
        "city": "Rajkot",
        "balance": 72600,
        "history": []
    },
    {
        "name": "Neha",
        "account_number": "34567",
        "mobile_num": "9012345678",
        "type": "Saving",
        "city": "Surat",
        "balance": 38450,
        "history": []
    },
    {
        "name": "Amit",
        "account_number": "45678",
        "mobile_num": "8765432109",
        "type": "Saving",
        "city": "Ahmedabad",
        "balance": 51200,
        "history": []
    },
    {
        "name": "Priya",
        "account_number": "56789",
        "mobile_num": "9988776655",
        "type": "Current",
        "city": "Vadodara",
        "balance": 89500,
        "history": []
    }
]


def create_account():
    name = input("customer name:- ")
    account = input("account number:- ")
    mobile = input("mobile number:- ")
    type = input("S/C:- ")
    city = input("city name:- ")
    balance = int(input("balance:- "))

    customer = {
        "name": name,
        "account_number": account,
        "mobile_num": mobile,
        "type": type,
        "city": city,
        "balance": balance,
        "history": []
    }

    s.append(customer)

    print("Account Create Succ...")
    for customer in s:
            print("----------------------")
            print("Name:", customer["name"])
            print("Account Number:", customer["account_number"])
            print("Mobile Number:", customer["mobile_num"])
            print("Account Type:", customer["type"])
            print("City:", customer["city"])
            print("Balance:", customer["balance"])


def show_all():
    for customer in s:
        print("----------------------")
        print("Name:", customer["name"])
        print("Account Number:", customer["account_number"])
        print("Mobile Number:", customer["mobile_num"])
        print("Account Type:", customer["type"])
        print("City:", customer["city"])
        print("Balance:", customer["balance"])


def search():
    name = input("Enter customer name:- ")

    for customer in s:
        if customer["name"] == name:
            print("----------------------")
            print("Name:", customer["name"])
            print("Account Number:", customer["account_number"])
            print("Mobile Number:", customer["mobile_num"])
            print("Account Type:", customer["type"])
            print("City:", customer["city"])
            print("Balance:", customer["balance"])
            return

    print("Customer Not Found")


def update():
    name = input("Enter customer name:- ")

    for customer in s:
        if customer["name"] == name:
            customer["mobile_num"] = input("New mobile number:- ")
            customer["city"] = input("New city:- ")
            print("Details Updated")
            return

    print("Customer Not Found")


def delete():
    name = input("Enter customer name:- ")

    for customer in s:
        if customer["name"] == name:
            s.remove(customer)
            print("Account Deleted")
            return

    print("Customer Not Found")


def deposit():
    name = input("Enter customer name:- ")
    amount = int(input("Enter amount:- "))

    for customer in s:
        if customer["name"] == name:
            customer["balance"] += amount
            customer["history"].append("Deposit " + str(amount))

            print("Money Added")
            print("Balance:", customer["balance"])
            return

    print("Customer Not Found")


def withdraw():
    name = input("Enter customer name:- ")
    amount = int(input("Enter amount:- "))

    for customer in s:
        if customer["name"] == name:

            if amount <= customer["balance"]:
                customer["balance"] -= amount
                customer["history"].append("Withdraw " + str(amount))

                print("Withdraw Successful")
                print("Balance:", customer["balance"])

            else:
                print("Insufficient Balance")

            return

    print("Customer Not Found")


def balance():
    name = input("Enter customer name:- ")

    for customer in s:
        if customer["name"] == name:
            print("Name:", customer["name"])
            print("Balance:", customer["balance"])
            return

    print("Customer Not Found")


def chart():
    name = []
    balance = []

    for customer in s:
        name.append(customer["name"])
        balance.append(customer["balance"])

    mtp.bar(name, balance)
    mtp.title("Customer Bank Balance")
    mtp.xlabel("Customer")
    mtp.ylabel("Balance")
    mtp.show()


def history():
    name = input("Enter customer name:- ")

    for customer in s:
        if customer["name"] == name:

            print("Transaction History")

            for data in customer["history"]:
                print(data)

            return

    print("Customer Not Found")


def summary():
    name = input("Enter customer name:- ")

    for customer in s:
        if customer["name"] == name:

            print("----------------------")
            print("Name:", customer["name"])
            print("Account Number:", customer["account_number"])
            print("Mobile Number:", customer["mobile_num"])
            print("Account Type:", customer["type"])
            print("City:", customer["city"])
            print("Balance:", customer["balance"])
            print("Transactions:", customer["history"])

            return

    print("Customer Not Found")


while True:

    print("\nBANK MANAGEMENT SYSTEM")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Search Account")
    print("4. Update Account")
    print("5. Delete Account")
    print("6. Deposit Money")
    print("7. Withdraw Money")
    print("8. Check Balance")
    print("9. Balance Chart")
    print("10. Transaction History")
    print("11. Account Summary")
    print("12. Exit")

    choice = input("Enter your choice:- ")

    if choice == "1":
        create_account()

    elif choice == "2":
        show_all()

    elif choice == "3":
        search()

    elif choice == "4":
        update()

    elif choice == "5":
        delete()

    elif choice == "6":
        deposit()

    elif choice == "7":
        withdraw()

    elif choice == "8":
        balance()

    elif choice == "9":
        chart()

    elif choice == "10":
        history()

    elif choice == "11":
        summary()

    elif choice == "12":
        print("Thank you")
        break

    else:
        print("Wrong choice")