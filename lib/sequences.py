#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        result = []
        print(result)
    elif length == 1:
        result = [0]
        print(result)
    elif length == 2:
        result = [0, 1]
        print(result)
    else:
        i = 3
        result = [0, 1]
        while i <= length :
            result.append(result[i-3]+result[i-2])
            i += 1
        print(result)


