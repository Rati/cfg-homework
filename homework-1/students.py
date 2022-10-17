"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.subject_details = []

    def show_student_details(self):
        print(f"Student Id : {self.id}")
        print(f"Student Name : {self.name}")
        print(f"Student Age : {self.age}")


class CFGStudent(Student):

    def __init__(self, id, name, age, specialization):
        super().__init__(id, name, age)
        self.specialization = specialization

    def add_subject(self, new_subject, new_marks):
        self.subject_details.append({'Name': new_subject, 'Marks': new_marks})
        print("Student subject details added successfully")

    def remove_subject(self, subject_to_remove):
        for subject in self.subject_details:
            if subject['Name'] == subject_to_remove:
                self.subject_details.remove(subject)
                print(f"subject details have been removed for student id {self.id}")

    def show_subjects(self):
        print(f"Subject details {self.subject_details}")

    def overall_marks(self):
        total_marks = 0
        for subject in self.subject_details:
            total_marks += subject["Marks"]
        avg_marks = total_marks/len(self.subject_details)
        print(f"Average marks = {avg_marks}")
        return avg_marks


student1 = CFGStudent(11, 'Emma', 24, 'Software')
student1.show_student_details()
student2 = CFGStudent(12, 'Kylie', 25, 'Data')
student2.show_student_details()
student1.add_subject('Python', 92)
student2.add_subject('Mysql', 94)
student1.add_subject('HTML', 85)
student2.add_subject('Bootstrap', 80)
student1.show_subjects()
student2.show_subjects()
student1.overall_marks()
student2.overall_marks()
student1.remove_subject('HTML')
student1.show_subjects()
