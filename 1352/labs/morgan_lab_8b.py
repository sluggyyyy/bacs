class Student:
    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def __str__(self)->str:
        return self.first + ' ' + self.last + ' (GPA: ' + str(self.gpa) + ')'

class Course:
    def __init__(self):
        self.roster = []  # list of Student objects
        
    
        
    def add_student(self, student):
        self.roster.append(student)
    
    def __str__(self):
        student_str = ''
        for student in range(len(self.roster)):
            student_str += str(self.roster[student]) + '\n'
        return f'Student list:\n{student_str}'
    
    def get_deans_list(self):
        return [student for student in self.roster if student.gpa >= 3.5]

# Don't edit the code below
def main():
    course = Course()

    course.add_student(Student('Henry', 'Nguyen', 3.5))
    course.add_student(Student('Brian', 'Stern', 2.0))
    course.add_student(Student('Lynda', 'Robinson', 3.2))
    course.add_student(Student('Sonya', 'King', 3.9))

    print(course)

    deans_list = course.get_deans_list()
    print("Dean's list:")
    for student in deans_list:
        print(student)


if __name__ == "__main__":
    main()
