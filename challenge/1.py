from abc import ABC, abstractmethod
import random


# Abstract base class
class Person(ABC):
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height
        self.bmi = None
        self.category = None

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be a positive number.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {self.bmi:.2f}")
        print(f"Category: {self.category}")


# Adult class
class Adult(Person):
    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)
        self.get_bmi_category()

    def get_bmi_category(self):
        if self.bmi < 18.5:
            self.category = "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            self.category = "Normal weight"
        elif 24.9 <= self.bmi < 29.9:
            self.category = "Overweight"
        else:
            self.category = "Obese"


# Child class
class Child(Person):
    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)
        self.get_bmi_category()

    def get_bmi_category(self):
        if self.bmi < 14:
            self.category = "Underweight"
        elif 14 <= self.bmi < 18:
            self.category = "Normal weight"
        elif 18 <= self.bmi < 24:
            self.category = "Overweight"
        else:
            self.category = "Obese"


# BMI Application class
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person: Person):
        self.people.append(person)

    def generate_random_person(self):
        names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
        name = random.choice(names)
        age = random.randint(5, 65)
        weight = round(random.uniform(20.0, 120.0), 1)
        height = round(random.uniform(1.0, 2.0), 2)

        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        person.calculate_bmi()
        self.add_person(person)

    def print_results(self):
        print("\n--- BMI Results ---")
        for person in self.people:
            person.print_info()

    def run(self):
        print("Welcome to the BMI Calculator App")
        print("Generating 3 random people...\n")

        for _ in range(3):  # Generate 3 random people
            self.generate_random_person()

        self.print_results()


# Main runner
if __name__ == "__main__":
    app = BMIApp()
    app.run()
