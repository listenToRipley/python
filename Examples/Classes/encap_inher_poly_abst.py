import math
from abc import ABC, abstractmethod

# Encapsulation

class Email:
  def __init__(self, sender, recipient, subject, body):
    self.sender = sender
    self.recipient = recipient
    self.subject = subject
    self.body = body

  def send_send(self):
    #Logic related to sending an email
    pass

  def read_email(self):
    #Logic related to reading an email
    pass

# Inheritances

class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def start(self):
    #Code to start the vehicle
    pass

  def stop(self):
    #code to stop the vehicle
    pass

class Car(Vehicle):
  def __init__(self, make, model, doors_qty):
    super().__init__(make, model)
    self.doors_qty = doors_qty

  def lock_doors(self):
    #Logic to lock the doors
    pass

  def unlock_doors(self):
    #Logic to unlock the doors
    pass

class Motorcycle(Vehicle):
  def __init__(self, make, model, num_wheels):
    super().__init__(make, model)
    self.num_wheels = num_wheels

# Polymorphism

class Shape:
  def calc_area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def calc_area(self):
    return math.pi * pow(self.radius, 2)

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def calc_area(self):
    return self.width * self.height
  

shapes = [Circle(5), Rectangle(10,2), Circle(7), Rectangle(25, 75)]

for shape in shapes:
  print(shape.calc_area())


# Abstraction

class Payment():
  @abstractmethod
  def process_payment(self):
    pass

class CreditCardPayment(Payment):
  def process_payment(self):
    #Code to process credit card payment
    pass

class StripePayment(Payment):
  def process_payment(self):
    #Code to process payment
    pass

class PayPalPayment(Payment):
  def process_payment(self):
    #Code to process payment
    pass