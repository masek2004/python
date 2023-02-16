class emobilisstudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
            print(f"my name is {self.name} and is {self.age} years old")
#creating an object
myoj=emobilisstudent("masek", 18)
myoj.hello_me()

class me:
    def __init__(self, name, height):
        self.name=name
        self.height=height
    def abtme(self):
        print(f"i am {self.name} and i am {self.height} tall")
#object
myobj=me("masek", "6ft")
myobj.abtme()
myobj=me("marcus", "4ft")
myobj.abtme()
myobj=me("mark","3ft")
myobj.abtme()
myobj=me("timo","2ft")
myobj.abtme()

#create a class called magari,it should have model,make and year properties
#create min of 3 objects
class magari:
    def __init__(self,name,model,make,year):
        self.name=name
        self.model=model
        self.make=make
        self.year=year
    def cars(self):
        print(f"hi i am {self.name} and i have a {self.model} {self.make} made in {self.year}")
#object
myobj=magari("masek", "toyota","premio", 2017)
myobj.cars()
myobj=magari("marcus","toyota","corolla",2015)
myobj.cars()
myobj=magari("timo","mazda","demio",2016)
myobj.cars()

class register:
    def __init__(self,name, age, timearrived):
        self.name=name
        self.age=age
        self.timearrived=timearrived
    def register(self):
        print(f"i'am {self.name} ,{self.age} and i arrived at {self.timearrived}")
#object
myobj=register("masek","18yrs","4:00")
myobj.register()
myobj=register("marcus","18yrs","3:00")
myobj.register()
myobj=register("mark","17yrs","9:30")
myobj.register()
myobj=register("timo", "18yrs", "8:00")
