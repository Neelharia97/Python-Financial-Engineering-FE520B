#4point.py
import math
class Point():
    def __init__(self,x,y): #Initializing co-ordinates x and y
        self.x = x
        self.y = y
        
    def cal(self):
        return math.sqrt(self.x**2 + self.y**2) #Calculating distance




