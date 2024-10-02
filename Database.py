'''Create a DB using dictionaries containing key as USN and related fields containing Name,gender, Marks1, Marks2 & Marks3 of students.
Implement the following functions to perform
i) Update Name/gender/marks
ii) search for usn and display the relevant fields
iii) delete based on search for name
iv)generate the report with avg marks more than 70%'''

class StudentDB:
    def __init__(self):
        self.db = {}

    def add_student(self, usn, name, gender, marks1, marks2, marks3):
       """Add a student to the database"""
       self.db[usn] = {'Name': name, 'Gender': gender, 'Marks1': marks1, 'Marks2': marks2, 'Marks3': marks3}
    def update_info(self, usn, field, new_value):
       if usn in self.db:
           if field in self.db[usn]:
               self.db[usn][field] = new_value
               print(field, "updated successfully for USN", usn)
           else:
               print(field, "is not a valid field.")
       else:
           print("Student with USN", usn, "not found.")
     #Search for a student by USN and display relevant fields
    def search_usn(self, usn):
        if usn in self.db:
           print("Student details:")
           for key, value in self.db[usn].items():
               print(key, ":", value)
        else:
           print("Student with USN", usn, "not found.")
    def delete_by_name(self, name): #Delete a student by name
       usn_to_delete = None
       for usn, student_info in self.db.items():
           if student_info['Name']==name:
               usn_to_delete=usn
               break
       if usn_to_delete:
               del self.db[usn_to_delete]
               print("Student with name", name, "deleted successfully.")
       else:
               print("Student with name", name, "not found.")
    def generate_report(self): #Generate report with average marks more than 70%"""
        print("Students with average marks more than 70%:")
        for usn, student_info in self.db.items():
            average_marks = (student_info['Marks1'] +student_info['Marks2'] +student_info['Marks3'])/ 3
            if average_marks > 70:
                print("USN:", usn, "Name:", student_info['Name'], "Average Marks:", average_marks)
def main():
    student_db = StudentDB()
    # Adding students
    student_db.add_student('1', 'Alice', 'Female', 80, 75, 85)
    student_db.add_student('2', 'Bob', 'Male', 70, 65, 75)
    student_db.add_student('3', 'Charlie', 'Male', 90, 85, 95)
    while True:
        print("\nMenu:")
        print("1. Update student information")
        print("2. Search by USN")
        print("3. Delete by name")
        print("4. Generate report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            usn = input("Enter USN of the student: ")
            field = input("Enter the field to update (Name/Gender/Marks1/Marks2/Marks3): ")
            new_value = input("Enter the new value: ")
            student_db.update_info(usn, field, new_value)
        elif choice == '2':
            usn = input("Enter USN to search: ")
            student_db.search_usn(usn)
        elif choice == '3':
            name = input("Enter name of the student to delete: ")
            student_db.delete_by_name(name)
        elif choice=='4':
            student_db.generate_report()
        elif choice=='5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__=="__main__":
    main()
