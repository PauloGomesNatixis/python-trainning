from colorsys import ONE_THIRD
from typing import Callable, Dict, Union
from unittest import result

#from networkx import power
from pydantic import BaseModel


"""
Below you will find some Python functions within a class. 
Your task is to add type hints to the functions and variables. 
For example, the `add` function should have a type hint of `int` for the `number` parameter 
and the return type. 
The `number` variable should have a type hint of `int`.


    def all():
        return {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'power': self.power
        }

"""
# Define the Pydantic model for the 'all' function's return value
class AllModel(BaseModel):
    add: Union[int, float]
    subtract: Union[int, float]
    multiply: Union[int, float]
    divide: Union[int, float]
    power: Union[int, float]


"""
## Exercise

```python
class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self, number):
        return self.number + number

    def subtract(self, number):
        return self.number - number

    def multiply(self, number):
        return self.number * number

    def divide(self, number):
        return self.number / number

    def power(self, number):
        return self.number ** number
"""

class Calculator:
    def __init__(self, number: Union[int, float]):
        self.number: Union[int, float] = number

    def add(self, number: Union[int, float]) -> Union[int, float]:
        return self.number + number

    def subtract(self, number: Union[int, float]) -> Union[int, float]:
        return self.number - number

    def multiply(self, number: Union[int, float]) -> Union[int, float]:
        return self.number * number

    def divide(self, number: Union[int, float]) -> float:
        return self.number / number  # Division always returns float

    def power(self, number: Union[int, float]) -> Union[int, float]:
        return self.number ** number

    def all(self, others_number:int) -> AllModel:
        all_results = AllModel(
            add = self.add(others_number),
            subtract = self.subtract(others_number),
            multiply = self.multiply(others_number),
            divide = self.divide(others_number),
            power = self.power(others_number),
            )

        return all_results



calc = Calculator(10)
others_number = 6

results = calc.all(others_number)

print(results)
print(results.json())
