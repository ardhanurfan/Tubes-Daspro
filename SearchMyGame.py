from misc import print_matrix

def search_my_game(user_id, data_kepemilikan, data_game):
    # Prosedur mencari game yang dimiliki user berdasar id, tahun rilis
    # I.S. input berupa id(string) dan/atau tahun rilis (integer > 0)
    # F.S. menampilkan game hasil pencarian

    # KAMUS LOKAL
    # id : string {masukan id game}
    # tahun_rilis : string {masukan tahun rilis}
    # cek : boolean {validasi input}
    # found : integer {jumlah game yang ditemukan}
    # found_game : matrix of string {menyimpan hasil pencarian}
    # procedure print_matrix(matrix: matrix of string)
    #    {I.S. matrix terdefinisi, yaitu sebuah list 2D 
    #     F.S. matrix tercetak di layar dengan rapi}
    
    # ALGORITMA UTAMA

    # Mencari game yang dimiliki
    # Mencari game_id yang dimiliki
    my_game_id = []
    for i in data_kepemilikan:
        if i[1] == user_id:
            my_game_id += [i[0]]
    
    # Mencari data game yang dimiliki berdasar id game
    my_game = []
    for i in my_game_id:
        for j in data_game:
            if i == j[0]:
                # Menambahkan kecuali stok
                temp = []
                for k in range(5):
                    temp += [j[k]]
                my_game += [temp]
    
    id = input('Masukan ID Game: ')

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
    for i in my_game:
        if id != '' and str(tahun_rilis) != '':  # semua diisi
            if i[0] == id and i[3] == str(tahun_rilis):
                found += 1
                found_game += [i]
        elif str(tahun_rilis) != '':  # jika id kosong
            if i[3] == str(tahun_rilis):
                found += 1
                found_game += [i]
        elif id != '' :  # jika tahun rilis kosong
            if i[0] == id:
                found += 1
                found_game += [i]
        else: # Jika keduanya kosong
            found += 1
            found_game += [i]

    if found == 0:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    else:
        print_matrix(found_game)
