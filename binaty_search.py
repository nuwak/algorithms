def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0

    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            print(count)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = range(1, 100)

print(binary_search(my_list, 52))
print(binary_search(my_list, -7))
