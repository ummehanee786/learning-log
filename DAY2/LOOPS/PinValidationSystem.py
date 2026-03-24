correctpin=1234
maxAt=3
for at in range(1,maxAt+1):
    pin=int(input("enter PIN: "))
    if(pin==correctpin):
        print("ACCESS GRANTED")
        break
    else:
        remAt=maxAt-at
        if(remAt>0):
            print(f"INCORRECT, {remAt} remaining attempts")
        else:
            print("ACCOUNT BLOCKEDs")
