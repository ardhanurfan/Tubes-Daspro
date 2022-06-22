from misc import len

def login(matrixUser):
    # Spesifikasi : Meminta input username dan password. Jika input valid, akan mengembalikan
    #               role dan indeks user di matrixUser. Jika tidak, akan mengembalikan string
    #               kosong dan -1

    # KAMUS LOKAL
    # username, password : string
    # i : int

    # ALGORITMA
    username = str(input("Masukkan username: "))
    password = str(input("Masukkan password: "))
    for i in range(1, len(matrixUser)):
        if (username == matrixUser[i][1]) and (password == matrixUser[i][3]):
            print(f"Halo {matrixUser [i][2]} ! Selamat datang di \"Binomo\" ")
            return matrixUser[i][4], i
    print("Password atau username salah atau tidak ditemukan.")
    return '', -1