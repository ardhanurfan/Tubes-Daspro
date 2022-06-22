

def topup(matrixuser):
    # Program Top Up
    # I.S. matrixuser terdefinisi
    # F.S. matrixuser dengan saldo setelah di top up

    # Kamus Lokal
    # username : string
    # saldo : integer {saldo yang yang akan ditambahkan}
    # saldo_awal : integer {saldo sebelum top up}
    # saldo_akhir : integer {saldo setelah top up}
    # cek : boolean {validasi}
    # cek_user : boolean {validasi}
    # index : integer {index data}

    # Algoritma
    username = str(input("Masukkan username: "))

    cek = False  # input jumlah top up dengan validasi integer
    while not cek:
        try:
            saldo = int(input("Masukkan saldo: "))
            cek = True
        except ValueError:
            print("Masukan saldo tidak valid. Coba lagi!")
            cek = False

    cek_user = False
    index = 0
    for i in matrixuser:
        if username == i[1]:
            cek_user = True
            saldo_awal = int(i[5])
            break
        index += 1

    if cek_user:
        if (saldo > 0):
            saldo_akhir = saldo + saldo_awal
            matrixuser[index][5] = str(saldo_akhir)
            print("Top up berhasil. Saldo ", username,
                  "bertambah menjadi ", saldo_akhir)
        else:  # saldo_awal < saldo
            if (saldo_awal + saldo < 0):
                print("Masukan tidak valid.")
            else:  # Jika saldo awal awal > saldo
                saldo_akhir = saldo_awal + saldo
                matrixuser[index][5] = str(saldo_akhir)
                print("Top up berhasil. Saldo ", username,
                      "bertambah menjadi ", saldo_akhir)
    else:  # Username tidak ditemukan
        print((f"Username {username} tidak ditemukan."))
