import connect

db = connect.koneksi()
#menambahkan data baru ke dalam tabel pegawai
def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO pelanggan(nama_pelanggan,alamat_pelanggan,email_pelanggan)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Pelanggan berhasil ditambah!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel pegawai
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM pelanggan"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print('---------------------------------------------------------')
    print("| ID | NAMA\t\t| ALAMAT\t\t| EMAIL PELANGGAN\t\t")
    print('---------------------------------------------------------')
    for data in results:
        print("|",data[0]," |",data[1],"\t\t|",data[2],"\t\t\t\t|",data[3],"\t\t|")
        print('---------------------------------------------------------')

#mengubah data per record berdasarkan id pada tabel pegawai
def edit(data):
    cursor = db.cursor()
    sql = """UPDATE Pelanggan SET nama_pelanggan=%s,alamat_pelanggan=%s,email_pepelanggan=%s WHERE id_pelanggan=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Pelanggan berhasil diubah!'.format(cursor.rowcount))

#menghapus data dari tabel pegawai
def delete(data):
    cursor = db.cursor()
    sql="""DELETE FROM pelanggan WHERE id_pelanggan=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Pelanggan berhasil dipecat!'.format(cursor.rowcount))

#mencari data dari tabel pegawai
def search(id_pelanggan):
    cursor = db.cursor()
    sql="""SELECT*FROM pelanggan WHERE  id_pelanggan=%s"""
    cursor.execute(sql,id_pelanggan)
    results = cursor.fetchall()
    print("------------------------------------------------")
    print("|ID|NAMA\t\t ALAMAT\t\t EMAIL PELANGGAN\t\t")
    print("------------------------------------------------")
    for data in results:
        print("|",data[0],"|",data[1],"\t\t",data[2],"\t\t",data[3],"\t\t|")
        print('----------------------------------------')
