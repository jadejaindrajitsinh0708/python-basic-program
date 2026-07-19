# 1
# 1.1
def add_number(num):
    num = input("enter number :-")
    if num.isdigit():
        num=float(num)

        if num ==0:
            print(" neutrul number ")
        elif num >=0:
            print("number is positive ")
        elif num <= 0:
            print("number is negitive ")
    else :
        print("invailid number")
# add_number(num)

# 1.2

def odd_number(num):
    num = input("enter number :-")
    if num.isdigit():
        num=int(num)

        if num == 0:
            print("numbner is neutural")

        elif num %2 ==0 :
            print("number is even ,num")
        else :
            print("number is odd")
    else:
        print("invailid number 🔄️")
# odd_number(num)

# 1.3
def lar_number():
    a= input("1.enter a number :")
    b= input("2.enter a number :")
    if a.isdigit():
        a=int(a)
    if b.isdigit():
        b=int(b)
        if a==b :
            print("Equal numbers")
    
        elif a>b :
            print("a,number is big")
        else :
            print("b,number is big")
    else:
        print("invailid number:")
# lar_number()



# 1.4
def three_number(a,b,c):
    
    a = input("enter first number :")
    b = input("enter second number :")
    c = input("enter third number :")

    if a.isdigit():
        a=int(a)
    if b.isdigit():
        b=int(b)
    if c.isdigit():
        c=int(c)
        if a ==b ==c :
            print(" equal number ")

        elif a >= b and a >= c :
            print("largest number is a")
        elif b >= a and b>=c :
            print("largest number is ,b")
        else :
            print("largest number is ,c ")

# three_number(a,b,c)

# 5. Check voting eligibility (age ≥ 18). 

def age_num(age):
    
    age = input("enter your age :-")
    if age.isdigit():
        age=float(age)
        if age >=18 :
            print("You are eligible for vote ✅")
        else :
            print("you are not eligible for vote ❌ ")
    else :
        print("Invalid input")

# age_num(age)

# 1.6

def year_number():
        year = input("Enter a year: ")
        if year.isdigit():
            year=int(year)

            if year % 4 == 0:
                print("Leap Year")
            else:
                print("Not a Leap Year")
        else :
            print("invalid input ")
            print("please try agen")
# year_number()

# 1.7



def student():
    marks = input("enter your marks")
    if marks.isdigit():
        marks=int(marks)

    
        if marks > 100 or marks < 0:
            print("INVALID MARKS! Please enter marks between 0 and 100.")

        elif marks > 91 :
            print("congratulation 🎉🎊 GRADE : A1")
        elif marks == 91 :
            print("congratulation 🎉🎊 GRADE : A1 ")
        elif marks > 81 :
            print("congratulation 🎉🎊 GRADE : A2 " )
        elif marks == 81 :
            print("congratulation 🎉🎊 GRADE : A2 ")
        elif marks > 71 :
            print("congratulation 🎉🎊 GRADE : B1 ")
        elif marks == 71 :
            print("congratulation 🎉🎊 GRADE : B1 ")
        elif marks >61 :
            print("congratulation 🎉🎊 GRADE : B2 ")
        elif marks==61 :
            print("congratulation 🎉🎊 GRADE :B2 ")
        elif marks>51 :
            print("congratulation 🎉🎊 GRADE : C1 ")
        elif marks == 51 :
            print("congratulation 🎉🎊 GRADE :C1 ")
        elif marks> 41 :
            print("congratulation 🎉🎊 GRADE :C2 ")
        elif marks == 41 :
            print("congratulation 🎉🎊 GRADE :C2 ")
        elif marks>33:
            print("congratulation 🎉🎊 GRADE :  D")
        elif marks == 33 :
            print("congratulation 🎉🎊 GRADE :D2 ")
        else :
           print(" FAILL")
    else :
        print("invalid input ")
# student()
# 1.8

def alphabet():
    ch = input("Enter an alphabet: ")

    if ch.isalpha():
            ch=str(ch)
            if ch =="a" or ch =="e" or ch=="i"or ch == "o" or ch =="u" or ch == "A" or ch == "E" or ch == "I" or ch=="O" or ch=="U" :
                print("It is a Vowel")
            else :
                print("It is a Consonant")
            
    else :
        print("invalid input ")
# alphabet()

# 1.9
def calculator():

    a= input("enter a first number :")
    b = input("enter second number :")
    if a.isdigit():
        a=int(a)
    if b.isdigit():
        b=int(b)
        
        op = input("Operation પસંદ કરો (+, -, *, /): ")

        if op=="+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a+b)
        else :
            print("INVALID INPUT ")
    else :
        print("INVALID NUMBER")

# calculator()
# 1.10
def divisible_number():
    num=int(input("enter any number :"))
    
    if num % 5 == 0 and num % 11 == 0:
            print("number is divisible")
            
    else:
            print("number is not divisible")
   
divisible_number()
