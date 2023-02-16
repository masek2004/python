#list in python
myclass=["marcus","mark","alex","timo","masek"]
myclass[0]="sylvia"
myclass.append("daniel")
myclass.insert(2, "godfrey")
myclass.append("ariana")
myclass.insert(1, "killy")
myclass[4]="anne"
myclass.sort()
print(type(myclass))
print(myclass)
print("my name is"+ myclass[1])
#tuple in python
myfavfruit=("orange","mango","strawberry","pineapple")
print(myfavfruit)
print(myfavfruit[0])
#set
myfavcars={"toyota","mazda","jeep"}
myfavcars.add("peugeot")
print(myfavcars)
#dictionary in python
cars={
    "name":"toyota",
    "model":"crown",
    "year":2018

}
print(cars)
print(cars["model"])