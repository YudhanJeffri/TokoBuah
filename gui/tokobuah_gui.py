import tkinter as tk
from function import data_buah
from function import pelanggan
import tkinter.messagebox as MessageBox


def pelanggan_window():
    window = tk.Toplevel()
    window.title('Pelanggan')
    window.geometry("500x300")
    nama = tk.Label(window, text='Nama Pelanggan')
    nama.place(x=20, y=60)

    alamat = tk.Label(window, text='Alamat Pelanggan')
    alamat.place(x=20, y=90)

    email = tk.Label(window, text='Email Pelanggan')
    email.place(x=20, y=120)

    id_member = tk.Label(window, text='ID Pelanggan')
    id_member.place(x=20, y=30)

    e_nama = tk.Entry(window)
    e_nama.place(x=150, y=60)

    e_alamat = tk.Entry(window)
    e_alamat.place(x=150, y=90)

    e_id_member = tk.Entry(window)
    e_id_member.place(x=150, y=30)

    e_email = tk.Entry(window)
    e_email.place(x=150, y=120)

    def button_insert():

        nama = e_nama.get()
        alamat = e_alamat.get()
        id = e_id_member.get()
        email = e_email.get()

        if (id >= '0'):
            MessageBox.showinfo("Insert Status", "ID Harus Kosong!")
        elif (nama == ""):
            MessageBox.showinfo("Insert Status", "Nama Tidak Boleh Kosong!")
        elif (alamat == ""):
            MessageBox.showinfo("Insert Status", "Alamat Tidak Boleh Kosong!")
        elif(email == ""):
            MessageBox.showinfo("Insert Status", "Alamat Email Tidak Boleh Kosong!")
        else:
            data = [nama, alamat,email]
            pelanggan.add(data)

            e_nama.delete(0, 'end')
            e_alamat.delete(0, 'end')
            e_email.delete(0, 'end')
            MessageBox.showinfo("Insert Status", "Data member berhasil ditambahkan!")

    button_insert = tk.Button(window, text='Insert', font=("italic", 10), bg="white", command=button_insert)
    button_insert.place(x=50, y=150)



root = tk.Tk()
root.title('Toko Buah')
root.geometry("500x300")
b = tk.Button(root, text="Pelanggan", command=pelanggan_window())
b.pack()

root.mainloop()