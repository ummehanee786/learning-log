n=int(input("enter no of deliveries: "))
sum=0
for i in range(0,n):
    delivery=int(input())
    sum+=delivery
average=sum/n
print(f"Total is {sum}")
print(f"average is {average}")
