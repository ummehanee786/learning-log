L=int(input("enter lower bound: "))
R=int(input("enter upper bound: "))
flag=False
for n in range(L,R+1):
    num=str(n)
    count=len(num)
    total=0
    for d in num:
        total+=int(d)**count
    if(total==n):
        print(n)
        flag=True
if not flag:
    print("No Armstrong no. found")
