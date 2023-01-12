


class fraction:
    
    def __init__(self,soorat, makhraj):
        self.soorat = soorat
        self.makhraj = makhraj
    def sum(self,f2):
        res = fraction(None,None)

        if (self.makhraj == f2.makhraj):          
            res.soorat = self.soorat  + f2.soorat 
            res.makhraj = self.makhraj 
            
        else:         
            res.soorat = self.soorat * f2.makhraj + f2.soorat * self.makhraj
            res.makhraj = self.makhraj * f2.makhraj 
        
        return res
        
    def sub(self,f2):

        res = fraction(None,None)

        if(self.makhraj == f2.makhraj):
            res.soorat = self.soorat - f2.soorat
            res.makhraj = self.makhraj 
        else:
            
            res.soorat = self.soorat * f2.makhraj - f2.soorat * self.makhraj
            res.makhraj = self.makhraj * f2.makhraj 

        return res

    def div(self,f2):

        res = fraction(None,None)
        res.soorat = self.soorat * f2.makhraj 
        res.makhraj = self.makhraj * f2.soorat
        return res

         



s1 = int(input("soorat kasr 1 ra vared konid : "))
m1 = int(input("mackraj kasr 1 ra vard konid : "))
while m1 == 0 : 
    m1 = int(input("mackraj kasr 1 ra dobare vard konid! : "))
f1= fraction(s1,m1)

s2 = int(input("soorat kasr 2 ra vared konid : "))
m2 = int(input("mackraj kasr 2 ra vard konid : "))
while m2 == 0 : 
    m2 = int(input("mackraj kasr 2 ra dobare vard konid! : "))
f2= fraction(s2,m2)
s = f1.div(f2)
print("Natije:" + str(s.soorat) + "/" + str(s.makhraj))

