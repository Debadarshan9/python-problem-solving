# Even or Odd

# 1. Using % operator
num = int(input("Enter a number: "))

if (num % 2 == 0):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


# 2. Using bitwise and (&) operator
num2 = int(input("Enter a number: "))

if (num2 & 1 == 0):
    print(f"{num2} is an even number.")
else:
    print(f"{num2} is odd number.")
