#! python3

import fileinput


def spongify(s):
    output = ""
    for i in range(len(s)):
        if i%2 == 0:
            output += s[i].upper()
        else:
            output += s[i].lower()

    return output

for i in fileinput.input():
    print(spongify(i),end='')


