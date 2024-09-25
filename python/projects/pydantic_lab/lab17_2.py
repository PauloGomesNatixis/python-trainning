from pydantic import BaseModel

class AllModel(BaseModel):
    """Pydantic model to validate the results of Calculator operations."""
    add: int
    subtract: int
    multiply: int
    divide: float
    power: int


class Calculator:
    """A simple calculator that performs basic arithmetic operations."""

    def __init__(self, number: int) -> None:
        """
        Initialize the calculator with a number.
        Args:
            number (int): The base number for calculations.
        """
        self.number = number

    def add(self, number: int) -> int:
        """
        Add a number to the base number.
        Args:
            number (int): The number to add.
        Returns:
            int: The result of the addition.
        """
        return self.number + number

    def subtract(self, number: int) -> int:
        """
        Subtract a number from the base number.
        Args:
            number (int): The number to subtract.
        Returns:
            int: The result of the subtraction.
        """
        return self.number - number

    def multiply(self, number: int) -> int:
        """
        Multiply the base number by another number.
        Args:
            number (int): The number to multiply by.
        Returns:
            int: The result of the multiplication.
        """
        return self.number * number

    def divide(self, number: int) -> float:
        """
        Divide the base number by another number.
        Args:
            number (int): The number to divide by.
        Returns:
            float: The result of the division.
        """
        return self.number / number

    def power(self, number: int) -> int:
        """
        Raise the base number to the power of another number.
        Args:
            number (int): The exponent to raise the base number by.
        Returns:
            int: The result of the exponentiation.
        """
        return self.number ** number

    def all(self, number: int) -> AllModel:
        """
        Perform all basic operations and return the results.
        Args:
            number (int): The number to perform calculations with.
        Returns:
            AllModel: A Pydantic model containing the results of all operations.
        """
        all_results = AllModel(
            add=self.add(number),
            subtract=self.subtract(number),
            multiply=self.multiply(number),
            divide=self.divide(number),
            power=self.power(number)
        )
        return all_results


if __name__ == "__main__":
    calculator = Calculator(10)
    
    # Testing individual methods
    print("Addition (10 + 5):", calculator.add(5))          # Output: 15
    print("Subtraction (10 - 5):", calculator.subtract(5))   # Output: 5
    print("Multiplication (10 * 5):", calculator.multiply(5)) # Output: 50
    print("Division (10 / 5):", calculator.divide(5))        # Output: 2.0
    print("Power (10 ** 5):", calculator.power(5))           # Output: 100000

    # Testing all operations with number 5
    print("All operations with number 5:", calculator.all(5).dict())
