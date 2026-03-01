# Reverse a number

# 1. Not Converting to string
def revNum(num):
    result = 0
    sign = -1 if num < 0 else 1
    num = abs(num)
    while num > 0:
        digit = num % 10
        num = num // 10
        result = 10 * result + digit
    return sign * result


x = int(input("Enter a number: "))
print(f"Reverse of {x} is {revNum(x)}")


# 2. By Converting string
def reverseNum(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    return sign * int(str(num)[::-1])


x = int(input("Enter a number: "))
print(f"Reverse of {x} is {reverseNum(x)}")
