from misc import print_matrix

def search_game_at_store(data_game):
    # Prosedur mencari game yang ada di toko berdasar id, nama game, harga, kategori, dan tahun rilis
    # I.S. input berupa id(string), nama game (string), harga(string), kategori(string), dan tahun rilis(integer > 0)
    # F.S. menampilkan game hasil pencarian

    # KAMUS LOKAL
    # id : string {masukan id game}
    # tahun_rilis : string {masukan tahun rilis}
    # cek : boolean {validasi}
    # found : integer {jumlah game yang ditemukan}
    # found_game : matrix of string {menyimpan hasil pencarian}
    # hapus : array of integer {index yang tidak sesuai pencarian}
    # procedure print_matrix(matrix: matrix of string)
    #    {I.S. matrix terdefinisi, yaitu sebuah list 2D 
    #     F.S. matrix tercetak di layar dengan rapi}
    # function length(x : string or array) => integer
    #    {I.S. menerima parameter berupa string atau array
    #     F.S. mengembalikan panjang karakter atau array berupa integer}

    # Implementasi fungsi atau prosedur
    def length(x):
        # Fungsi menghitung panjang 
        # I.S. menerima parameter berupa string atau array
        # F.S. mengembalikan panjang karakter atau array berupa integer

        # KAMUS LOKAL
        # panjang : integer 

        # ALGORITMA
        panjang = 0
        for i in x:
            panjang += 1
        return panjang

    # ALGORITMA UTAMA
    id = input('Masukan ID Game: ')
    nama = input('Masukan Nama Game: ')

    cek = False  # input harga dengan validasi harus > 0 atau '' (integer)
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

    kategori = input('Masukan Kategori Game: ')

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

    print('Daftar game pada inventory yang memenuhi kriteria:')

    found = 0
    found_game = []
    for i in range(1,length(data_game)):
        if id != '':
            if id != data_game[i][0]:
                continue
        
        if nama != '':
            if nama != data_game[i][1]:
                continue

        if kategori != '':
            if kategori != data_game[i][2]:
                continue
        
        if tahun_rilis != '':
            if tahun_rilis != data_game[i][3]:
                continue
        
        if harga != '':
            if harga != data_game[i][4]:
                continue
        
        found_game += [data_game[i]]
        found += 1

    if found == 0:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    else:
        print_matrix(found_game)
