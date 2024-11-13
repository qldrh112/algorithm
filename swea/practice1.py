def binary_sort(arr, N, k):
    start = 0
    end = N - 1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == k:
            return middle

        elif arr[middle] > k:
            end = middle - 1

        else:
            start = middle + 1

    return False


print(binary_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 8))
