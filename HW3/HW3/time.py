#2
class Time():
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def addTime(self,time):
        self.second += time.second
        if self.second>=60:
            self.second,self.minute = self.second%60,self.minute + self.second//60
        
        self.minute += time.minute
        if self.minute>=60:
            self.minute,self.hour = self.minute%60,self.hour+self.minute//60
        
        self.hour += time.hour
    
    def DisplayTime(self):
        print(f'{self.hour} hr {self.minute} mins and {self.second} seconds')
        
    def DisplaySecond(self):
        self.second = self.hour*3600 + self.minute*60 + self.second
        print(self.second)
t1 = Time(2,12,45)
t2 = Time(2,44,45)
t1.addTime(t2)
t1.DisplayTime()
t1.DisplaySecond()
t2.DisplaySecond()