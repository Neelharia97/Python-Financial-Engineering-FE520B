#3 Random Number Generator
class LCG():
    def __init__(self,seed,multiplier,increment,modulus):
        self.seed =seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        
    def getSeed(self):
        return (self.seed)
    
    def SetSeed(self,inputSeed):
        self.seed = inputSeed
        return (self.seed)
    
    def generate(self):
        self.seed = (self.seed*self.multiplier +self.increment)%self.modulus
        self.SetSeed(self.seed)
        return(self.seed)
    
    def nextNumbers(self,n):
        for i in range(n):
            #print(self.generate())
            print(self.generate()/2**32)
            #plt.scatter(self.generate()/2**32,i)

class SCG(LCG):
    def __init__(self,seed,multiplier,increment,modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        if self.seed%4!=2:
            print("error")
    #    else:
            
    def generate(self):
        if self.seed%4!=2:
            ValueError("error")
        else:
            self.seed = (self.seed*(self.seed + 1))%self.modulus
            return (self.seed)
        
    
        
a = LCG(2,1103515245,12345,2**32)
b = SCG(2,1103515245,12345,2**32)
b.nextNumbers(10)
print("\n")
a.nextNumbers(10)
    