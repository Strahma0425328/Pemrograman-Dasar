# Binary search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
# Contoh penggunaan
arr = [1, 3, 5, 7, 9]
print(binary_search_recursive(arr, 5, 0, len(arr)-1))  # Output: 2
print(binary_search_recursive(arr, 10, 0, len(arr)-1))  # Output: -1

# interpolitan search
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        
        # Hitung posisi interpolasi
        pos = low + int(((x - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1
