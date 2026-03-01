# GCD ofTwo Numbers

# 1. For loop
def gcd(num1, num2):
    minimum = min(num1, num2)
    for i in range(minimum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


x, y = map(int, input("Enter 2 numbers: ").split())
print(gcd(x, y))


# 2.Euclidian Method
def euclidian(num1, num2):
    num1, num2 = abs(num1), abs(num2)
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


a, b = map(int, input("Enter 2 numbers: ").split())
print(euclidian(a, b))
