import sqlite3
koneksi =sqlite3.connect("database_fauna.db")
cursor = koneksi.cursor()
koneksi.execute('''
    CREATE TABLE Fauna(
    id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_fauna VARCHAR(50),
    jenis VARCHAR(50),
    asal VARCHAR(50),
    jml_skrng INTEGER(50),
    thn_ditemukan INTEGER(50)
    )
''')
print("Database dan Tabel Berhasil Di Buat")
koneksi.close()