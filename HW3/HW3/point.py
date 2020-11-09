#4point.py
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def cal(self):
        return sqrt(self.x**2 + self.y**2)
    