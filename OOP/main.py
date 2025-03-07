from datetime import datetime
# class Employee:
#     def __init__ (self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f"{first}.{last}@company.com"
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('Aldenir', 'Flauzino', 300)
# emp_2 = Employee('Lula', 'Silva', 1000)

# print(emp_1.fullname())
# print(emp_1.first)
# print(emp_2.fullname())
# print(emp_2.first)


# How many students do we have? = 15.
# I want to design a software for CCTB and we want to track record of progress of students.

 
# TrackRecord
# - Qualifications of the Students
# - Attendance
# - Grades of exams.

# Basic Data Types:
# - String
# - Int
# - Boolean
# - Float

# Classes which we define are also considered as Type or to be sore specifif Data Types.
# first_name, last_name
# fisrt student
# second
# third

class Qualification:
    def __init__(self, degree: str, institution: str, year:int):
        self.degree = degree
        self.institution = institution
        self.year = year

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.year})"
    
class Attendance:
    def __init__(self, is_present: bool, date: str):
      self.is_present = is_present
      self.date = date
    
    def __str__(self):
        return f"{'Present' if self.is_present else 'Absent'} on {self.date}"
    

class Grade:
    def __init__(self, exam_name:str, score:float):
        self.exam_name = exam_name
        self.score = score

    def __str__(self):
        return f"{self.exam_name}: {self.score}"

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = first_name
        self.qualifications = []
        self.grades = []
        self.attendance =  []

    def add_qualification(self, qualification: Qualification):
            self.qualifications.append(qualification)
    
    def add_grade(self, grade: Grade):
            self.grades.append(grade)
    
    def add_attendance(self, attendance: Attendance):
        self.attendance.append(attendance)

    def get_average_grade(self):
        if self.grades:
            return sum(grade.score for grade in self.grades) / len(self.grades)
        return 0.0

    def __str__(self):
        qualifications_str = ', '.join(str(q) for q in self.qualifications)
        grades_str = ', '.join(str(g) for g in self.grades)
        attendance_str = ', '.join(str(g) for g in self.attendance)
        return (f"Student: {self.first_name} {self.last_name}\n"
                f"Qualifications: {qualifications_str}\n"
                f"Attendance: {attendance_str}\n"
                f"Grades: {grades_str}\n"
                f"Average Grade: {self.get_average_grade()}")

# Example
qualification1 = Qualification("High School Diploma", "XYZ School", 2018)
qualification2 = Qualification("Bachelor's in Computer Science", "ABC University", 2022)
attendance1 = Attendance(True, '2025-02-25')
attendance2 = Attendance(True, '2025-02-27')

student1 = Student("John", "Doe")
student1.add_qualification(qualification1)

# Adicionar presenças com data
student1.add_attendance(attendance1)
student1.add_attendance(attendance2)

# Adicionar notas
student1.add_grade(Grade("Math Exam", 85.0))
student1.add_grade(Grade("Science Exam", 90.0))

print(student1)