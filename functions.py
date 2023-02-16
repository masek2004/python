def hello():
    print("this is my first function")
hello()
hello()
hello()
def calculate():
    x=10
    y=30
    print(x*y)
calculate()


def names(fname,lname):
    print(fname+" "+lname)
names("masek ", "msm")
names("marcus ", "garvey")
names("mark ", "alex")

def greetings(name, greetings="hello"):
    print(greetings +" "+ name)
greetings("masek")
greetings("niaje","sean")
def ukoaje(names, name="my name is"):
    print(name +" "+ names)
ukoaje("masek")
def age(name, age="i am"):
    print(age +" "+ name)
age("18 yrs")

#function to sort max value
def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,4,3,2,4,5)
print(result)
#function to sort minimum value
def minval(e,r,t,y,u,):
    return min(e,r,t,y,u)
result=minval(3,4,5,6,7)
print(result)
#function to sort a list
def sort_list(list):
    return sorted(list)
answer=sort_list([3,4,15,9,8,6])
print(answer)
#funcion to print out numbers
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(2500)