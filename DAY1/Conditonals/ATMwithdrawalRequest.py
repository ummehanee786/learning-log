balance=int(input("balance : "))
amount=int(input("amount :"))
acc_type=int(input("for (saving)1 or (current) 2 :"))
if amount >50000:
    print("Exceeds maximum limit")
elif amount % 100 !=0:
    print("not a multiple of 100")
elif acc_type == 1:
    if balance - amount < 500 :
        print("insufficient balance")
    else:
        balance -= amount
        print("success, balance=", balance)
else:
    fee =50 if amount > 25000 else 0
    balance -= amount +fee
    print("success, balance=", balance)
