#!/usr/bin/python3
def add(arr):
    sumi = 0
    for x in arr:
        sumi += x
    print(sumi)


if __name__ == "__main__":
    import sys

    arr = []
    input = sys.argv
    for x in range(1, len(input)):
        arr.append(int(input[x]))
    add(arr)
