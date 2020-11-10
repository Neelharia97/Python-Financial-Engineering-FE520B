#1.1
import numpy as np
class Rectangular():
    
    def __init__(self,length,breadth): #initializing length and breadth
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth #Calculating area i.e length*breadth

    def perimeter(self):
        return 2*(self.length+self.breadth) #Calculating perimeter i.e 2(length+breadth)


#1.2

if __name__ == "__main__":
    length= np.random.randint(1,100,10) #Generating random values for length
    width = np.random.randint(1,100,10) #Generating random values for width

    a = np.array(length) #Entering length values into array
    b = np.array(width) #Entering width values into array

    print("length: ",a)
    print("breadth: ",b)

    myRec = Rectangular(a,b) #Creating method for class
    print("area: ",myRec.area()) #Calling function in class
    print("perimeter: ",myRec.perimeter()) #Calling function in class