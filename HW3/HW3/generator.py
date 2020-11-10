#3 Random Number Generator
class LCG():
    def __init__(self,seed,multiplier,increment,modulus):
        self.seed =seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        
    def getSeed(self):
        return (self.seed)

    def iter(self):
        return self
    
    def SetSeed(self,inputSeed):
        self.seed = inputSeed
        return (self.seed)
    
    def generate(self):
        self.seed = (self.seed*self.multiplier +self.increment)%self.modulus
        self.SetSeed(self.seed)
        return(self.seed)

    def __next__(self):
        return self.generate()

    def nextNumbers(self,n):

            #print(self.generate())
        return [self.generate() for i in range(n)]
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
        
    
if __name__ == "__main__":
    a = LCG(2,1103515245,12345,2**32)
    b = SCG(2,1103515245,12345,2**32)
   # print(a.__next__())
   #print(b.__next__())
    print(a.nextNumbers(10000000))
   # print(b.nextNumbers(10))
    #print("\n")

