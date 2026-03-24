def kmToMiles(km):
    return km*0.621371
def kgToPounds(kg):
    return kg*2.20462
def celToFar(cel):
    return c*9/5+32
val=float(input("Enter value: "))
conType=int(input("1-Distance 2-weight 3-Temp "))
if(conType==1):
    res=kmToMiles(val)
    print(f"{val} km in miles is {res} ")
elif(conType==2):
    res=kgToPounds(val)
    print(f"{val} kg in pounds is {res} ")
elif(conType==3):
    res=celToFar(val)
    print(f"{val} cel in fahrenheit is {res} ")
else:
    print("Invalid type")