in_string = "locate the fiFle"

char_dict = {}
for i in in_string:
    char_dict[i] = char_dict.get(i) + 1 if i in char_dict else 1

print(*iter(char_dict.keys()))
print (char_dict)