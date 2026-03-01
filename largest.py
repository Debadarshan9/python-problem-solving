# Largest of Three Numbers

def largestAmongThree(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num3):
        return num2
    else:
        return num3


x, y, z = map(int, input("Enter 3 numbers: ").split())
print(largestAmongThree(x, y, z))
