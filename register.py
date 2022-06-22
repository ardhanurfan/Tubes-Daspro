import misc

def register(matrixUser):
    # Spesifikasi : Meminta input nama, username, dan password, lalu menambahkan user
    #               role 'User' sesuai input yang diterima 
    # I.S. matrixUser terdefinisi
    # F.S. matrixUser mendapat tambahan maksimal satu baris berisi user baru

    # KAMUS LOKAL
    # nama, username, password : string
    # c : string { satu huruf, untuk iterasi }

    # ALGORITMA
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print()

    # Validasi username
    for c in username:
        if not ( ('A' <= c and c <= 'Z') or ('a' <= c and c <= 'z') or ('0' <= c and c <= '9') or c == '-' or c == '_' ):
            print(f"Username {username} tidak valid, silakan menggunakan username lain.")
            return
        
    # Validasi nama & password (tidak boleh ada ;)
    for c in nama:
        if (c == ';'):
            print(f"Nama {nama} tidak valid, silakan menggunakan username lain.")
            return
    for c in password:
        if (c == ';'):
            print(f"Password {password} tidak valid, silakan menggunakan username lain.")
            return

    # Username sudah terdaftar
    for i in range(1,misc.len(matrixUser)):
        if(username == matrixUser[i][1]):
            print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
            return

    # Semua masukan valid
    matrixUser += [[str(misc.len(matrixUser)), username, nama, password, "User", "0"]]
    print(f"Username {username} telah berhasil register ke dalam \"Binomo\".")