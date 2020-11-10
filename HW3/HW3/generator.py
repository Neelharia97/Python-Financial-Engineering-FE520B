#3 Random Number Generator
import matplotlib.pyplot as plt
class LCG():
    def __init__(self,seed,multiplier,increment,modulus): #Initializing seed, multiplier, increment and modulus
        self.seed =seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        
    def getSeed(self): #Return seed value
        return (self.seed)

    def iter(self):
        return self
    
    def SetSeed(self,inputSeed): #Used to set seed, if seed needs to be changed
        self.seed = inputSeed
        return (self.seed)
    
    def generate(self): #Generate Random Numbers
        self.seed = (self.seed*self.multiplier +self.increment)%self.modulus # Replicating Xn+1 = (Xn(Xn + 1)) mod M
        self.SetSeed(self.seed)
        return(self.seed)

    def __next__(self): #Return next Random Number
        return self.generate()

    def nextNumbers(self,n): #Return next n Random Numbers
        a=[] #List to store random numbers
        for i in range(n):
            a.append(self.generate()) #Storing the random numbers
           # plt.scatter(self.generate(),i) #Visualization of the uniform distribution of the random numbers
        #plt.xlabel("Random Number") #X_axis
       # plt.ylabel("Iteration") #Y_axis
        #plt.show()
        return a


class SCG(LCG): #Inherited class SCG
    def __init__(self,seed,multiplier,increment,modulus):  #Initialization of variables
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        if self.seed%4!=2:
            print("error")
    #    else:
            
    def generate(self): # Function to generate random numbers
        if self.seed%4!=2: #Checks for conditions i.e (X0 mod 4 = 2.)
            ValueError("error") #Returns error if condition  is false
        else:
            self.seed = (self.seed*(self.seed + 1))%self.modulus #Generation of Random number if satisfies condition. Formula : Xn+1 = (Xn(Xn + 1)) mod M
            return (self.seed)
        
    
if __name__ == "__main__":
    a = LCG(2,1103515245,12345,2**32)
    b = SCG(2,1103515245,12345,2**32)
    print("LCG Next Number: ",a.__next__())
    print("SCG Next Number: ",b.__next__())
    print("LCG Next n Numbers: ",a.nextNumbers(1000))
    print("SCG Next n Numbers: ",b.nextNumbers(1000))
    #print("\n")

