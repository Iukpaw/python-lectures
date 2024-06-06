
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def get_info(self):
        return f"Employee Name: {self.name}, Department: {self.department}"

class Manager(Employee):
    def __init__(self, name, department, team_size):
        super().__init__(name, department)
        self.team_size = team_size
    
    def get_info(self):
        return f"Manager Name: {self.name}, Department: {self.department}, Team Size: {self.team_size}"


employees = []

employees.append(Employee('John', 'Sales'))
employees.append(Employee('Kate', 'Marketing'))
employees.append(Employee('David', 'Sales'))
employees.append(Manager('George', 'Marketing', 6))

for employee in employees:
    print(employee.get_info())
