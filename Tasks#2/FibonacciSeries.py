num = int(input("Enter a number for fibonacci Series \n"))
num1, num2 = 0, 1
count = 0

if num <= 0:
    print("Invalid number")
elif num == 1:
    print("Fibonacci Series", num, ":", num1)
else:
    print("Fibonacci Series:")
    while count < num:
        print(num1)
        fib = num1 + num2
        num1 = num2
        num2 = fib
        count += 1
