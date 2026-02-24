# Prime Number Check

def isPrime(num):

    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if (num % i == 0):
            return False

    return True


x = int(input("Enter a number: "))
if (isPrime(x)):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is  not a prime number.")
