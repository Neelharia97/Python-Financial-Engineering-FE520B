#2
class Time():
    def __init__(self,hour,minute,second): #Initializing hour minute and second values
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def addTime(self,time): #Calculating total time after addition
        self.second += time.second
        if self.second>=60: #Convert to mins if seconds greater than 60
            self.second,self.minute = self.second%60,self.minute + self.second//60 #assign remainder as seconds beyond 60
        
        self.minute += time.minute
        if self.minute>=60: #Convert to hours if mins greater than 60
            self.minute,self.hour = self.minute%60,self.hour+self.minute//60
        
        self.hour += time.hour
    
    def DisplayTime(self): #Call function to display
       return (f'{self.hour} hr {self.minute} mins and {self.second} seconds')
        
    def DisplaySecond(self): #Call function to convert time into seconds and display
        self.second = self.hour*3600 + self.minute*60 + self.second
        return (self.second)
if __name__ == "__main__":
    t1 = Time(2,12,45) #Creating instance t1 for Time class
    t2 = Time(2,44,45)
    t1.addTime(t2) #Calling function addtime
    print("Add Time: " ,t1.DisplayTime())
    print("Seconds t1: ", t1.DisplaySecond())
    print("Seconds t2: ",t2.DisplaySecond())


