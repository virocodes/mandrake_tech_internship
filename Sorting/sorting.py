def bubble_sort(arr):
    l = len(arr)
    for _ in range(l-1):
        swap = False
        for j in range(l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap: break
    return arr

def quick_sort(arr):

    if not arr: return arr
    if len(arr) == 1: return arr
    
    if len(arr) == 2:
        if arr[0] > arr[1]: 
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    pivot = arr[-1]
    mid = 0
    for i in range(len(arr)):
        if arr[i] <= pivot:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1

    return quick_sort(arr[:mid-1]) + [arr[mid-1]] + quick_sort(arr[mid:])

