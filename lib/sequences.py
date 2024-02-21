#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        seq = []
    elif length == 1:
        seq = [0]
    else:
        seq = [0, 1]
        for i in range(2, length):
            seq.append(seq[i-1] + seq[i-2])
    print(seq)