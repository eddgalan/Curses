class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError('Salary cannot be negative')
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary
        print(f"{self.name}'s salary was deleted")