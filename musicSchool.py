class MusicSchool:

    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Chello"]],
                "Eric":   [12, "583-356-223", ["Singing"]]}

    def __init__(self, max_num_students, working_hours, revenue):
        self.max_num_students= max_num_students
        self.working_hours = working_hours
        self.revenue = revenue
    
    def print_students_data(self):
        for student in self.students:
            print("Student:", student,"who is", self.students[student][0], "years old and is taking", self.students[student][2])
    
    def print_student(self, name):
        self.name = name
        
        if self.name in self.students:
            print("Student:", name,"who is", self.students[name][0], "years old and is taking", self.students[name][2])
        else:
            print("This student is not enrolled in this school.")
    
    def add_student(self, name, age, phone_number, classes):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.classes = [classes]
        
        student_count = 0
        
        for students in self.students:
            student_count += 1
        
        if student_count < 56:
            self.students[name] = [age, phone_number, [classes]]
            print(self.students)
        
    def export_student_list(self):
        with open('studentList.txt', 'w') as f:
            print(self.students, file=f)
            
            
            
            
            
            
            
            