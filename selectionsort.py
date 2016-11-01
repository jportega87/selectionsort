import random

def selectionSort(arr):
    min = arr[0]
    subtrack = 0

    while subtrack < (len(arr) - 1):
        for i in range(subtrack, len(arr)):
            if min > arr[i]:
                min = arr[i]
        for i in range(subtrack, len(arr)):
            if min == arr[i]:
                arr[i] = arr[subtrack]
                arr[subtrack] = min
        subtrack += 1
        min = arr[subtrack]
    return arr

count = 0
x = []

while count < 10:
    x.append(random.randint(0, 10000))
    count += 1

x = selectionSort(x)
print x
