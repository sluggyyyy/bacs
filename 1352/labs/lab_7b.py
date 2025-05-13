class Student:
    # TODO: create class variables, one called count to keep track of the number of
    # Student objects that have been instantiated, and another to keep track of
    # the next available student id to assign. The first student instantiated should
    # be given the id 876000001
    count = 0
    next_student_id = 876000001
    

    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average
        self.student_id = Student.next_student_id
        Student.count += 1
        Student.next_student_id += 1
        
        # TODO: assign the student_id instance variable to this student, and update
        # the class variables as needed:


    def __str__(self)->str:
        # TODO: change the string representation below of the student to include their student_id
        # The format should look like "Saquon Barkley (876000002, GPA 3.8)"
        
        return f"{self.first} {self.last} ({self.student_id}, GPA: {self.gpa})"
    

def main():
    saquon = Student('Saquon', 'Barkley', 3.8)
    sven = Student('Sven', 'Nilsson', 2.5)
    desta = Student('Desta', 'Bekele', 3.4)
    print(Student.count)
    print(desta)

if __name__ == "__main__":
    main()