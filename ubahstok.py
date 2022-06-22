def ubah_stok(data_game):
    # Program ubah stok
    # I.S. stok terinisialisasi pada data game
    # F.S. mengubah stok game (bisa menambah/mengurangi)

    # Kamus Lokal
    # id : string {id game}
    # sum : integer {jumlah ubah stok}
    # stok _awal : integer {stok awal game}
    # stok_akhir : integer {stok setelah diubah}
    # cek : boolean {validasi}

    # Algoritma
    cek = False
    while not cek:
        id = input("Masukkan ID game: ")
        if id == '':  # cek kosong atau tidak
            print("ID tidak boleh kosong!")
            cek = False
        else:
            for i in data_game:  # cek id game ada atau tidak
                if id == i[0]:
                    cek = True
            if not cek:
                print("Tidak ada game dengan ID tersebut!")

    cek = False  # input jumlah dengan validasi integer
    while not cek:
        try:
            sum = int(input("Masukkan jumlah: "))
            cek = True
        except ValueError:
            print("Masukan tidak valid. Coba lagi!")
            cek = False

    stok_awal = 0  # jumlah stok sebelum diubah
    for i in data_game:
        if i[0] == id:
            stok_awal = int(i[5])

    if (sum < 0):
        if stok_awal + sum < 0:
            print(
                "Stok game gagal dikurangi karena stok kurang. Stok sekarang: ", stok_awal)
        elif (stok_awal > sum):
            stok_akhir = stok_awal + sum
            for i in data_game:
                if i[0] == id:
                    i[5] = stok_akhir
            print("Stok game berhasil dikurangi. Stok sekarang: ", stok_akhir)
    elif sum == 0:
        print("Stok sekarang: ", stok_awal)
    else:  # sum>0
        stok_akhir = stok_awal + sum
        for i in data_game:
            if i[0] == id:
                i[5] = stok_akhir
        print("Stok game berhasil ditambah. Stok sekarang: ", stok_akhir)
