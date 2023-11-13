"""design a student management system which allows class teacher to add students 
and their marks for every subject for 3 exams. Last option should be to see the 
total mark of given student. Choose the data structure according to the requirements"""
import json
class Student_exam_Portal():

    def __init__(self):
       self.students = {}

    def get_integer_input(self,prompt) :
        while True :
            try:
                student_data = int(input(prompt))
                return student_data
            except :
                print("enter a valid integer input")
    def get_string_input(self,prompt) :
        while True :
            
                student_data = input(prompt)
                if student_data.isnumeric():
                     print("enter a valid string input") 
                else :
                    return student_data
                  
    def save_file(self) :
       with open("data.json","w") as file :
           json.dump(self.students,file)
           file.close()
    def open_file(self):
        try:
            with open("data.json", "r") as file:
                student_data = json.load(file)
            return student_data
        except (json.decoder.JSONDecodeError, FileNotFoundError, TypeError):
            print("No data found or database is empty")
            return {}




    def add(self):
        while True:
            print("Exam term : command ---> 'first'")
            print("Exam term : command ---> 'second'")
            print("Exam term : command ---> 'third'")
            print("Exam term : command ---> 'q'- to exit to main")
            action = input("Enter 'q' to exit or any other key to continue: ").lower()
            if action == "q":
                break

            register_no = self.get_integer_input("Register number of student to enter the marks: ")
            exam_term = self.get_string_input("Which term marks need to be entered: ").lower()

            # Open the file to get existing data
            self.students = self.open_file()

            # Check if register_no and exam_term are in self.students
            if str(register_no) in self.students and exam_term in self.students[str(register_no)]:
                self.display_existing_data(str(register_no), exam_term)
            else:
                # If not in self.students, initialize both register_no and exam_term
                if str(register_no) not in self.students:
                    self.students[str(register_no)] = {}
                if exam_term not in self.students[str(register_no)]:
                    self.add_new_data(str(register_no), exam_term)


# ... (rest of the methods remain the same)

               
    def add_new_data(self,register_no,exam_term) :          
        # If not in self.students, initialize both register_no and exam_term
        if register_no not in self.students:
            self.students[register_no] = {}
        if exam_term not in self.students.get(register_no, {}):
            student_name = self.get_string_input("Student name: ")
            english = self.get_integer_input("Marks for English: ")
            maths = self.get_integer_input("Marks for Maths: ")
            science = self.get_integer_input("Marks for Science: ")

            student_data = {
                "Student_name": student_name,
                "Marks_for_English": english,
                "Marks_for_Maths": maths,
                "Marks_for_Science": science
            }
            self.students[str(register_no)][exam_term] = student_data
            self.save_file()
            print("Student data added successfully")
        else:
            print("Invalid exam term. Please enter 'first', 'second', 'third', or 'q' to exit.")
    def display_existing_data(self,register_no,exam_term):
        print("Data already present for the same register number and term")
        student = self.students.get(register_no, {}).get(exam_term, {})
        print("Student_name:", student.get("Student_name"))
        print("Marks_for_English:", student.get("Marks_for_English"))
        print("Marks_for_Maths:", student.get("Marks_for_Maths"))
        print("Marks_for_Science:", student.get("Marks_for_Science"))
        updates = self.get_string_input("Do you want to update student data(yes/no):").lower()
        if updates == "yes":
            student_name = self.get_string_input("Student name: ")
            english = self.get_integer_input("Marks for English: ")
            maths = self.get_integer_input("Marks for Maths: ")
            science = self.get_integer_input("Marks for Science: ")

            # Update the student's data within self.students
            self.students[register_no][exam_term]["Student_name"] = student_name
            self.students[register_no][exam_term]["Marks_for_English"] = english
            self.students[register_no][exam_term]["Marks_for_Maths"] = maths
            self.students[register_no][exam_term]["Marks_for_Science"] = science

            print("Student data has been updated successfully")
        self.save_file()


    def show(self):
        detail = input("Enter the student register no,to display the marks for term:")
        term = input("which exam term mark you need to view :")
        self.students = self.open_file()
        if self.students :
            if detail in self.students and term in self.students[detail] :
                student = self.students[detail][term]
                print("Student name :",student["Student_name"])
                print("Marks for English:",student["Marks_for_English"])
                print("Marks for Maths:",student["Marks_for_Maths"])
                print("Marks for Science:",student["Marks_for_Science"])
            else:
                print("no data found")    
        else:
            print("no data found, may be due to database is missing or empty, Please add data")
            self.students ={}
            return       
    def total(self):
        self.students= self.open_file()
        total_marks = input("Enter the register number of the student to view the total marks of all terms: ")
        if total_marks in self.students:
            student_data = self.students[total_marks]
            total_sum = 0
            for terms in ["first", "second", "third"]:
                if terms in student_data :
                    for term, subject_data in student_data.items():
                        value_list_term = []  # Initialize the list for each term
                        term_total = 0  # Initialize the term total for each term
                        for key, value in subject_data.items():
                            if key != "Student_name":
                                value_list_term.append(int(value))
                                term_total = sum(value_list_term)  # Calculate term total for each term
                else:
                    print("No data found for the {} term exam of student, {} ".format(terms,subject_data["Student_name"]))
                
    

            print("Total marks of {} for {} term is: {}".format(subject_data["Student_name"], term, term_total))
            total_sum += term_total  # Add term_total to the overall total_sum
            print("Total marks of student {} for all term exams with Register number {} is: {}".format(subject_data["Student_name"],total_marks, total_sum))
        else:
            print("Register number you entered not found")      
    def run(self):
        print("Welcome to the Student exam portal")
        while True:
            print("Use the below mentioned commands for smooth running of software")
            print("'ADD' - To add the student data including marks")
            print("'SHOW' - To display the exam marks for different terms")
            print("'TOTAL' - To display the total marks of the student of whole year")
            print("'q'- to exit")
            portal = input().lower()
            if portal == "add":
                self.add()
            elif portal == "show":
                self.show() 
            elif portal == "total" :
                self.total()       
            elif portal == "q":
                exit()


if __name__ == "__main__":
    exam = Student_exam_Portal()
    exam.run()




