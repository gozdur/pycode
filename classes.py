

class Employee:

    num_of_emps = 0   # class variable
    raise_amount = 1.05 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # instance variable


emp_1 = Employee('Pawel', 'Gozdur', 30000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 2
print(emp_1.raise_amount)

print(Employee.num_of_emps)





