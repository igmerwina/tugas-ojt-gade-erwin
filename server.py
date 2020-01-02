# @author igmerwina
# server.py 
'''
server.py digunakan untuk: 
1. menampilkan data yang telah diinsert ke db ke dalam tampilan web
2. Web dibangun menggunakan framework flask. 
'''

# import library flask & sqlite3 
from flask import Flask, render_template
import sqlite3

# app digunakan untuk inisialisasi penggunaan modul2 yang ada di flask
app = Flask(__name__)

# routing:home menggunakan alamat ('/')
@app.route("/")
def home(): # nama fungsi yang digunakan untuk memanggil data (nama bisa bebas)
    conn = sqlite3.connect("database.db") # koneksi ke db
    cur = conn.cursor() # cursor() digunakan untuk mengeksekusi perintah di db
    cur.execute("SELECT * FROM data_diri")   # eksekusi query select * from table
    rows = cur.fetchall() # mengambil semua record data pada table & menyimpan ke variable rows
    
    # mempassing data pada db ke index.html melalui variable rows
    return render_template("index.html", rows=rows)


# syntax pada python untuk menjalankan main method
if __name__ == "__main__":
    app.run(debug=True)

# done!