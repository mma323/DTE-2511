class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def __str__(self):
        return (f"Name: {self.name } Address: {self.address} ")
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

class Student(Person):
    def __init__(self,studentId,name,address):
        super().__init__(name, address)                       # oppgave
        self.studentId = studentId
        self.myGrades = []

    def __str__(self):
        return (f"Student: Id :  {self.studentId }  - {super().__str__()}")       # oppgave
    
    def addCourseIdAndGrade(self, id, grade):                 # oppgave
        if (grade >= 'A' and grade <= 'F'):
            self.myGrades.append(CourseGrade(id, grade));
            return True;
        return False;
        
    # Print all courses taken (the id) and their grade         # oppgave - fjernes
    def printIdAndGrades(self):
        print(f"\nKurs som {self.getName()}  har:")    
        for cg in self.myGrades:
            print(f"Kurs id   {cg.getCourseId()}, karakter =  {cg.getGrade()}")

    # Compute the average grade
    def getAverageGrade(self):                            # oppgave
        sumGrades = 0;
        for cg in self.myGrades:
            sumGrades += ord(cg.getGrade()) - ord('A')
        return chr(int(sumGrades / len(self.myGrades) + ord('A')))

class Teacher(Person):
    def __init__(self ,name ,address):
        super().__init__(name, address)                 # oppgave
        self.name = name
        self.address = address
        self.courses = {}

    def __str__(self):
        return (f"Teacher:   {super().__str__()}")      # oppgave

    def addCourse(self,  course):                       # oppgave
        if course.id in self.courses:
            return False
        else:
            self.courses[course.id] = course
            return True 

    # ikke en del av oppgaven        
    def removeCourse(self,  courseId):
        if courseId in self.courses:
            del self.courses[courseId]            
            return True
        else:
            return False
    
    def printCourses(self):                               # oppgave
        print(f"Courses teached by {self.getName()}\n")
        for course in self.courses:
            print (self.courses[course])


class Course():
    def __init__(self,id,name,credits, year, semester):
        self.id = id
        self.name = name
        self.credits = credits
        self.year = year
        self.semester = semester
    
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def __str__(self):
        return (f"Course: Id :  {self.id }  - {self.name}")

class CourseGrade():
    def __init__(self,courseId,grade):
        self.courseId = courseId
        self.grade = grade
    def getCourseId(self):
        return self.courseId
    def getGrade(self):
        return self.grade