from models.Student import Student

class StudentRepository:
    Students = []
    def add_student(self, student):
        self.Students.append(student)
    def get_student(self, rollNo):
        return self.Students[0]
