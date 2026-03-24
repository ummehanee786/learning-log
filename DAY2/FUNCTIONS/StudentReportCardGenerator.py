def calAverage(marks):
    return sum(marks)/len(marks)
    
def gradeFind(avg):
    if(avg>=90):
        return "A+"
    elif(avg>=80):
        return "A"
    elif(avg>=70):
        return "B"
    elif(avg>=60):
        return "C"
    elif(avg>=50):
        return "D"
    else:
        return "F"
        
def checkPass(grade):
    if(grade=="F"):
        return False
    else:
        return True
        
def report(name,marks):
    avg=calAverage(marks)
    grade=gradeFind(avg)
    status=checkPass(grade)
    print("----REPORT----")
    print(f"Name is {name} ")
    print(f"Marks is {marks}")
    print(f"Average is {avg} ")
    print(f"Grade is {grade} ")
    print(f"Did you pass? {status} ")
    
name=input("Enter name: ")
marks=list(map(int,input("Enter marks ").split()))
report(name,marks)