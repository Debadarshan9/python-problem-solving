# Palindrome Number

def palindromeNumber(num):
    original = num
    reversedNum = 0
    while num > 0:
        digit = num % 10
        reversedNum = reversedNum * 10 + digit
        num //= 10

    return reversedNum == original


x = int(input("Enter a number: "))

if palindromeNumber(x):
    print(f"{x} is a palindrome number.")
else:
    print(f"{x} is not a palindrome number.")
