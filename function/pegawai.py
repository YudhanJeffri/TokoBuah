import connect

db = connect.koneksi()
#menambahkan data baru ke dalam tabel pegawai
def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO pegawai(nama_pegawai,alamat_pegawai,email_pegawai)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pegawai berhasil ditambah!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel pegawai
def show():
    cursor=db.cursor()
    sql="""SELECT*FroM pegawai"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print('---------------------------------------------------------')
    print("| ID | NAMA\t\t| ALAMAT\t\t| EMAIL PEGAWAI\t\t")
    print('---------------------------------------------------------')
    for data in results:
        print("|",data[0]," |",data[1],"\t\t|",data[2],"\t\t\t\t|",data[3],"\t\t|")
        print('---------------------------------------------------------')

#mengubah data per record berdasarkan id pada tabel pegawai
def edit(data):
    cursor = db.cursor()
    sql = """UPDATE pegawai SET nama_pegawai=%s,alamat_pegawai=%s,email_pegawai=%s WHERE id_pegawai=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data pegawai berhasil diubah!'.format(cursor.rowcount))

#menghapus data dari tabel pegawai
def delete(data):
    cursor = db.cursor()
    sql="""DELETE FROM pegawai WHERE id_pegawai=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Pegawai berhasil dipecat!'.format(cursor.rowcount))

#mencari data dari tabel pegawai
def search(id_pegawai):
    cursor = db.cursor()
    sql="""SELECT*FROM pegawai WHERE id_pegawai=%s"""
    cursor.execute(sql,id_pegawai)
    results = cursor.fetchall()
    print("------------------------------------------------")
    print("|ID|NAMA\t\t ALAMAT\t\t EMAIL PEGAWAI\t\t")
    print("------------------------------------------------")
    for data in results:
        print("|",data[0],"|",data[1],"\t\t",data[2],"\t\t",data[3],"\t\t|")
        print('----------------------------------------')
