# Fibonacci Series (First N Terms)

# 1. Using for loop

def fibFor(num):
    a, b = 0, 1
    for i in range(1, num+1):
        print(a, end=" ")
        a, b = b, a+b


x = int(input("Enter a number: "))
print("Fibonacci Series: ", end=" ")
fibFor(x)

# Using while loop


def fibWhile(num):
    a, b = 0, 1
    count = 0
    while count < num:
        print(a, end=" ")
        a, b = b, a+b
        count += 1


y = int(input("Enter a number: "))
print("Fibonacci Series: ", end=" ")
fibWhile(y)
