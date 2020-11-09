#1.1
class Rectangular():
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
myRec = Rectangular(10,20)
print(myRec.area())
print(myRec.perimeter())    

#1.2
import numpy as np
length= np.random.randint(1,100,10)
width = np.random.randint(1,100,10)

a = np.array(length)
b = np.array(width)

print("length: ",a)
print("breadth: ",b)

myRec = Rectangular(a,b)
print("area: ",myRec.area())
print("perimeter: ",myRec.perimeter())