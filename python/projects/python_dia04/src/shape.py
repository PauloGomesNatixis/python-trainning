from math import pi
from logging import DEBUG, INFO



class Shape:
    def area(self):
        print("This is the area funcion!")
            
            

class Square(Shape):
    #metodo contrutor para criar nova instancia
    def __init__(self, size):
        self.width = size
        self.height = size
        
    #garantir que height é numero
    #if height:
     #   sel
        
    def perimeter(self): 
        return 2 * (self.height + self.width) 
        
    def area(self): 
        return (self.height * self.width) 
        
class Retangle(Square):
    #metodo contrutor para criar nova instancia
    def __init__(self, width: int, height:int|None = None):
        self.width = width
        self.height = height
        

class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def circunference(self):
        return 2 * 3,14 * self.radius

    def perimeter(self):
        return 2 * 3,14 * self.radius

    def area(self):
        return (3,14 * self.radius ** 2)
    


if __name__ == "__main__" :
    shape = Shape() 
    square = Square(size = 2)
    retangulo = Retangle(width = 2, height = 3)
    circle = Circle(radius = 2.5)
    
    perimetro_quadrado = square.perimeter()
    perimetro_retangulo = retangulo.perimeter()
    perimetro_circ = circle.perimeter()
    
    area_quadrado = square.area()
    area_retangulo = retangulo.area()
    area_circ = circle.area()
    
    print("FIM")


