import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# STUDENT CLASS
# ==========================================================

class Student:

    # Constructor
    def __init__(self, student_id, name, marks):

        self.__student_id = student_id
        self.__name = name
        self.__marks = marks

        # Search result
        self.found = False


    # ======================================================
    # CHECK STUDENT ID
    # ======================================================

    def check_id(self, student_id):

        if self.__student_id == student_id:

            self.found = True

        else:

            self.found = False


    # ======================================================
    # DISPLAY STUDENT
    # ======================================================

    def display(self):

        print("-" * 55)

        print("Student ID   :", self.__student_id)
        print("Student Name :", self.__name)

        print("\nSubject Marks:")

        subject = 1

        for mark in self.__marks:

            print("Subject", subject, ":", mark)

            subject = subject + 1

        # Convert marks into NumPy array
        marks_array = np.array(self.__marks)

        # NumPy operations
        total = np.sum(marks_array)

        average = np.mean(marks_array)

        highest = np.max(marks_array)

        lowest = np.min(marks_array)

        percentage = (total / 500) * 100

        print("\nTotal Marks   :", total)

        print("Average Marks :", round(average, 2))

        print("Highest Marks :", highest)

        print("Lowest Marks  :", lowest)

        print("Percentage    :", round(percentage, 2), "%")


        # Grade condition
        if percentage >= 90:

            print("Grade         : A+")

        elif percentage >= 80:

            print("Grade         : A")

        elif percentage >= 70:

            print("Grade         : B")

        elif percentage >= 60:

            print("Grade         : C")

        elif percentage >= 50:

            print("Grade         : D")

        else:

            print("Grade         : Fail")

        print("-" * 55)


    # ======================================================
    # UPDATE NAME
    # ======================================================

    def update_name(self, new_name):

        self.__name = new_name


    # ======================================================
    # UPDATE MARKS
    # ======================================================

    def update_marks(self, new_marks):

        self.__marks = new_marks


    # ======================================================
    # GRAPH DATA
    # ======================================================

    def graph_data(self, names, averages):

        marks_array = np.array(self.__marks)

        average = np.mean(marks_array)

        names.append(self.__name)

        averages.append(average)


    # ======================================================
    # RESULT DATA
    # ======================================================

    def result_data(self, averages):

        marks_array = np.array(self.__marks)

        total = np.sum(marks_array)

        average = np.mean(marks_array)

        highest = np.max(marks_array)

        lowest = np.min(marks_array)

        percentage = (total / 500) * 100

        averages.append(average)

        print("\nStudent Name :", self.__name)

        print("Total Marks  :", total)

        print("Average      :", round(average, 2))

        print("Highest      :", highest)

        print("Lowest       :", lowest)

        print("Percentage   :", round(percentage, 2), "%")


# ==========================================================
# STUDENT MANAGEMENT CLASS
# ==========================================================

