from  models.Student import Student
from services.student_service import StudentService
name = input("Student Name: ")
rollNo = input("Roll No: ")
marks = input("Marks: ")

studentService = StudentService()
studentService.new_student(name, rollNo, marks)

s = studentService.read_student(100)
print(s.name)

