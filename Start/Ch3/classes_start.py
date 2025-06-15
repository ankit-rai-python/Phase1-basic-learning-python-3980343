# LinkedIn Learning Python course by Joe Marini
"""
This script demonstrates the use of classes and inheritance in Python by modeling vehicles.
Classes:
--------
1. Vehicle:
    - Base class representing a generic vehicle.
    - Attributes:
        - bodystyle: The type of vehicle (e.g., Car, Motorcycle).
    - Methods:
        - __init__(bodystyle): Initializes the vehicle with a specific bodystyle.
        - drive(speed): Sets the vehicle's mode to "driving" and assigns a speed.
2. Car (inherits from Vehicle):
    - Represents a car, a specific type of vehicle.
    - Attributes:
        - wheels: Number of wheels (default is 4 for cars).
        - doors: Number of doors (default is 4 for cars).
        - enginetype: Type of engine (e.g., Gasoline, Electric).
    - Methods:
        - __init__(enginetype): Initializes the car with a specific engine type.
        - drive(speed): Prints a message about driving the car and calls the parent class's drive method.
3. Motorcycle (inherits from Vehicle):
    - Represents a motorcycle, another specific type of vehicle.
    - Attributes:
        - wheels: Number of wheels (2 or 3 depending on whether it has a sidecar).
        - doors: Number of doors (always 0 for motorcycles).
        - enginetype: Type of engine (e.g., Gasoline, Electric).
    - Methods:
        - __init__(enginetype, has_sidecar): Initializes the motorcycle with a specific engine type and sidecar status.
        - drive(speed): Prints a message about driving the motorcycle and calls the parent class's drive method.
Objects:
--------
1. car1: A Car object with a Gasoline engine.
2. car2: A Car object with an Electric engine.
3. motorcycle1: A Motorcycle object with a Gasoline engine and no sidecar.
4. motorcycle2: A Motorcycle object with an Electric engine and a sidecar.
Usage:
------
- The script creates a list of vehicles (cars and motorcycles) and iterates through them.
- For each vehicle, it prints its attributes (bodystyle, engine type, wheels, and doors) and simulates driving at 60 mph.
Key Concepts:
-------------
- Inheritance: Car and Motorcycle inherit from the Vehicle base class.
- Method Overriding: Both Car and Motorcycle override the `drive` method to provide specific behavior.
- Polymorphism: The `drive` method is called on different types of vehicles, demonstrating polymorphic behavior.
- Object Initialization: Demonstrates how to initialize objects with specific attributes.
"""
# Example file for working with classes
#


class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode="driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
    def drive(self, speed):
        print(f"Driving at {speed} mph in a {self.bodystyle} with {self.enginetype} engine.")
        return super().drive(speed)
        

class Motorcycle(Vehicle):
    def __init__(self, enginetype, has_sidecar):
        super().__init__("Motorcycle")
        if(has_sidecar):
            self.wheels = 3
        else:
            self.wheels = 2

        self.doors = 0
        self.enginetype = enginetype


    def drive(self, speed):
        print(f"Driving at {speed} mph in a {self.bodystyle} with {self.enginetype} engine.")
        return super().drive(speed)


car1 = Car("Gasoline")
car2 = Car("Electric")
motorcycle1 = Motorcycle("Gasoline", False)
motorcycle2 = Motorcycle("Electric", True)
# car1.drive(60)

vehicles = [car1, car2, motorcycle1, motorcycle2]
for vehicle in vehicles:
    print(f"{vehicle.bodystyle} with {vehicle.enginetype} engine, "
        f"{vehicle.wheels} wheels, and {vehicle.doors} doors.")
    vehicle.drive(60)
