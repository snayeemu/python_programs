#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(a):
    reverse_array = []
    for i in range(len(a)):
        reverse_array.append(a[-(i + 1)])
    return reverse_array


