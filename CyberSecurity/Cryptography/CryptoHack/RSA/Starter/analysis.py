flag = "lpqwmarwsywpqaauadrrqfcfkqwueyifwoxlkvxawjhpkbgrzf" # We strip all special characters from the flag
key = "eginni" # This is for the first iteration, replace if neccessary
for i in range(len(flag) - len(key)):
    test = flag[i:i+len(key)]
    res = ""
    for j in range(len(key)):
        if (not (97 <= ord(test[j]) <= 122)):
            res += test[j]
            continue
        letter = ord(test[j]) - ord(key[j])
        if (letter < 0):
            letter += 26
        res += chr(letter + 97)
    print(res) # This prints out all possible results, choose the most reasonable one