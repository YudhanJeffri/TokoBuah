#build in
import mysql.connector
#fungsi koneksi
def koneksi():
    db = mysql.connector.connect(
        host = "localhost",
        user = "testuser",
        password = "test123",
        database = "tokobuah_py",
        autocommit = True
    )
    if db.is_connected():
        return db
    else:
        print('DB disconnect!')
