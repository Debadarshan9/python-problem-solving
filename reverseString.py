#  Reverse a string

# 1. Simple slicing approach
string = input("Enter a word: ")
print("Reverse of the given word is ", string[::-1])


# 2. Foor loop
string2 = input("Enter a word: ")
rev = ""

for ch in string2:
    rev = ch + rev
print("Reverse of the given word is ", rev)
