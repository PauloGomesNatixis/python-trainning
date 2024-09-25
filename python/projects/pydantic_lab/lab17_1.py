from pydantic import BaseModel, ValidationError

class CalculatorModel(BaseModel):
    """Model to validate the input data for Calculator."""
    number: int

# Create an instance of the CalculatorModel with a valid number
try:
    calculator = CalculatorModel(number=5)
    print("Valid input:", calculator.dict())  # Should output: {'number': 5}
except ValidationError as e:
    print(e)

# Test with an invalid input (e.g., a string)
try:
    calculator = CalculatorModel(number="invalid")
    print("Invalid input:", calculator.dict())
except ValidationError as e:
    print("Validation Error:", e)
