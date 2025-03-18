import library
class Student:
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
   
    def student_details(self):
        return f'id [{self.student_id}] {self.name}'