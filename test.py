print("hello world")
print("hey")

marks = float(input("enter your marks"))

def student(marks):
    
    if marks > 100 or marks < 0:
        print("INVALID MARKS! Please enter marks between 0 and 100.")

    elif marks > 91 :
        print(" GRADE : A1")
    elif marks == 91 :
        print("GRADE : A1 ")
    elif marks > 81 :
        print("GRADE : A2 " )
    elif marks == 81 :
        print("GRADE : A2 ")
    elif marks > 71 :
        print("GRADE : B1 ")
    elif marks == 71 :
        print("GRADE : B1 ")
    elif marks >61 :
        print("GRADE : B2 ")
    elif marks==61 :
        print("GRADE :B2 ")
    elif marks>51 :
        print("GRADE : C1 ")
    elif marks == 51 :
        print("GRADE :C1 ")
    elif marks> 41 :
        print("GRADE :C2 ")
    elif marks == 41 :
        print("GRADE :C2 ")
    elif marks>33:
        print("GRADE :  D")
    elif marks == 33 :
        print("GRADE :D ")
    else :
        print(" FAILL")




student(marks)

english = float(input("enter your english marks: "))
gujrati = float(input("enter your gujrati marks: "))
economics = float(input("enter your economics marks: "))
accountancy = float(input("enter your accountancy marks: "))
statistics = float(input("enter your statistics marks: "))
spcc = float(input("enter your spcc marks: "))
business_studies = float(input("enter your business studies marks: "))


total_marks = english + gujrati + economics + accountancy + statistics + spcc + business_studies
percentage = (total_marks / 700) * 100

print(f" (Total Marks): {total_marks}")
print(f" (Percentage): {percentage:.2f}%") 

if english >= 33 and gujrati >= 33 and economics >= 33 and accountancy >=33 and statistics >= 33 and spcc >= 33 and business_studies >= 33 :  
    print("you are passs")
else :
    print("faill")




number = int(input("enter any number"))

def num(number):
 if number > 1 :

    for i in range(2,number) :
        if number   %i == 0  :
            print("number is not prime")
            break
    else :
        print("number is prime")
 else :
    print("number is not prime")

num(number)









