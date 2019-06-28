from models.Student import Student
from repositories.student_repository import StudentRepository

class StudentService:
    studentRepository = StudentRepository()
    def new_student(self, name, rollNo, marks):
        student = Student(name, rollNo, marks)
        self.studentRepository.add_student(student)
    def read_student(self, rollNo):
        return self.studentRepository.get_student(rollNo)
        


