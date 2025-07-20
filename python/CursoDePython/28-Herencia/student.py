from person import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f'{super().__str__()} and my student ID is: {self.student_id}'

    def greet(self):
        super().greet()
        print(f'My student ID is: {self.student_id}')

