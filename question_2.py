# Create Parent class Person
# 1. Has name, age, city
# 2. Has method introduce() - prints name and city

# Create Child class Student that inherits Person
# 1. Has extra attribute course and grade
# 2. Has method study() - prints "studying course name"

# Create Child class Teacher that inherits Person
# 1. Has extra attribute subject and salary
# 2. Has method teach() - prints "teaching subject name"

# Test:
# - Create 2 students and 2 teachers
# - Call introduce() on all
# - Call study() and teach()


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"city: {self.city}")

    def introduce(self):
        print(f"name: {self.name}")
        print(f"city: {self.city}")


class Student(Person):
    def __init__(self, name, age, city, course, grade):
        super().__init__(name, age, city)
        self.course = course
        self.grade = grade

    def study(self):
        print(f"studing: {self.course} course")


class Teacher(Person):
    def __init__(self, name, age, city, subject, salary):
        super().__init__(name, age, city)
        self.subject = subject
        self.salary = salary

    def teach(self):
        print(f"Teaching: {self.subject} subject")


person_1 = Person("rohit", "20", "nashik")
person_2 = Person("omkar", "23", "pune")

Student_1 = Student("rahul", "24", "nagpur", course="engineering", grade="A+")
Student_2 = Student("abhishek", "21", "mumbai", course="medical", grade="A")

teacher_1 = Teacher("sahil", "21", "thane", subject="maths", salary="30000")
teacher_2 = Teacher("tejas", "20", "akola", subject="biology", salary="20000")

person_1.info()
person_2.info()

Student_1.info()
print(f"course: {Student_1.course}")
print(f"grade: {Student_1.grade}")
Student_1.study()

Student_2.info()
print(f"course: {Student_2.course}")
print(f"grade: {Student_2.grade}")
Student_2.study()

teacher_1.info()
print(f"subject: {teacher_1.subject}")
print(f"salary: {teacher_1.salary}")
teacher_1.teach()

teacher_2.info()
print(f"subject: {teacher_2.subject}")
print(f"salary: {teacher_2.salary }")
teacher_2.teach()
