def binary_search(arr, l, r, x):
    while l <= r:
        m = (r + l) // 2
        if arr[m] == x:
            return m
        if arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

arr = [2, 3, 4, 10, 40]
x = 4
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

