# LCM of 2 numbers

# 1. Simple loop method
def lcmLoop(num1, num2):
    if (num1 == 0 or num2 == 0):
        return 0
    num1, num2 = abs(num1), abs(num2)
    maxNum = max(num1, num2)
    multiple = maxNum
    count = 1
    while True:
        if (multiple % num1 == 0 and multiple % num2 == 0):
            return multiple
        count += 1
        multiple = maxNum * count


x, y = map(int, input("Enter 2 numbers: ").split())
print(f"LCM of {x} and {y} is {lcmLoop(x,y)}")


# 2. (a,b) / gcd(a,b)
def lcmFormula(num1, num2):
    mul = abs(num1*num2)
    if (mul == 0):
        return 0
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return mul // num1


a, b = map(int, input("Enter 2 numbers: ").split())
print(f"LCM of {a} and {b} is {lcmFormula(a,b)}")
