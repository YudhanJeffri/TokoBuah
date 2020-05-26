from function import data_buah
from function import pegawai
from function import supplier
from function import pembayaran
from function import pelanggan
from function import transaksi

print('|---Sistem Informasi Toko Buah---|')

print('1. Buah')
print('2. Supplier')
print('3. Pegawai')
print('4. Pembayaran')
print('5. Pelanggan')
print('6. Transaksi')
print('|---Sistem Informasi Toko Buah---|')
menu1 = int(input('Pilih : '))


#menu Buah
if(menu1 == 1):
    print('1. Tambah Buah')
    print('2. Ubah Buah')
    print('3. Hapus Buah')
    print('4. Tampilkan Buah')
    print('5. Cari Buah')
    menu2 = int(input('[Buah]Pilih : '))
    if(menu2 == 1):
        nama_buah = input("Nama Buah : ")
        jumlah_buah = int(input("Jumlah Buah : "))
        status_buah = input("Status Buah : ")
        harga_satuan = int(input("Harga Satuan/Kg : "))
        jenis_buah = input("Jenis Buah : ")
        id_supplier = int(input("Id Suplier : "))
        data=[nama_buah,jumlah_buah,status_buah,harga_satuan,jenis_buah,id_supplier]
        data_buah.add(data)
    elif(menu2 == 2):
        id_buah = int(input('No, Buah : '))
        nama_buah = input("Nama Buah : ")
        jumlah_buah = int(input("Jumlah Buah : "))
        status_buah = input("Status Buah : ")
        harga_satuan = int(input("Harga Satuan/Kg : "))
        jenis_buah = input("Jenis Buah : ")
        id_supplier = int(input("Id Supplier : "))
        data = [nama_buah, jumlah_buah, status_buah, harga_satuan, jenis_buah, id_supplier,id_buah]
        data_buah.edit(data)
    elif(menu2 == 3):
        id_buah = input('No. Buah : ')
        data = [id_buah]
        data_buah.search(data)
        confirm = input('Yakin Menghapus member ini?[Y/N]:')
        if(confirm == 'Y'):
            data_buah.delete(data)
        else:
            print('Tidak jadi menghapus data member!')

    elif(menu2==4):
        data_buah.show()
    elif(menu2==5):
        id_buah = input('No. Buah : ')
        data = [id_buah]
        data_buah.search(data)
    else:
        print('Menu tidak tersedia')

#menu Supplier
elif(menu1 == 2):
    print('1. Tambah Supplier')
    print('2. Ubah Supplier')
    print('3. Hapus Supplier')
    print('4. Tampilkan Supplier')
    menu2 = int(input('[Supplier]Pilih : '))
    if (menu2 == 1):
        nama_supplier = input("Nama Supplier: ")
        alamat_supplier = input("Alamat Supplier : ")
        no_telepon_supplier = int(input("No Telepon : "))
        data = [nama_supplier, alamat_supplier,no_telepon_supplier]
        supplier.add(data)
    elif (menu2 == 2):
        id_supplier = int(input('No, Supplier : '))
        nama_supplier = input('Nama Supplier : ')
        alamat_supplier = input('Alamat Supplier : ')
        data_supplier = [nama_supplier, alamat_supplier, id_supplier]
        supplier.edit(data_supplier)
    elif (menu2 == 3):
        id_supplier = int(input('No. Supplier : '))
        data = [id_supplier]
        supplier.search(data)
        confirm = input('Yakin Menghapus Supplier ini?[Y/N]:')
        if (confirm == 'Y'):
            supplier.delete(data)
        else:
            print('Tidak jadi menghapus data supplier!')
    elif (menu2 == 4):
        supplier.show()
    else:
        print('Menu tidak tersedia')

#menu Pegawai
elif(menu1 == 3):
    print('1. Tambah Pegawai')
    print('2. Ubah Pegawai')
    print('3. Hapus Pegawai')
    print('4. Tampilkan Pegawai')
    menu4 = int(input('[Pegawai]Pilih : '))
    if (menu4 == 1):
        name = input("Nama Pegawai : ")
        alamat = input("Alamat Pegawai : ")
        email_pegawai = input("Email : ")
        data = [name, alamat,email_pegawai]
        pegawai.add(data)
    elif (menu4 == 2):
        id_pegawai = input('No, Pegawai : ')
        nama = input('Nama : ')
        alamat_pegawai = input('Alamat : ')
        email_pegawai = input('Email : ')
        data = [nama, alamat_pegawai, id_pegawai,email_pegawai]
        pegawai.edit(data)
    elif (menu4 == 3):
        id_pegawai = input('No. Pegawai : ')
        data = [id_pegawai]
        pegawai.search(data)
        confirm = input('Yakin Memecat Pegawai ini?[Y/N]:')
        if (confirm == 'Y'):
            pegawai.delete(data)
        else:
            print('Tidak jadi Memecat Pegawai!')
    elif (menu4 == 4):
        pegawai.show()
    else:
        print('Menu tidak tersedia')

    #menu Pembayaran
