# Linear Search

def linear_search(arr, num):
    l = []
    for i in range(len(arr)):
        if (arr[i] == num):
            l.append(i + 1)

    return l


arr = list(map(int, input("Enter a list of numbers: ").split()))
num_to_search = int(input("Enter the number to search in above list: "))
result = linear_search(arr, num_to_search)

if len(result) == 0:
    print(f"{num_to_search} is not found.")
else:
    print(f"{num_to_search} is found at {', '.join(map(str,result))} positions.")
