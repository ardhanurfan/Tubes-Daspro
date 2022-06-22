def ubah_game(data_game):
    # I.S masukan berupa id, nama game, kategori game (string)
    # F.S mengembalikan data game (array) yang telah diubah berdasarkan input

    # KAMUS LOKAL
    # id, nama, string : string
    # tahun_rilis : integer
    # cek : bool {untuk memvalidasi input}
    # i : string {digunakan dalam iterasi}

    # ALGORITMA
    cek = False
    while not cek:
        id = input('Masukkan ID game: ')
        if id == '':  # cek kosong atau tidak
            print('ID tidak boleh kosong!')
            cek = False
        else:
            for i in data_game:  # cek id game ada atau tidak
                if id == i[0]:
                    cek = True
            if not cek:
                print('Tidak ada game dengan ID tersebut!')

    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')

    cek = False  # input tahun rilis dengan validasi harus > 0 atau ''
    while not cek:
        try:
            tahun_rilis = input('Masukkan tahun rilis: ')
            if tahun_rilis == '' or int(tahun_rilis) > 0:
                cek = True
            else:
                raise ValueError
        except ValueError:
            print('Tahun rilis tidak valid. Coba lagi!')
            cek = False

    cek = False  # input harga dengan validasi harus > 0 atau ''
    while not cek:
        try:
            harga = input('Masukan Harga Game: ')
            if harga == '' or int(harga) > 0:
                cek = True
            else:
                raise ValueError
        except ValueError:
            print('Harga tidak valid. Coba lagi! (contoh: 11000)')
            cek = False

    for array in data_game:
        if array[0] == id:
            index = 1
            for i in [nama, kategori, tahun_rilis, harga]:
                if i != '':
                    array[index] = str(i)
                index += 1
