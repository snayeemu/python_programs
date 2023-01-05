#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(given_string):
    result = ""
    for i in range(len(given_string)):
        if i == 0 and given_string[i].isalpha():
            result += given_string[i].upper()
        elif given_string[i].isspace():
            continue
        elif given_string[i - 1].isspace() and given_string[i].isalpha():
            result += " " + given_string[i].upper()
        else:
            result += given_string[i]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    given_string = input()

    result = solve(given_string)



    fptr.write(result + '\n')

    fptr.close()