elif (menu1 == 4):
    print('1. Tambah Pembayaran')
    print('2. Ubah Pembayaran')
    print('3. Hapus Pembayaran')
    print('4. Tampilkan Pembayaran')
    menu2 = int(input('[Pembayaran]Pilih : '))

    if (menu2 == 1):
        tgl_pembayaran = input('Tanggal : ')
        total_bayar = input('Total : ')
        id_transaksi = input('Id_transaksi')
        data = [tgl_pembayaran, total_bayar, id_transaksi]
        pembayaran.add(data)

    elif (menu2 == 2):
        id_pembayaran = input('Id Pembayaran : ')
        tgl_pembayaran = input('Tanggal :')
        total_bayar = input('Total : ')
        id_transaksi = input('Id Transaksi : ')
        data = [tgl_pembayaran, total_bayar, id_transaksi, id_pembayaran]
        pembayaran.edit(data)
    elif (menu2 == 3):
        id_pembayaran = input('Id Pembayaran :')
        data = [id_pembayaran]
        pembayaran.search(data)
        confirm = input('Yakin Menghapus pelanggan ini?[Y/N]:')
        if (confirm == 'Y'):
            pembayaran.delete(data)
        else:
            print('Tidak jadi menghapus data pelanggan!')

    elif (menu2 == 4):
        pembayaran.show()
    else:
        print('Menu tidak tersedia')
#menu Pelanggan
elif(menu1 == 5):
    print('1. Tambah Pelanggan')
    print('2. Ubah Pelanggan')
    print('3. Hapus Pelanggan')
    print('4. Tampilkan Pelanggan')
    menu4 = int(input('[Pelanggan]Pilih : '))
    if (menu4 == 1):
        name = input("Nama Pelanggan : ")
        alamat = input("Alamat Pelanggan : ")
        email_pelanggan = input("Email Pelanggan : ")
        data = [name, alamat,email_pelanggan]
        pelanggan.add(data)
    elif (menu4 == 2):
        id_pelanggan = input('No, Pelanggan : ')
        nama = input('Nama Pelanggan : ')
        alamat_pelanggan = input('Alamat Pelanggan : ')
        email_pelanggan = input('Email Pelanggan : ')
        data = [nama, alamat_pelanggan, id_pelanggan,email_pelanggan]
        pelanggan.edit(data)
    elif (menu4 == 3):
        id_pelanggan = input('No. Pelanggan : ')
        data = [id_pelanggan]
        pelanggan.search(data)
        confirm = input('Menghapus Pelanggan ini?[Y/N]:')
        if (confirm == 'Y'):
            pelanggan.delete(data)
        else:
            print('Tidak jadi Menghapus Pelanggan!')
    elif (menu4 == 4):
        pelanggan.show()
    else:
        print('Menu tidak tersedia')
elif(menu1 == 6):
    print('1. Tambah Transaksi')
    print('2. Ubah Transaksi')
    print('3. Hapus Transaksi')
    print('4. Tampilkan Transaksi')
    print('5. Cari Transaksi')
    menu4 = int(input('[Transaksi]Pilih : '))
    if (menu4 == 1):
        id_buah = int(input("Id Buah : "))
        id_pelanggan = int(input("Id Pelanggan : "))
        id_pegawai = int(input("Id Pegawai : "))
        keterangan = input("Keterangan (Lunas/Belum Lunas) : ")
        data = [id_buah,id_pelanggan,id_pegawai,keterangan]
        transaksi.add(data)
    elif (menu4 == 2):
        confirm = input('Hanya Mengubah Keterangan? [Y/N]:')
        if(confirm == 'Y'):
            id_transaksi = int(input("Id Transaksi : "))
            keterangan = input("Keterangan : ")
            data_keterangan = [keterangan,id_transaksi]
            transaksi.edit_keterangan(data_keterangan)
        else:
            id_transaksi = int(input("Id Transaksi : "))
            id_buah = int(input("Id Buah : "))
            id_pelanggan = int(input("Id Pelanggan : "))
            id_pegawai = int(input("Id Pegawai : "))
            keterangan = input("Keterangan : ")
            data = [id_buah, id_pelanggan, id_pegawai, keterangan,id_transaksi]
            transaksi.edit(data)
    elif (menu4 == 3):
        id_transaksi = input('No. Transaksi : ')
        data = [id_transaksi]
        transaksi.search(data)
        confirm = input('Menghapus Transaksi ini?[Y/N]:')
        if (confirm == 'Y'):
            transaksi.delete(data)
        else:
            print('Tidak jadi Menghapus Transaksi!')
    elif (menu4 == 4):
        transaksi.show()
    elif(menu4 == 5):
        id_transaksi = input('No. Transaksi : ')
        data = [id_transaksi]
        transaksi.search(data)
    else:
        print('Menu tidak tersedia')
