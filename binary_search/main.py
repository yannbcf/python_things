import warnings

def is_list_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True

def binary_search(ascending_list: list, target: int, check_ascending = False) -> int:
    if check_ascending and not is_list_ascending(ascending_list):
        warnings.warn("The list provided is not in ascending order. We fixed it for you.", category=UserWarning)
        ascending_list.sort()

    l = 0
    r = len(ascending_list)
   
    while l <= r:
        m = (l + r) // 2
        if ascending_list[m] < target:
            l = m + 1
        elif ascending_list[m] > target:
            r = m - 1
        else:
            return m

    return -1
