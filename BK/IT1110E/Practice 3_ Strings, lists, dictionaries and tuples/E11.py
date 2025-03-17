n = int(input())
s = input()
result = ""
if (n > 26): n = n%26
for char in s:
    if(char != ' '): 
        if (ord(char) + n > 122):
            result += chr(ord(char) - 26 + n)
        else:
            result += chr(ord(char) + n)
    else:
        result += ' '
print(result)