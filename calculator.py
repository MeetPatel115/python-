class calculator:
    def __init__(self):
        print("calaculator has been started")

    def cube(self,value):
        return value**3
    def sqaure(self,value):
        return value**2
    def sqrt(self,value):
        return value**(1/2)
    
    def choice(self,value, slec):
        if slec=='s':
            print(self.sqaure(value))
        elif slec=='r':
            print(self.sqrt(value))
        else:
            print(self.cube(value))

cal=calculator()

cal.choice(4,'s')
cal.choice(4,'r')
cal.choice(4,'')