class programmer:

    def __init__(self,name,location,salary,project):
        self.name=name
        self.location=location
        self.salary=salary
        self.project=project
        print(f"The object for {name} has been created")
    
    def increamental(self):
        if self.salary>10000:
            print("This year you get 25 percent increament")
            self.salary+=self.salary*.25
        else:
            print("This year you get 15 percent increament")
            self.salary+=self.salary*.15

    def info(self):
        print(f"Hi, My name is {self.name} and i am working in this project {self.project}. while my current salary is  {self.salary} and I am located at {self.location}.")

meet=programmer("Meet","Ahmedabad",2500000,"Speech translaction")
meet.info()  
meet.increamental()
meet.info()