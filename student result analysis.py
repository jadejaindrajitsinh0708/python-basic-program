import numpy as np
import matplotlib.pyplot as plt

class Student_Details:

    def __init__(self,roll, name,marks):
        self.roll = roll
        self.name = name
        self.__marks = marks

    def get_marks(self):

        print("Marks :", self.__marks)

    def set_marks(self, marks):
       self.__marks = marks
        
    def display(self):
        arr = np.array(self.__marks)
        total = arr.sum()
        avg = arr.mean()
        per = (total/(len(arr)*100))*100
        print("Student Roll No: ",self.roll)
        print("Student Name: ",self.name)
        print("Student Marks: ",self.__marks)
        print("Total Marks :", total)
        print("Percentage of Marks :", (round(per,2)))


class SMS:

    def __init__(self):
        self.students = [
            Student_Details(101,"indrajeet",[80,89,90]),
            Student_Details(102,"bhavya",[70,79,80])
        ]

    def add_student(self):
        while True:
            try:
                roll = int(input("Enter the student Roll No: "))

                if roll > 0:
                    for student in self.students:
                        if student.roll == roll:
                            print("Student already exists!")
                            break
                    else:
                        break
                else:
                    print("Student roll should be greater than 0!")
                    break
            except:
                print("Enter the valid student roll!")

        while True:
            try:
                name = input("Enter the student name: ").strip()

                if len(name)>=2 and len(name)<=50 and name.replace(" ","",2).isalpha():
                    break
                else:
                    print("Enter the valid student name!")

            except:
                print("Enter the valid student name!")

        marks = []
        subjects = ["python","AI","ML"]

        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"enter the marks of {subject} = "))

                    if mark>=0 and mark<=100:
                        marks.append(mark)
                        break
                    else:
                        print("enter the valid marks")

                except:
                    print("Enter the valid marks")

        student = Student_Details(roll,name,marks)
        self.students.append(student)
        print("Student added successfully.")

    def view_record(self):

        if len(self.students) != 0:
            for student in self.students:
                 if student.display():
                    break
            else:
                print("No student records found.")

            
            
    def search_record(self):
        if len(self.students)!= 0:
            while True:
                try:
                    roll = int(input("Enter the student Roll No to search: "))
                    for student in self.students:
                        if student.roll == roll:
                            student.display()
                            print("Student found.")
                            break
                    else:
                        print("Student not found.")
                        break
                    break
                except:
                    print("Enter a valid student roll no.")
        else:
            print("No student records found.")

    def update_record(self):
        while True:
            try:
                roll = int(input("Enter the student Roll No to update: "))

                if roll > 0:
                    for student in self.students:
                        if student.roll == roll:
                            break
                    else:
                        print("Student not found")
                        break

                    while True:
                                    
                        
                        print("1. Update Name of student")
                        print("2.Update Marks of student")
                        print("3.Exit")
                    
                        choice = input("Enter your choice: ")
                    
                        if choice == "1":
                    
                            while True:
                                try:
                                    name = input("Enter a new name:").strip()

                                    if len(name)>=2 and len(name)<=50 and name.replace(" ","",2).isalpha():
                                        student.name = name
                                        print("Name updated successfully.")
                                        break
                                    else:
                                        print("Enter the valid student name!")

                                except:
                                    print("Something went wrong!")

                        elif choice == "2":

                            while True:
                                try:
                                   
                                    print("1. Python")
                                    print("2. AI")
                                    print("3. ML")
                                    print("4. Exit")

                                    subject_choice = input("Enter your choice: ")

                                    if subject_choice == "1" :
                                        while True:
                                            try:
                                               mark = float(input("Enter marks of python: ")) 
                                               if mark>=0 and mark<=100:
                                                    student._Student_Details__marks[0] = mark
                                                    print("Marks updated successfully.")
                                                    break
                                            except:
                                                print("Enter the valid marks")
                                                
                                    elif subject_choice == "2":
                                        while True:
                                            try:
                                                mark = float(input("Enter marks of AI: ")) 
                                                if mark>=0 and mark<=100:
                                                    student._Student_Details__marks[1] = mark
                                                    print("Marks updated successfully.")
                                                    break
                                            except:
                                                print("Enter the valid marks")
                                                
                                    elif subject_choice == "3":
                                        while True:
                                            try:
                                                mark = float(input("Enter marks of ML: ")) 
                                                if mark>=0 and mark<=100:
                                                    student._Student_Details__marks[2] = mark
                                                    print("Marks updated successfully.")
                                                    break
                                            except:
                                                print("Enter the valid marks")
                                                
                                    elif subject_choice == "4":
                                        print("thank you for the update.")
                                        break
                                    
                                    else:
                                        print("Enter a valid subject choice!")
                                    
                                except:
                                    print("Something went wrong!")

                        elif choice == "3":
                            print("Update completed")
                            break

                        else:
                            print("Enter a valid choice!")
                    break
            except:
                print("Enter a valid choice!")
                
                
    def delete_record(self):
            if len(self.students) !=0:
                while True:
                    try:
                        roll = int(input("Enter the student Roll No to delete: "))
                        for student in self.students:
                            if student.roll == roll:
                                self.students.remove(student)
                                print("Student record deleted.")
                                break
                        else:
                            print("Student record not found.")
                    except:
                        print("Enter a valid student roll no.")
                    break
                
                
    def graph(self):
        roll = int(input("Enter the student Roll No to view graph: "))

        for student in self.students:
            if student.roll == roll:
                subjects = ["Python", "AI", "ML"]
                marks = student._Student_Details__marks

                while True:
                
                    print("1. Bar Graph")
                    print("2. Line Graph")
                    print("3. Pie Chart")
                    print("4. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        plt.bar(subjects, marks)
                        plt.title(student.name)
                        plt.xlabel("Subjects")
                        plt.ylabel("Marks")
                        plt.show()

                    elif choice == "2":
                        plt.plot(subjects, marks, marker="o")
                        plt.title(student.name)
                        plt.xlabel("Subjects")
                        plt.ylabel("Marks")
                        plt.yticks(np.arange(0, 101, 10))
                        plt.show()

                    elif choice == "3":
                        plt.pie(marks, labels=subjects, autopct="%1.1f%%")
                        plt.title(student.name)
                        plt.show()

                    elif choice == "4":
                        print("Exit")
                        break

                    else:
                        print("Enter a valid choice!")
                break
        else:
            print("Student not found.")

student = SMS()


while True:

    print("1. Add Student Record")
    print("2. View Student Record")
    print("3. Search Student Record")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Graphical Representation of Marks")
    print("7. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:
            student.add_student()

        elif choice == 2:
            student.view_record()

        elif choice == 3:
            student.search_record()

        elif choice == 4:
            student.update_record()

        elif choice == 5:
            student.delete_record()

        elif choice == 6:
            student.graph()

        elif choice == 7:
            print("Thank you for using the Student Management System.")
            break

        else:
            print("Enter a valid choice!")

    except:
        print("Invalid choice!")