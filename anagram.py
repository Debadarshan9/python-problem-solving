# Check anagram

# 1. Dictonary method
def is_anagram_dict(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    if len(str1) != len(str2):
        return False

    count = {}

    for ch in str1:
        count[ch] = count.get(ch, 0) + 1

    for ch in str2:
        if ch not in count:
            return False

        count[ch] -= 1
        if (count[ch] < 0):
            return False

    return True


str1, str2 = map(str, input("Enter two word: ").split())
if (is_anagram_dict(str1, str2)):
    print("The given words are anagram")
else:
    print("The given words are not anagram")


# 2. using sorted() method
word1, word2 = map(str, input("Enter 2 words: ").split())
if (sorted(word1.lower())) == sorted(word2.lower()):
    print("The given words are anagram.")
else:
    print("The given words are not anagram.")
