
class Data:
    def __init__(self,year,month,day):
        self.day = day
        self.month = month
        self.year = year
    def show(self):
        print( str(self.year) + "/" + str(self.month) + "/" + str(self.day)) 
    def add(self,dataObj):
        res = Data(None,None,None)
        if(self.day + dataObj.day > 30):
            self.day -= 30
            self.month += 1
        res.day = self.day + dataObj.day
        if (self.month + dataObj.month > 12):
            self.month -= 12
            self.year += 1
        res.month = self.month + dataObj.month
        res.year = self.year + dataObj.year      
        print("The result of sum")  
        return res
    
    def sub(self,dataObj):
        res = Data(None,None,None)
        if(self.day - dataObj.day <= 0):
            self.day += 30
            self.month -= 1
        res.day = self.day - dataObj.day
        if (self.month - dataObj.month <= 0):
            self.month += 12
            self.year -= 1
        res.month = self.month - dataObj.month
        if(self.year - dataObj.year < 0):
            res.year = 0
            res.month =  0
            res.day = 0 
        else:  
            res.year = self.year - dataObj.year   
        print("Result of subtraction")     
        return res
        

    def IsValidData(self):
        
        if(self.day > 30 or self.day < 1):           
            return False
            
        if(self.month > 12 or self.month < 1):
            return False
        if(self.year < 0):
            return False
        
        
        
       
y1 = int(input("Pleae enter the year for data 1: "))
m1 = int(input("Pleae enter the month for data 1: "))
d1 = int(input("Pleae enter the day for data 1: "))
data1 = Data(y1,m1,d1)
while(data1.IsValidData() == False):
    print("The values you've entered are not valid, Please try again:\n")
    y1 = int(input("Pleae enter the year for data 1: "))
    m1 = int(input("Pleae enter the month for data 1: "))
    d1 = int(input("Pleae enter the day for data 1: "))
    data1 = Data(y1,m1,d1)
    
y2 = int(input("Pleae enter the year for data 2: "))
m2 = int(input("Pleae enter the month for data 2: "))
d2 = int(input("Pleae enter the day for data 2: "))
data2 = Data(y2,m2,d2)
while(data2.IsValidData() == False):
    print("The values you've entered are not valid, Please try again:\n")
    y2 = int(input("Pleae enter the year for data 2: "))
    m2 = int(input("Pleae enter the month for data 2: "))
    d2 = int(input("Pleae enter the day for data 2: "))
    data2 = Data(y2,m2,d2)
        

result = data1.sub(data2)
result.show()   
result = data1.add(data2)
result.show()

    