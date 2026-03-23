day =int(input(" 1-7 , 1 is monday : "))
show_time = int(input("Input in 24H format: "))
age = int(input("enter your age: "))
seat_type = int(input("1 -3, 1(Regular), 2(premium), 3(Recliner): "))
base_price = 200
if 1 <= day <= 4:
    weekday_discount = base_price*0.20
else:
    weekday_discount=0.0
after_weekday_discount=base_price - weekday_discount
if age < 12 or age > 60:
    age_discount = after_weekday_discount *0.30
else:
    age_discount=0.0
after_age_discount = after_weekday_discount - age_discount
if seat_type == 1:
    surcharge = 0
elif seat_type == 2:
    surcharge = 150
else:
    surcharge = 250
subtotal = after_age_discount + surcharge
if subtotal > 500:
    gst_rate= subtotal *0.10
else:
    gst_rate = subtotal * 0.12

grand_total = subtotal + gst_rate
print("grand total you have to pay is : ", grand_total)
print(f"grand total you have to pay is :  {grand_total:.2f}")