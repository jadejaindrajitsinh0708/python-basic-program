D = [10,20,30,40,50,60]

def add_number(D):
    num = int(input("enter any number ::_"))
 
    D.append(num)
    print("number is add in list  ✅✅🆗 :")
   
    print(D)
# add_number(D)

indrajit = [10,20,30,40,50,60,70,80,90,100]

def remove(indrajit):
    num = input("enter remove  number :--")
    num= int(num)

    if num == " " :
        print("enter a  number v")
        pass
    
    if num in indrajit :
        indrajit.remove(num)
        print("number is remove 🆗🆗😊")
    else :
        print("number is not found ")
    print(indrajit)
# remove(indrajit)

while True :
    print("  😎*****choose onliy one option *****😎 ")
    print("1. add number in list :-")
    print("2. remove number in this list:--")
    print("3. Exit...🔚")


    user = int(input("enter selected option : "))

    if user == 1:
        add_number(D)
    elif user == 2:
        remove(indrajit)
    elif user == 3:
        print("You are Exit.")
        break
    else:
         print("Invalid input")