import connect

db = connect.koneksi()
#menambahkan data baru ke dalam tabel supplier
def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO supplier(nama_supplier,alamat_supplier,no_telepon_supplier)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data supplier berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel supplier
def show():
    cursor=db.cursor()
    sql="""SELECT*FroM supplier"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print('---------------------------------------------------------------------')
    print("| ID | NAMA\t\t\t\t\t| ALAMAT\t\t| NO TELEPON SUPPLIER SUPPLIER\t\t|")
    print('---------------------------------------------------------------------')
    for data in results:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t\t\t|",data[3],"\t\t\t\t|")
        print('---------------------------------------------------------------------')

#mengubah data per record berdasarkan id pada tabel supplier
def edit(data_suppplier):
    cursor = db.cursor()
    sql = """UPDATE supplier SET nama_supplier=%s,alamat_supplier=%s,no_telepon_supplier=%s WHERE id_supplier=%s"""
    cursor.execute(sql,data_suppplier)
    db.commit()
    print('{}Data berhasil diubah!'.format(cursor.rowcount))

#menghapus data dari tabel supplier
def delete(data):
    cursor = db.cursor()
    sql="""DELETE FROM supplier WHERE id_supplier=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data supplier berhasil dihapus!'.format(cursor.rowcount))

#mencari data dari tabel supplier
def search(id_supplier):
    cursor = db.cursor()
    sql="""SELECT*FROM supplier WHERE id_supplier=%s"""
    cursor.execute(sql,id_supplier)
    results = cursor.fetchall()
    print("------------------------------------------------")
    print("|ID|NAMA\t\t ALAMAT\t\t NO TELEPON SUPPLIER\t\t")
    print("------------------------------------------------")
    for data in results:
        print("|",data[0],"|",data[1],"\t\t",data[2],"\t\t")
        print('----------------------------------------')
