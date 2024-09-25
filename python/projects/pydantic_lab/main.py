from cgi import test
from pydantic import BaseModel

class Foo(BaseModel):
    foo: str
    bar: int
    
def all (baz: Foo)->dict:
    return dict(baz)

#def teste(foo: int|None = None )-> bool:
#   return foo

x= Foo(foo="abc", bar=2)
print(all(x))

#print(test(123))