class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f'Name: {self.name}')
        print(f'Skills: {self.skills}')
        print(f'Details: {self.details}')
