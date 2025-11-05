    import streamlit as st
    class Person(ABC):
        """
        Abstract base class representing a person.
        """

        def __init__(self, name, age, weight, height):
            """
            Initializes a new instance of the Person class.
            """
            self.name = name
            self.age = age
            self._weight = weight
            self._height = height

        @property
        def weight(self):
            """Gets the weight of the person."""
            return self._weight

        @weight.setter
        def weight(self, value):
            """Sets the weight of the person."""
            if value < 0:
                raise ValueError("Weight cannot be negative")
            self._weight = value

        @property
        def height(self):
            """Gets the height of the person."""
            return self._height

        @height.setter
        def height(self, value):
            """Sets the height of the person."""
            if value < 0:
                raise ValueError("Height cannot be negative")
            self._height = value

        @abstractmethod
        def calculate_bmi(self):
            """Calculates the BMI of the person."""
            pass

    # ------------------- Concrete Subclass -------------------
    class BMI_Person(Person):
        """Concrete class that implements BMI calculation."""

        def calculate_bmi(self):
            bmi = self.weight / (self.height ** 2)
            return round(bmi, 2)

    # ------------------- Streamlit App -------------------
    st.title("💪 BMI Calculator App")

    st.write("Enter your details below to calculate your Body Mass Index (BMI).")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (m)", min_value=0.0, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            person = BMI_Person(name, age, weight, height)
            bmi = person.calculate_bmi()

            # Determine BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            st.success(f"{name}, your BMI is **{bmi}** ({category}).")
        else:
            st.error("Please enter valid height and weight values.")



