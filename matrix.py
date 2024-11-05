import numpy as np

# Definisi matriks menggunakan numpy
A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Operasi perkalian dan penjumlahan
hasil_A_C = np.matmul(A, C)
hasil_A_B = np.matmul(A, B)
hasil_D_plus_E = np.add(D, E)
hasil_D_minus_E = np.subtract(D, E)

# Menguji operasi perkalian yang akan menyebabkan error
try:
    hasil_A_D = np.matmul(A, D)
    print("Hasil dari A x D:")
    print(hasil_A_D)
except ValueError as error:
    print("Error pada operasi A x D:", error)

# Mencetak hasil operasi
print("Hasil dari A x C:")
print(hasil_A_C)
print("Hasil dari A x B:")
print(hasil_A_B)
print("Hasil dari D + E:")
print(hasil_D_plus_E)
print("Hasil dari D - E:")
print(hasil_D_minus_E)

# Implementasi tanpa library numpy
A = [[3, 0], [-1, 2], [1, 1]]
B = [[4, -1], [0, 2]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

# Fungsi untuk perkalian matriks
def kali_matriks(M1, M2):
    if len(M1[0]) != len(M2):
        raise ValueError("Ukuran matriks tidak cocok untuk perkalian.")
    return [[sum(M1[i][k] * M2[k][j] for k in range(len(M2))) for j in range(len(M2[0]))] for i in range(len(M1))]

# Fungsi untuk penjumlahan matriks
def tambah_matriks(M1, M2):
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

# Fungsi untuk pengurangan matriks
def kurangi_matriks(M1, M2):
    return [[M1[i][j] - M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

# Melakukan operasi sesuai dengan instruksi
hasil_A_C = kali_matriks(A, C)
hasil_A_B = kali_matriks(A, B)
hasil_D_plus_E = tambah_matriks(D, E)
hasil_D_minus_E = kurangi_matriks(D, E)

# Menguji operasi yang menyebabkan error
try:
    hasil_A_D = kali_matriks(A, D)
    print("Hasil dari A x D:", hasil_A_D)
except ValueError as error:
    print("Error pada operasi A x D:", error)

# Menampilkan hasil akhir
print("Hasil dari A x C:", hasil_A_C)
print("Hasil dari A x B:", hasil_A_B)
print("Hasil dari D + E:", hasil_D_plus_E)
print("Hasil dari D - E:", hasil_D_minus_E)
