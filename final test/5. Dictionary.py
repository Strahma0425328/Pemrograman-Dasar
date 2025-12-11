# Membuat dictionary
mahasiswa = {
    "nama": "Rahma",
    "nim": "D0425328",
    "jurusan": "Sistem Informasi"
}

# Menambah
mahasiswa["semester"] = 3

# Mengupdate
mahasiswa["nama"] = "St rahma"

# Menghapus
mahasiswa.pop("nim")

# Looping
for k, v in mahasiswa.items():
    print(k, ":", v)
