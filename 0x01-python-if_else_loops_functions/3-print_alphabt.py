#!/usr/bin/python3
for alph in range(97, 123):
    if chr(alph) != 101 and chr(alph) != 113:
        print("{}".format(chr(alph)), end="")
