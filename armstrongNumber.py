# Check Armstrong Number

def isArmstrong(num):
    original = num
    length = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** length
        num //= 10

    return original == total


x = int(input("Enter a number: "))
if (isArmstrong(x)):
    print(f"{x} is an armstrong number.")
else:
    print(f"{x} is not an armstrong number.")
