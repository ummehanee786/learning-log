num = int(input("Enter a number: "))
iterations = 0
n = num

while n > 9:  # keep going until n is a single digit
    s = 0
    while n != 0:
        rem = n % 10
        s += rem
        n //= 10
    n = s
    iterations += 1

print(f"final answer {n}")
print(f"iterations {iterations}")