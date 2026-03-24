n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(j<n-1-i):
            print(" ",end="")
        else:
            print("*",end="")
    print('\n')