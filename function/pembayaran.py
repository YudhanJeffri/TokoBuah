import connect
import mysql.connector

db = connect.koneksi()
#menambahkan data baru ke dalam tabel pelanggan
def add (data):
    cursor = db.cursor()
    sql = """INSERT INTO pembayaran(tgl_pembayaran,total_bayar,id_transaksi)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembayaran berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel member
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM pembayaran"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print('---------------------------------------------------------')
    print("| ID PEMBAYARAN | TANGGAL\t\t\t| TOTAL\t\t| ID TRANSAKSI\t\t|")
    print('---------------------------------------------------------')
    for data in results:
        print("|",data[0]," |",data[1],"\t\t\t|",data[2],"\t\t|",data[3],"\t\t|")
        print('---------------------------------------------------------')

#mengubah data per record berdasarkan id pada tabel pelanggan
def edit(data):
    cursor = db.cursor()
    sql = """UPDATE pembayaran SET tgl_pembayaran=%s,total_bayar=%s,id_transaksi=%S WHERE id_pembayaran=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembayaran berhasil diubah!'.format(cursor.rowcount))

#menghapus data dari tabel pelanggan
def delete(data):
    cursor = db.cursor()
    sql="""DELETE FROM pembayaran WHERE id_pembayaran=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pembayaran berhasil dihapus!'.format(cursor.rowcount))

#mencari data dari tabel pelanggan
def search(id_pelanggan):
    cursor = db.cursor()
    sql="""SELECT*FROM pembayaran WHERE id_pembayaran=%s"""
    cursor.execute(sql,id_pelanggan)
    results = cursor.fetchall()
    print("------------------------------------------------")
    print("|ID PEMBAYARAN|TANGGAL\t\t|TOTAL\t\t|ID TRANSAKSI\t\t")
    print("------------------------------------------------")
    for data in results:
        print("|",data[0],"|",data[1],"\t\t",data[2],"\t\t",data[3],"\t\t")
        print('----------------------------------------')
