from typing import Any


class Rectangle:
    def __init__(self,length,breadth) -> None:
        self.length=length
        self.breadth=breadth
    # def __str__(self) -> str:
    #     return f"breadth = {self.length} and length = {self.breadth}"
    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     return "hello world"
    def area(self)->float:
        return self.length*self.breadth
    
    def perimeter(self)->float:
        return 2*(self.length+self.breadth)
    def isSquare(self)->bool:
        # if self.length==self.breadth
        if self.length==self.breadth:
            return True
        return False
        

# soo in list if we create list and print we are getting list itself it is becos we have another method callled [__str__] which return str
# soo when we print the object we instead of adress it is printing the values 
x=Rectangle(5,6)
print(x)
print(x.area())
print(x.perimeter())
print(x.isSquare())
