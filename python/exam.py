# class Geometry:
#     def __init__(self, sides):
#         self.sides = sides

#     def perimeter(self):
#         return sum(self.sides)

# class Triangle(Geometry):
#     def __init__(self, sides):
#         super().__init__(sides)

#     def area(self):
#         a, b, c = self.sides
#         s = sum(self.sides) / 2

#         return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# triangle = Triangle([3, 4, 5])
# print(triangle.create_perimeter())


# def my_func(*args, **kwargs):
#     for arg in args:
#         print(arg)
    
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# my_func(1, 2, 3, a=10, b=20)

class BaseClass:
    def __init__(self, value: int):
        self.value = value

    def multiply(self, factor: int):
        return self.value * factor

class DerivedClass(BaseClass):
    def __init__(self, value: int):
        super().__init__(value)

    def divide(self, factor: int):
        return self.value / factor
    
class FinalClass(DerivedClass):
    def __init__(self, value: int):
        super().__init__(value)

    def divide(self, factor: int):
        result = super().divide(factor)

        return result / factor

classes = [BaseClass(10), DerivedClass(10), FinalClass(10)]

print(classes[1].divide(2))
print(classes[2].divide(2))

for _ in classes:
    print(_.multiply(2))

    
print("\n\n\14\n")

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

person = Person(name='Alice', age='30')
print(person)