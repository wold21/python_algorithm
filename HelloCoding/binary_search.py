def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_arr = [1, 3, 5, 7, 9, 12, 15, 17, 19, 21]
print(binary_search(my_arr, 12))