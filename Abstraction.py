from abc import ABC, abstractmethod
from asyncio.subprocess import Process

print("Coding on Abstraction Concepts")

class Vehicle(ABC):

    @abstractmethod
    def start_Engine(self):
        pass

    @abstractmethod
    def stop_Engine(self):
        pass

# Concrete class implementing the abstract methods for CAR
class Car(Vehicle):
    def start_Engine(self):
        print("Car Engine is Started")
    def stop_Engine(self):
        print("Car Engine is Stopped")

# Concrete class implementing the abstract methods for CAR
class Bike(Vehicle):
    def start_Engine(self):
        print("Bike Engine is Started")

    def stop_Engine(self):
        print("Bike Engine is Stopped")

# Demonstrating abstraction
car = Car()
bike = Bike()

car.start_Engine()
bike.start_Engine()

car.stop_Engine()
bike.stop_Engine()

# Combining Polymorphism and Abstraction
print("Coding both on Combining Polymorphism and Abstraction")

class Payment(ABC):

    @abstractmethod
    def Pay(self,amount):
        pass

# Polymorphism with different payment types
class CreditCardPayment(Payment):
    def Pay(self,amount):
        print(f"Paid {amount} using Credit Card")

class PaypalPayment(Payment):
    def Pay(self,amount):
        print(f"Paid {amount} using Paypal")

# Function demonstrating both abstraction and polymorphism
def Process_Payment(payment:Payment, amount:float):
    payment.Pay(amount)

# Using both abstraction and polymorphism
payment_method = CreditCardPayment()
Process_Payment(payment_method,1500.80)

payment_method = PaypalPayment()
Process_Payment(payment_method,2000.45)
