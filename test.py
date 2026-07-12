# print("hello world")
# print("hey")

# marks = float(input("enter your marks"))

# def student(marks):
    
#     if marks > 100 or marks < 0:
#         print("INVALID MARKS! Please enter marks between 0 and 100.")

#     elif marks > 91 :
#         print(" GRADE : A1")
#     elif marks == 91 :
#         print("GRADE : A1 ")
#     elif marks > 81 :
#         print("GRADE : A2 " )
#     elif marks == 81 :
#         print("GRADE : A2 ")
#     elif marks > 71 :
#         print("GRADE : B1 ")
#     elif marks == 71 :
#         print("GRADE : B1 ")
#     elif marks >61 :
#         print("GRADE : B2 ")
#     elif marks==61 :
#         print("GRADE :B2 ")
#     elif marks>51 :
#         print("GRADE : C1 ")
#     elif marks == 51 :
#         print("GRADE :C1 ")
#     elif marks> 41 :
#         print("GRADE :C2 ")
#     elif marks == 41 :
#         print("GRADE :C2 ")
#     elif marks>33:
#         print("GRADE :  D")
#     elif marks == 33 :
#         print("GRADE :D ")
#     else :
#         print(" FAILL")




# # student(marks)

# english = float(input("enter your english marks: "))
# gujrati = float(input("enter your gujrati marks: "))
# match = float(input("enter your matha marks"))
# scince = float(input("enter your scince marks"))
# hindi = float(input("enter your hindi marks"))
# social= float(input("enter your social marks"))

# economics = float(input("enter your economics marks: "))
# accountancy = float(input("enter your accountancy marks: "))
# statistics = float(input("enter your statistics marks: "))
# spcc = float(input("enter your spcc marks: "))
# business_studies = float(input("enter your business studies marks: "))


# total_marks = english + gujrati + match+ scince + hindi + social
# percentage = (total_marks / 600) * 100

# print(f" (Total Marks): {total_marks}")
# print(f" (Percentage): {percentage:.2f}%") 

# if english >= 26 and gujrati >= 26 and match >=26 and scince >=26 and hindi >=26 and social >=26 :
#     print("you are passs")
# else :
#     print("faill")




# number = int(input("enter any number"))

# def num(number):
#  if number > 1 :

#     for i in range(2,number) :
#         if number   %i == 0  :
#             print("number is not prime")
#             break
#     else :
#         print("number is prime")
#  else :
#     print("number is not prime")

# num(number)





# balance = 10000.0
# correct_pin = 1234


# while True:
#     print("\n--- ATM MENU ---")
#     print("1. Withdraw Money 💱 ")
#     print("2. Check Balance 🔄️")
#     print("3. Exit 🆗")
    
#     choice = input("Select an option (1-3): ")
    
#     if choice == "1":
#         pay = float(input("Enter amount to withdraw: "))
#         pin = int(input("Enter your PIN: "))
        
#         if pin == correct_pin:
#             if pay <= balance:
#                 balance = balance - pay  
#                 print("✅ Transaction successful!")
#                 print(f"Your new balance is: {balance}")
#             else:
#                 print("❌ Transaction failed: Insufficient balance!")
#         else:
#             print("❌ Transaction failed: Incorrect PIN!")
            
#     elif choice == "2":
#         print(f"💰 Your current balance is: {balance}")
        
#     elif choice == "3":
#         print("Thank you for using our service. Goodbye! 😊")
#         break  
        
#     else:
#         print("Invalid choice! Please select 1, 2, or 3.")







# num = 50

# for i in range(3):

#     guess = input("Guess the number between 1 to 100: ").strip()

#     if not guess.isdigit():
#         print("Enter only numbers")
#         continue

#     guess = int(guess)

#     if guess == num:
#         print("You Win")
#         break
#     elif guess < num:
#         print("Your guess is low")
#     else:
#         print("Your guess is high")

# num = 50

# num2 = 0
# while num2<3 :
#     guess = input("enter any number :-")
#     num2 =+1
#     if guess.isdigit():
#         guess=int(guess)  
#     else :
#         print("entre only digit")
#         continue

#     if guess == num :
#         print("cong...")
#         break
#     elif guess < num :
#         print("too high")
#     else :
#         print("too low")
# else :
#     print("game over")


my_list = [10,20,30,40,50,60]
def add_num(my_list):
    
    num = int(input("enter any number :--"))
    my_list.append(num)
    print(my_list)


    # add_num(my_list)
def remove_num(my_list):
  
 num = int(input("enter any number "))
if num == my_list :
        print("pass")
my_list.remove(num)

print(my_list)
    # remove_num(my_list)
while True:
    print("option 1. number add in this list :>>")
    print("option 2. remove number in this lost :>>")
    print("option 3. Exit you >...")
    if num :=input("enter your choose number :>>"):
        if num  =="1" :
            add_num(my_list)

        elif num == "2":
            remove_num(my_list)

        elif num =="3" :
            print("you EXIT .....")
            break

        else : 
            print("invalid this number" )
    # else:
    #     print("number is not difind")





























