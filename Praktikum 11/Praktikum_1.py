# =========================================
# Praktikum 1: Membuat Adjacency Matrix Graph
# Nama      : Azhar Fawwaz Haris
# NIM       : J0403251043 
# Kelas     : TPL A P2
# =========================================

# Fungsi untuk membuat graph dalam bentuk adjacency matrix
def createGraph(v, edges):

    # Membuat matrix berukuran v x v
    # Semua isi awal bernilai 0
    # 0 berarti belum ada hubungan antar vertex
    mat = [[0 for _ in range(v)] for _ in range(v)]

    # Perulangan untuk membaca setiap edge
    for it in edges:

        # Mengambil vertex awal
        u = it[0]

        # Mengambil vertex tujuan
        v = it[1]

        # Mengisi nilai 1 pada posisi [u][v]
        # Artinya vertex u terhubung ke vertex v
        mat[u][v] = 1

        # Karena graph tidak berarah,
        # maka hubungan berlaku dua arah
        # sehingga [v][u] juga bernilai 1
        mat[v][u] = 1

    # Mengembalikan adjacency matrix
    return mat


# Program utama
if __name__ == "__main__":

    # Jumlah vertex/node
    v = 4

    # Daftar edge/sisi pada graph
    # Format: [vertex_awal, vertex_tujuan]
    edges = [
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 3]
    ]

    # Memanggil fungsi createGraph
    # untuk membuat adjacency matrix
    mat = createGraph(v, edges)

    # Menampilkan judul output
    print("Adjacency Matrix : ")

    # Perulangan untuk menampilkan baris matrix
    for i in range(v):

        # Perulangan untuk menampilkan kolom matrix
        for j in range(v):

            # Menampilkan isi matrix
            print(mat[i][j], end = " ")

        # Pindah ke baris baru
        print()