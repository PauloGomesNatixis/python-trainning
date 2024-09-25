#from cgi import test
#from pydantic import BaseModel # type: ignore

class Calculator(BaseModel):
    a: int
    b: int
    
    def add(self)->int:
        return self.a + self.b
    
    def sub(self)->int:
        result = self.a - self.b
        if result <0:
            raise ValueError('resultado menor que zero')
            #print('resultado menor que zero')
        else:
            return result


calc = Calculator(a=10, b=5)
print(calc.add())
print(calc.sub())

calc = Calculator(a=5, b=10)
print(calc.add())
print(calc.sub())


