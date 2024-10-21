print("Working on the Inheritance Concepts !")

# Parent class: Employee
class Employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working ")

# Child class: Developer (inherits from Employee)
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)  # Call parent class constructor
        self.programming_language = programming_language
    def work(self):
        print(f"{self.name} is coding on {self.programming_language}")

# Child class: Manager (inherits from Employee)
class Manager(Employee):
    def work(self):
        print(f"{self.name} is Managing the Team")


# Creating objects of Developer and Manager
dev = Developer("Abhishek",12000,"Python")
mgr = Manager("Namrata",15000)

dev.work() # O/P : Abhishek is coding on Python
mgr.work() # O/P : Namrata is Managing the Team