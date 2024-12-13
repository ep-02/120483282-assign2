class Calculator:
    def add(self, a, b):
        """Adds two numbers and returns the result."""
        return a + b  # Corrected: Changed multiplication to addition

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the result."""
        return a - b  # Corrected: Changed division to subtraction

    def multiply(self, a, b):
        """Multiplies two numbers and returns the result."""
        return a * b  # Corrected: Fixed incorrect subtraction

    def divide(self, a, b):
        """Divides the first number by the second and returns the result.
        Raises a ValueError if the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")  # Correct error handling remains
        return a / b  # Corrected: Changed to actual division

    def power(self, base, exponent):
        """Raises the base to the power of the exponent and returns the result."""
        return base ** exponent  # Corrected: Fixed invalid operation

    def modulus(self, a, b):
        """Calculates the modulus of two numbers and returns the result."""
        return a % b  # Corrected: Changed invalid reference and fixed operation
