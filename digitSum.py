# Sum of digits of a number

# 1. Using math method
def sumOfDigits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total


x = int(input("Enter a number: "))
print(f"Sum of digits of {x} is {sumOfDigits(x)}")


# 2. Using recursion
def sumOfDigitsRecursion(num):
    if num == 0:
        return 0
    return num % 10 + sumOfDigitsRecursion(num // 10)


y = int(input("Enter a number: "))
print(f"Sum of digits of {y} is {sumOfDigitsRecursion(y)}")
