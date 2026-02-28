# Factorial Of a Number

# 1. Using Form Loop
def factorialFor(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i

    return fact


x = int(input("Enter a number:"))
print(f"Factorial of {x} is {factorialFor(x)}")

# 2. Using while Loop


def factorialWhile(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact


y = int(input("Enter a number:"))
print(f"Factorial of {y} is {factorialWhile(y)}")

# 3. Using recursion


def factorialRecursion(num):
    if num == 0 or num == 1:
        return 1

    return num * factorialRecursion(num-1)


z = int(input("Enter a number:"))
print(f"Factorial of {z} is {factorialRecursion(z)}")
