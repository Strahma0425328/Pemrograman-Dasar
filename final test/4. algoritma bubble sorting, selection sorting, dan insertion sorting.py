# bubble sorting
def bubble_sort(arr):
    n = len(arr)
    # Loop untuk setiap elemen
    for i in range(n):
        # Loop untuk membandingkan elemen bersebelahan
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar elemen jika urutannya salah
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:", arr)
bubble_sort(arr)
print("Array setelah diurutkan:", arr)


# selection sorting
def selection_sort(arr):
    n = len(arr)
    # Loop untuk setiap posisi
    for i in range(n):
        # Temukan indeks elemen terkecil di subarray arr[i..n-1]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Tukar elemen terkecil dengan elemen di posisi i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Contoh penggunaan
arr = [64, 25, 12, 22, 11]
print("Array sebelum diurutkan:", arr)
selection_sort(arr)
print("Array setelah diurutkan:", arr)


# insertion sorting
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # elemen yang akan ditempatkan
        j = i - 1

        # Geser elemen arr[j] yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Tempatkan key di posisi yang tepat
        arr[j + 1] = key

    return arr


# Contoh pemakaian
data = [12, 5, 3, 19, 1]
print("Sebelum sorting:", data)
print("Setelah sorting:", insertion_sort(data))
