print("Coding on Encapsulation Concepts")

# Scenario : You want to ensure that certain sensitive information, like an employee's social security number(ssn), is not directly accessible.
class Employee:
    def __init__(self,name,salary,ssn): # __init__ >>  Initializes a new object when created.
        self.name = name
        self.salary = salary
        self.__ssn = ssn  # Private attribute

# Public method to access private attribute
    def get_ssn(self):
        return f"SSN is : {self.__ssn[:3]}-XX-XXXX" # Means O/P will be

# Special method for equality comparison
    def __eq__(self, other):
        return self.salary == other.salary and self.get_ssn() ==other.get_ssn()
# Creating an Employee object
emp1 = Employee("Abhishek",14000,"1234-5678-9123")
print(f"Employee Name is : {emp1.name} who has Salary of : {emp1.salary} and the SSN is : {emp1.get_ssn()}")
#O/P > Employee Name is : Abhishek who has Salary of : 14000
                    # and the SSN is : SSN is : 123-XX-XXXX

emp2 = Employee("Namrata",13000,"3456-8956-3214")

#Comparing 2 Employees
print(emp1==emp2) # O/P : false
print(emp1==emp1) # O/P : false