class StudentManagement:

    # Constructor
    def __init__(self):

        self.students = []


    # ======================================================
    # ADD STUDENT
    # ======================================================

    def add_student(self):

        print("\n========== ADD STUDENT ==========")

        # ----------------------------------------------
        # STUDENT ID
        # ----------------------------------------------

        id_valid = False

        while id_valid == False:

            try:

                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:

                    print(
                        "Student ID must be greater than 0."
                    )

                else:

                    id_valid = True

            except ValueError:

                print(
                    "Student ID must contain numbers only."
                )


        # ----------------------------------------------
        # DUPLICATE ID
        # ----------------------------------------------

        duplicate = False

        for student in self.students:

            student.check_id(student_id)

            if student.found == True:

                duplicate = True


        if duplicate == True:

            print("Student ID already exists.")


        else:

            # ------------------------------------------
            # STUDENT NAME
            # ------------------------------------------

            name_valid = False

            while name_valid == False:

                name = input(
                    "Enter Student Name: "
                )

                # Empty name
                if name.strip() == "":

                    print(
                        "Name cannot be empty."
                    )

                # Only alphabets and spaces
                elif name.replace(" ", "").isalpha():

                    name_valid = True

                else:

                    print(
                        "Name must contain only "
                        "alphabets and spaces."
                    )


            # ------------------------------------------
            # MARKS
            # ------------------------------------------

            marks = []

            for i in range(5):

                mark_valid = False

                while mark_valid == False:

                    try:

                        mark = float(
                            input(
                                "Enter marks of Subject "
                                + str(i + 1)
                                + ": "
                            )
                        )

                        if mark < 0:

                            print(
                                "Marks cannot be negative."
                            )

                        elif mark > 100:

                            print(
                                "Marks cannot be greater than 100."
                            )

                        else:

                            marks.append(mark)

                            mark_valid = True

                    except ValueError:

                        print(
                            "Marks must contain numbers only."
                        )


            # ------------------------------------------
            # CREATE OBJECT
            # ------------------------------------------

            student = Student(
                student_id,
                name,
                marks
            )

            # Add object into list
            self.students.append(student)

            print(
                "\nStudent added successfully!"
            )


    # ======================================================
    # VIEW STUDENTS
    # ======================================================

    def view_students(self):

        print("\n========== VIEW STUDENTS ==========")

        if len(self.students) == 0:

            print(
                "No student records available."
            )

        else:

            for student in self.students:

                student.display()


    # ======================================================
    # SEARCH STUDENT
    # ======================================================

    def search_student(self):

        print("\n========== SEARCH STUDENT ==========")

        try:

            student_id = int(
                input("Enter Student ID: ")
            )

            if student_id <= 0:

                print(
                    "Student ID must be greater than 0."
                )

            else:

                found = False

                for student in self.students:

                    student.check_id(student_id)

                    if student.found == True:

                        student.display()

                        found = True


                if found == True:

                    print(
                        "Student found successfully."
                    )

                else:

                    print(
                        "Student not found."
                    )

        except ValueError:

            print(
                "Please enter numbers only."
            )


    # ======================================================
    # UPDATE STUDENT
    # ======================================================

    def update_student(self):

        print("\n========== UPDATE STUDENT ==========")

        try:

            student_id = int(
                input("Enter Student ID: ")
            )

            if student_id <= 0:

                print(
                    "Student ID must be greater than 0."
                )

            else:

                found = False

                for student in self.students:

                    student.check_id(student_id)

                    if student.found == True:

                        found = True

                        print("\n1. Update Name")
                        print("2. Update Marks")

                        choice = input(
                            "Enter your choice: "
                        )


                        # --------------------------------
                        # UPDATE NAME
                        # --------------------------------

                        if choice == "1":

                            name_valid = False

                            while name_valid == False:

                                new_name = input(
                                    "Enter New Name: "
                                )

                                if new_name.strip() == "":

                                    print(
                                        "Name cannot be empty."
                                    )

                                elif new_name.replace(
                                    " ", ""
                                ).isalpha():

                                    name_valid = True

                                else:

                                    print(
                                        "Name must contain "
                                        "only alphabets and spaces."
                                    )


                            student.update_name(
                                new_name
                            )

                            print(
                                "Name updated successfully."
                            )


                        # --------------------------------
                        # UPDATE MARKS
                        # --------------------------------

                        elif choice == "2":

                            new_marks = []

                            for i in range(5):

                                mark_valid = False

                                while mark_valid == False:

                                    try:

                                        mark = float(
                                            input(
                                                "Enter marks of "
                                                "Subject "
                                                + str(i + 1)
                                                + ": "
                                            )
                                        )

                                        if mark < 0:

                                            print(
                                                "Marks cannot "
                                                "be negative."
                                            )

                                        elif mark > 100:

                                            print(
                                                "Marks cannot "
                                                "be greater than 100."
                                            )

                                        else:

                                            new_marks.append(
                                                mark
                                            )

                                            mark_valid = True

                                    except ValueError:

                                        print(
                                            "Please enter "
                                            "numbers only."
                                        )


                            student.update_marks(
                                new_marks
                            )

                            print(
                                "Marks updated successfully."
                            )


                        # --------------------------------
                        # INVALID UPDATE CHOICE
                        # --------------------------------

                        else:

                            print(
                                "Invalid choice."
                            )


                if found == False:

                    print(
                        "Student not found."
                    )

        except ValueError:

            print(
                "Please enter a valid Student ID."
            )


    # ======================================================
    # DELETE STUDENT
    # ======================================================

    def delete_student(self):

        print("\n========== DELETE STUDENT ==========")

        try:

            student_id = int(
                input("Enter Student ID: ")
            )

            if student_id <= 0:

                print(
                    "Student ID must be greater than 0."
                )

            else:

                found = False

                for student in self.students:

                    student.check_id(student_id)

                    if student.found == True:

                        found = True

                        print(
                            "Student found."
                        )

                        confirm = input(
                            "Delete this student? (yes/no): "
                        )

                        confirm = confirm.lower()


                        if confirm == "yes":

                            self.students.remove(
                                student
                            )

                            print(
                                "Student deleted successfully."
                            )


                        elif confirm == "no":

                            print(
                                "Delete operation cancelled."
                            )


                        else:

                            print(
                                "Please enter only yes or no."
                            )

                        break


                if found == False:

                    print(
                        "Student not found."
                    )

        except ValueError:

            print(
                "Please enter a valid Student ID."
            )


    # ======================================================
    # RESULT ANALYSIS
    # ======================================================

    def result_analysis(self):

        print(
            "\n========== RESULT ANALYSIS =========="
        )

        if len(self.students) == 0:

            print(
                "No student records available."
            )

        else:

            averages = []

            for student in self.students:

                student.result_data(
                    averages
                )


            # NumPy array
            average_array = np.array(
                averages
            )


            print(
                "\n========== OVERALL ANALYSIS =========="
            )

            print(
                "Highest Average :",
                round(
                    np.max(average_array),
                    2
                )
            )

            print(
                "Lowest Average  :",
                round(
                    np.min(average_array),
                    2
                )
            )

            print(
                "Overall Average :",
                round(
                    np.mean(average_array),
                    2
                )
            )


    # ======================================================
    # DISPLAY GRAPH
    # ======================================================

    def display_graph(self):

        print(
            "\n========== DISPLAY GRAPH =========="
        )

        if len(self.students) == 0:

            print(
                "No student records available."
            )

        else:

            names = []

            averages = []


            for student in self.students:

                student.graph_data(
                    names,
                    averages
                )


            plt.bar(
                names,
                averages
            )

            plt.title(
                "Student Average Marks"
            )

            plt.xlabel(
                "Student Name"
            )

            plt.ylabel(
                "Average Marks"
            )

            plt.xticks(
                rotation=30
            )

            plt.tight_layout()

            plt.show()


# ==========================================================
# MAIN FUNCTION
# ==========================================================

def main():

    management = StudentManagement()

    exit_program = False


    while exit_program == False:

        print("\n")
        print("=" * 55)

        print(
            "       STUDENT RESULT ANALYTICS SYSTEM"
        )

        print("=" * 55)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Result Analysis")
        print("7. Display Graph")
        print("8. Exit")

        print("=" * 55)


        choice = input(
            "Enter your choice: "
        )


        if choice == "1":

            management.add_student()


        elif choice == "2":

            management.view_students()


        elif choice == "3":

            management.search_student()


        elif choice == "4":

            management.update_student()


        elif choice == "5":

            management.delete_student()


        elif choice == "6":

            management.result_analysis()


        elif choice == "7":

            management.display_graph()


        elif choice == "8":

            print(
                "\nThank you for using "
                "Student Result Analytics System."
            )

            exit_program = True


        else:

            print(
                "Invalid choice! "
                "Please enter a number from 1 to 8."
            )


# ==========================================================
# START PROGRAM
# ==========================================================

main()