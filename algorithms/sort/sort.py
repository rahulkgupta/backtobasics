def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    print arr

def merge_sort(arr, beg, end):
    if beg + 1 >= end:
        return
    mid = (beg + end)/2
    merge_sort(arr, beg, mid)
    merge_sort(arr, mid, end)
    left = []
    right = []
    for i in range(beg, mid):
        left.append(arr[i])
    for j in range(mid, end):
        right.append(arr[j])
    i = 0
    j = 0
    for k in range(beg, end):
        if i >= len(left):
            arr[k] = right[j]
            j = j + 1
        elif j >= len(right):
            arr[k] = left[i]
            i = i + 1
        elif left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
    print arr
