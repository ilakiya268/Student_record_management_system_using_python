MAX_STUDENTS = 30

class Student:
    def __init__(self):
        self.roll_no = ""
        self.name = ""
        self.Class = ""
        self.course = ""
        self.mobile_no = ""
        self.admission_year = ""

students = []  # List to store students' data

# Function to enter student data
def enter():
    ch = int(input("How many students do you want to enter? "))
    
    # Check if there is enough space to store new data
    if len(students) + ch <= MAX_STUDENTS:
        for i in range(ch):
            print(f"\nEnter the Data of student {i + 1}")
            s = Student()
            s.roll_no = input("Enter Roll NO: ")
            s.name = input("Enter Name: ")
            s.Class = input("Enter Class: ")
            s.course = input("Enter Course: ")
            s.mobile_no = input("Enter Mobile NO: ")
            s.admission_year = input("Enter Admission Year: ")
            students.append(s)  # Add the student to the list
    else:
        print("Not enough space to store data. Please reduce the number of students.")

# Function to show all student data
def show():
    if not students:
        print("No Data is Entered")
    else:
        for i, s in enumerate(students, 1):
            print(f"\nData of Student {i}")
            print("Roll NO:", s.roll_no)
            print("Name:", s.name)
            print("Class:", s.Class)
            print("Course:", s.course)
            print("Mobile NO:", s.mobile_no)
            print("Admission Year:", s.admission_year)

# Function to search for a student by roll number
def search():
    if not students:
        print("No data is entered")
    else:
        rollno = input("Enter the roll no of the student: ")
        found = False
        for s in students:
            if rollno == s.roll_no:
                print("Roll NO:", s.roll_no)
                print("Name:", s.name)
                print("Class:", s.Class)
                print("Course:", s.course)
                print("Mobile NO:", s.mobile_no)
                print("Admission Year:", s.admission_year)
                found = True
                break
        if not found:
            print(f"Student with Roll No {rollno} not found.")

# Function to update student data
def update():
    if not students:
        print("No data is entered")
    else:
        rollno = input("Enter the roll no of the student you want to update: ")
        found = False
        for s in students:
            if rollno == s.roll_no:
                print("\nPrevious data")
                print("Data of Student", s.roll_no)
                print("Roll NO:", s.roll_no)
                print("Name:", s.name)
                print("Class:", s.Class)
                print("Course:", s.course)
                print("Mobile NO:", s.mobile_no)
                print("Admission Year:", s.admission_year)
                print("\nEnter new data")
                s.roll_no = input("Enter Roll NO: ")
                s.name = input("Enter Name: ")
                s.Class = input("Enter Class: ")
                s.course = input("Enter Course: ")
                s.mobile_no = input("Enter Mobile NO: ")
                s.admission_year = input("Enter Admission Year: ")
                print("Data updated successfully.")
                found = True
                break
        if not found:
            print(f"Student with Roll No {rollno} not found.")

# Function to delete all student data
def delete():
    if not students:
        print("No data is entered yet")
    else:
        a = int(input("Are you Sure to Delete Data?\nPress 1 to delete all records: "))
        if a == 1:
            students.clear()
            print("All records are deleted..!!")
        else:
            print("Please Press 1 to Delete All Records")

if __name__ == "__main__":
    while True:
        print("\nPress 1 to Enter data")
        print("Press 2 to Show data")
        print("Press 3 to Search data")
        print("Press 4 to Update data")
        print("Press 5 to Delete data")
        print("Press 6 to Quit")
        value = int(input())
        if value == 1:
            enter()
        elif value == 2:
            show()
        elif value == 3:
            search()
        elif value == 4:
            update()
        elif value == 5:
            delete()
        elif value == 6:
            break
        else:
            print("Invalid input")
