#! python3

import sys
import random

def spongify(s):
    output = ""
    for i in range(len(s)):
        if i%2 == 0:
            output += s[i].upper()
        else:
            output += s[i].lower()

    return output

def sponge_real(s):
    output = ""
    for i in range(len(s)):
        if random.randint(0,1):
            output += s[i].upper()
        else:
            output += s[i].lower()

    return output

def usage_text():
    print("""
Usage:
    python3 spongePy.py [option] < [input-file] > [output-file]

    [option]
        -r : To activate realistic mode instead of normal (default) mode

    Everything after that is optional.

    If you'd like to use the samples, set [input-file] to sample-inputs/[filename].
""")

def do_the_thing(function_name):
    while True:
        try:
            print(function_name(input()))
        except EOFError:
            break


if len(sys.argv) == 2 and sys.argv[1] == '-r' :
    do_the_thing(sponge_real)
elif len(sys.argv) == 2:
    print("Input Error : Please recheck command.")
    # add usage text
else:
    do_the_thing(spongify)

