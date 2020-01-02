# author @igmerwina
# get_data.py

''' 
get_data.py digunakan untuk:
1. Membuat koneksi ke database
2. Membuat table yang dibutuhkan ke database 
3. Menghilangkan delimiter (pipe) pada file txt
4. Import data txt ke dalam db 
'''

# import libary sqlite3
import sqlite3

# membuat koneksi sqlite dengan nama db: database.db
conn = sqlite3.connect("database.db")
# cursor() digunakan untuk eksekusi sql command
cur = conn.cursor()
# eksekusi sql command untuk membuat table data_diri dengan 4 column
cur.execute("CREATE TABLE data_diri (no_ktp, nama, jenis_kelamin, alamat);")

# membuka file data.txt dengan mode akses read
with open(r'data.txt', 'r') as infile:
    data = infile.read()
    # menghapus pipe untuk mengambil data pada file txt
    data = data.replace("|", "")

# membagi data pada file txt menjadi baris kalimat
# contoh baris pertama: 1267062810912302 Erwin Pria Jakarta
row = data.split('\n')  

# Fungsi formated digunakan untuk memecah setiap baris kalimat 
# menjadi array yang berisi kata-kata
# contoh: ['1267062810912302',	'Erwin',	'Pria',	'Jakarta']
# tuple merupakan kumpulan data yang tidak bisa diubah 
# x.split digunakan untuk memecah kalimat menjadi kata
# sedangkan for x in row merupakan pengulangan tiap kata pada baris kalimat
formatted = [tuple(x.split()) for x in row]

# eksekusi perintah sql untuk insert data per kata ke dalam table data_diri
cur.executemany(
    "INSERT INTO data_diri (no_ktp, nama, jenis_kelamin, alamat) VALUES (?, ?, ?, ?)", formatted)
# commit perintah sql ke db
conn.commit() 
# menutup koneksi dengan database 
conn.close() 

# done!
