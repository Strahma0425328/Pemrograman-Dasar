# Array 1D
arr_1d = [1, 2, 3, 4, 5]

# Operasi dasar
print("Array 1D:", arr_1d)
print("Elemen indeks 2:", arr_1d[2])  # Output: 3
arr_1d.append(6)  # Tambah elemen
print("Setelah append:", arr_1d)  # Output: [1, 2, 3, 4, 5, 6]

# Iterasi
for i in arr_1d:
    print(i, end=" ")  # Output: 1 2 3 4 5 6

# Array 2D (3x3)
arr_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Operasi dasar
print("Array 2D:")
for row in arr_2d:
    print(row)  # Output: [1, 2, 3] dll.

print("Elemen baris 1, kolom 2:", arr_2d[1][2])  # Output: 6
arr_2d[0].append(10)  # Tambah ke baris pertama
print("Setelah append:", arr_2d[0])  # Output: [1, 2, 3, 10]

# Iterasi
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        print(f"arr_2d[{i}][{j}] = {arr_2d[i][j]}")


# Array 3D (2x2x2)
arr_3d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

# Operasi dasar
print("Array 3D:")
for layer in arr_3d:
    for row in layer:
        print(row)  # Output: [1, 2] dll.

print("Elemen layer 1, baris 0, kolom 1:", arr_3d[1][0][1])  # Output: 6
arr_3d[0][0].append(9)  # Tambah ke layer pertama, baris pertama
print("Setelah append:", arr_3d[0][0])  # Output: [1, 2, 9]

# Iterasi
for i in range(len(arr_3d)):
    for j in range(len(arr_3d[i])):
        for k in range(len(arr_3d[i][j])):
            print(f"arr_3d[{i}][{j}][{k}] = {arr_3d[i][j][k]}")
