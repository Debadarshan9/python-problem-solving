# Remove Duplicates from String

def remove_duplicates_from_string(word):
    result = ""
    result_lower = ""
    for ch in word:
        lower_ch = ch.lower()
        if lower_ch not in result_lower:
            result += ch
            result_lower += lower_ch

    return result


str1 = input("Enter a string: ")
print("After removing duplicate letter: ", remove_duplicates_from_string(str1))


# using set()
def remove_duplicates_from_string_set(word):
    seen = set()
    result = ""
    for ch in word:
        lower_ch = ch.lower()
        if lower_ch not in seen:
            seen.add(lower_ch)
            result += ch
    return result


str2 = input("Enter a string: ")
print("After removing duplicate letter: ",
      remove_duplicates_from_string_set(str2))
