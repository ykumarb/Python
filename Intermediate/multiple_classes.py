# Classes and Objects - Multiple Classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
    
    def getGrade(self):
        return self.grade
    
class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []
    
    def addStudent(self, student):
        if len(self.students) <  self.maxStudents:
            self.students.append(student)
            return True
        return False
    
    def getAverageGrade(self):
        total = 0
        for s in self.students:
            total += s.getGrade()
        return (total/len(self.students))
    
s1 = Student("Rock", 18, 100)
s2 = Student("John", 19, 99)
s3 = Student("Cena", 20, 97)

studentAdded = False

c1 = Course('Science', 2)
studentAdded = c1.addStudent(s1)
print(studentAdded)
studentAdded = c1.addStudent(s2)
print(studentAdded)
studentAdded = c1.addStudent(s3)
print(studentAdded)

avgGrade = c1.getAverageGrade()
print(avgGrade)