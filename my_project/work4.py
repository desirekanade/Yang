class Student:
    def __init__(self, name, age, group_number, average_grade):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def scholarship_amount(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        return self.scholarship_amount() > other.scholarship_amount()


class Graduate(Student):
    def __init__(self, name, age, group_number, average_grade, research_title):
        super().__init__(name, age, group_number, average_grade)
        self.research_title = research_title

    def scholarship_amount(self):
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        else:
            return 0

# Example
student1 = Student("1 person", 20, "101", 4.5)
graduate1 = Graduate("2 person", 25, "201", 5, "Deep Learning Research")

print(student1.display_info())
print(f"Student Scholarship: {student1.scholarship_amount()}")

print(graduate1.display_info())
print(f"Graduate Scholarship: {graduate1.scholarship_amount()}")

if student1.compare_scholarship(graduate1):
    print("The student's scholarship is higher")
else:
    print("The graduate's scholarship is higher or equal")
