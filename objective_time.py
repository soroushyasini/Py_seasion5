class time:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s       
    def show(self):
            print(self.h, ":" , self.m, ":" , self.s)
            
    def sub(self,time2):
        res = time(None, None, None)
        if(self.s < time2.s):
            self.m = self.m - 1
            self.s = self.s + 60
        res.s = self.s - time2.s
        if(self.m < time2.m):   
            self.h = self.h - 1
            self.m = self.m + 60
        res.m = self.m - time2.m
        if(self.h < time2.h):
            res.s = 0
            res.m =  0
            res.h = 0
        else:
            res.h = self.h - time2.h
        return res
    def convertTimeToSec(self):
        seconds = self.s + self.m * 60 + self.h * 3600
        print("Time to seconds: "+ str(seconds))
class seconds:
    def __init__(self,seconds):
        self.seconds = seconds
    def convertSecondsToTime(self,timeClass):
        timeClass.s = self.seconds % 60 
        timeClass.m = self.seconds // 60
        timeClass.h = timeClass.m // 60
        if(timeClass.h >= 1):
            timeClass.m = timeClass.m % 60 
        
        timeClass.show()

inputSeconds = int(input("Please enter seconds you want to convert: "))

time3 = time(None,None,None)
seconds1 = seconds(inputSeconds)
seconds1.convertSecondsToTime(time3)

h1 = int(input("Pleae enter hour for variable 1: "))
m1 = int(input("Pleae enter minute for variable 1: "))
s1 = int(input("Pleae enter second for variable 1: "))
h2 = int(input("Pleae enter hour for variable 2: "))
m2 = int(input("Pleae enter minutes for variable 2: "))
s2 = int(input("Pleae enter seconds for variable 2: "))

time1 = time(h1,m1,s1)
time2 = time(h2,m2,s2)

time1.show()
time2.show()
s = time1.sub(time2)
s.show()
s.convertTimeToSec()
