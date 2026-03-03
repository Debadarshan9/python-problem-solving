# Find second largest in an array

# 1. Without sorting
def second_largest(arr):

    if len(arr) < 2:
        return None

    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second


arr = list(map(int, input("Enter a list of numbers: ").split()))
print("Second largest number is ", second_largest(arr))


# 2. With the help of sorting
unique = sorted(set(arr))
if len(unique) < 2:
    print("No second largest no is present.")
else:

    print("Second largest number is ", unique[-2])
