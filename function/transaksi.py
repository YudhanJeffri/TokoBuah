import connect

db = connect.koneksi()

def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO transaksi(id_buah, id_pelanggan, id_pegawai,keterangan)VALUES(%s,%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Transaksi berhasil ditambah!'.format(cursor.rowcount))

def show():
    cursor=db.cursor()
    sql="""SELECT*FROM transaksi"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print('-----------------------------------------------------------------------------------------------------------------')
    print("| ID | ID BUAH\t| ID PELANGGAN\t| ID PEGAWAI\t| TANGGAL\t| KETERANGAN\t\t\t|")
    print('-----------------------------------------------------------------------------------------------------------------')
    for data in results:
        print("|",data[0]," |",data[1],"\t\t|",data[2],"\t\t\t|",data[3],"\t\t|",data[4],"\t\t\t|",data[5],"\t\t\t|")
        print('-----------------------------------------------------------------------------------------------------------------')

def edit(data):
    cursor = db.cursor()
    sql = """UPDATE transaksi SET id_buah=%s,id_pelanggan=%s,id_pegawai=%s,keterangan=%s WHERE id_transaksi=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data berhasil diubah!'.format(cursor.rowcount))

def edit_keterangan(data):
    cursor = db.cursor()
    sql = """UPDATE transaksi set keterangan=%s WHERE id_transaksi=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Keterangan Transaksi diubah!'.format(cursor.rowcount))

def delete(data):
    cursor = db.cursor()
    sql="""DELETE FROM transaksi WHERE id_transaksi=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Transaksi berhasil dihapus!'.format(cursor.rowcount))

def search(id_transaksi):
    cursor = db.cursor()
    sql="""SELECT*FROM transaksi WHERE id_transaksi=%s"""
    cursor.execute(sql,id_transaksi)
    results = cursor.fetchall()
    print('-----------------------------------------------------------------------------------------------------------------')
    print("| ID | ID BUAH\t| ID PELANGGAN\t| ID PEGAWAI\t| TANGGAL\t\t\t| KETERANGAN\t\t\t|")
    print('-----------------------------------------------------------------------------------------------------------------')
    for data in results:
        print("|", data[0], " |", data[1], "\t\t|", data[2], "\t\t\t|", data[3], "\t\t\t\t|", data[4], "\t\t\t|", data[5],"\t\t\t|")
        print('-----------------------------------------------------------------------------------------------------------------')