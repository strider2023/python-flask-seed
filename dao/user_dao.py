class UserDao:
    'Common base class for all employees'

    id = -1
    name = ''
    department = ''

    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

    def getEmployee(self):
        dict = {}
        dict['id'] = self.id
        dict['name'] = self.name
        dict['department'] = self.department
        return dict

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary