grade=float(input("enter your grade"))
if grade>=90:
    print("A")
elif grade<=90 and grade>=80:
    print("A-")
elif grade<=80 and grade>=70:
    print("B+")
elif grade<=70 and grade>=60:
    print("B")
elif grade<=60 and grade>=50:
    print("B-")
else:
    print("invalid")
