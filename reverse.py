def reverseWord(string):
    array = string.strip().split(" ")[::-1]
    return " ".join(array);

print(reverseWord("What a time to be alive"))
    