class Rectangle:
    def __init__(self,length,breadth) -> None:
        self.length=length
        self.breadth=breadth
    
    def area(self)->float:
        return self.length*self.breadth
    
    def perimeter(self)->float:
        return 2*(self.length+self.breadth)
    def isSquare(self)->bool:
        # if self.length==self.breadth
        if self.length==self.breadth:
            return True
        return False
        



x=Rectangle(5,6)
print(x.area())
print(x.perimeter())
print(x.isSquare())
