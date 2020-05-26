import connect

db = connect.koneksi()

def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO buah(nama_buah,jumlah_buah,status_buah,harga_satuan,jenis_buah,id_supplier)VALUES(%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Buah berhasil ditambah!'.format(cursor.rowcount))

def show():
    cursor=db.cursor()
    sql="""SELECT*FROM buah"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print('-----------------------------------------------------------------------------------------------------------------')
    print("| ID | NAMA BUAH\t| JUMLAH BUAH\t| STATUS BUAH\t| HARGA SATUAN/Kg\t| JENIS BUAH\t\t\t| ID SUPPLIER\t|")
    print('-----------------------------------------------------------------------------------------------------------------')
    for data in results:
        print("|",data[0]," |",data[1],"\t\t|",data[2],"\t\t\t|",data[3],"\t\t|",data[4],"\t\t\t|",data[5],"\t\t|",data[6],"\t\t\t|")
        print('-----------------------------------------------------------------------------------------------------------------')

def edit(data):
    cursor = db.cursor()
    sql = """UPDATE buah SET nama_buah=%s,jumlah_buah=%s,status_buah=%s,harga_satuan=%s,jenis_buah=%s,id_supplier=%s WHERE id_buah=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data berhasil diubah!'.format(cursor.rowcount))

def delete(data):
    cursor = db.cursor()
    sql="""DELETE FROM buah WHERE id_buah=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Buah berhasil dihapus!'.format(cursor.rowcount))

def search(id_buah):
    cursor = db.cursor()
    sql="""SELECT*FROM buah WHERE id_buah=%s"""
    cursor.execute(sql,id_buah)
    results = cursor.fetchall()
    print('-----------------------------------------------------------------------------------------------------------------')
    print("| ID | NAMA BUAH\t| JUMLAH BUAH\t| STATUS BUAH\t| HARGA SATUAN/Kg\t| JENIS BUAH\t\t\t| ID SUPPLIER\t|")
    print('-----------------------------------------------------------------------------------------------------------------')
    for data in results:
        print("|", data[0], " |", data[1], "\t\t|", data[2], "\t\t\t|", data[3], "\t\t|", data[4], "\t\t\t|", data[5],"\t\t|", data[6], "\t\t\t|")
        print('-----------------------------------------------------------------------------------------------------------------')