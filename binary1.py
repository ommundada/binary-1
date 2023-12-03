import random

def binary_search(list, key):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

list = random.sample(range(10000), 5000)

key = int(input("Enter the key element to search for: "))

index = binary_search(list, key)

if index != -1:
    print("The key element", key, "is found at index", index)
else:
    print("The key element", key, "is not found in the list")
