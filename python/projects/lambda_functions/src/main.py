"""Este é ficheiro principal do projeto.""" # doc string do package

from copyreg import constructor
from typing import Any
from unittest import result


class ClassA:
    """definicao da class"""
    
    # constructor
    def __init__(self, name: str):
        """
        Args: 
            name(str): class name
        """
        name = name
        pass #
    ## melhor pratica para quando class nao estao criada
    # raise NotImplementedError("this class is not implemetend yet.")
    

def get_person(
    name:str,
    age: int | None = None #pode ser int ou None, valor por defeito = None
    )-> dict:
    """
    Get person from user 'name' 
    Args:
        name(str): name from user
        
    retuurns: 
        A string representing the name
    """ # doc string da funcao
    result: dict[str,Any] = {
        "name":name
        }
    
    if age is not None:
        result["age"]= age
    
    return result

#my_name: str = ""
#"""my_name is a string variavel """
#my_name = get_name(my_name)

my_person = get_person(
    name="bruno",
    age=29)

print(my_person)

breakpoint()
    
    
def get_name(name:str)-> str:
    """
    Get name from user 'name' 
    Args:
        name(str): name from user
        
    retuurns: 
        A string representing the name
    """ # doc string da funcao
    return name

my_name: str = ""
"""my_name is a string variavel """
my_name = get_name(my_name)

def func(name ="aaa")-> str:
    print(name)
    return name


func() #valor por defeito
func("hello")
func(name="hello name")
