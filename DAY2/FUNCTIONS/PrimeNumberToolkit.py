def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
    
def primesInRange(start,end):
    res=[]
    for n in range(start,end+1):
        if(isPrime(n)):
            res.append(n)
    return res
    
def primeFactor(n):
    li=[]
    factors=[]
    for i in range(2,n+1):
        if(n%i==0):
            li.append(i)
    for j in li:
        if(isPrime(j)):
            factors.append(j)
    return factors
start=int(input("Enter lower bound: "))
end=int(input("Enter upper bound: "))
num=int(input("enter a num: "))
res=primesInRange(start,end)
print(f"Prime nos bw {start} to {end} are {res}")
fac=primeFactor(num)
print(f"Prime factors of {num} are {fac}")

