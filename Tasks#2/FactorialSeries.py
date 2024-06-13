num = int(input("Enter a number for factorial Series \n"))
fact = 1

if num <= 0:
    print("Invalid number")
elif num == 1:
    print("Factorial Series:", num,)
else:
    for i in range(1, num+1):
        fact = fact * i

print("Factorial of", num, "is:", fact)
