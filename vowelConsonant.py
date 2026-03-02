# Count Vowels and Consonants

# 1. Simple approach
def count_basis(word):
    word = word.lower()
    vowels = "aeiou"
    v = 0
    c = 0
    for i in word:
        if i.isalpha():
            if (i in vowels):
                v += 1
            else:
                c += 1
    return v, c


string1 = input("Enter a word: ")
vowels1, consonants1 = count_basis(string1)
print("vowels: ", vowels1)
print("Consoants: ", consonants1)


# 2. filter() approach
def count_filter(word):
    word = word.lower()
    vowel = "aeiou"
    letters = list(filter(str.isalpha, word))
    v = len(list(filter(lambda x: x in vowel, letters)))
    c = len(letters) - v
    return v, c


string2 = input("Enter a word: ")
vowels2, consonants2 = count_filter(string2)
print("vowels: ", vowels2)
print("Consoants: ", consonants2)


# 3. Using dictonary
def count_dict(word):
    word = word.lower()
    vowel = "aeiou"

    count = {"vowels": 0, "consonants": 0}

    for i in word:
        if i.isalpha():
            if i in vowel:
                count["vowels"] += 1
            else:
                count["consonants"] += 1
    return count


string3 = input("Enter a word: ")
counts = count_dict(string3)
print("vowels: ", counts["vowels"])
print("Consoants: ", counts["consonants"])
