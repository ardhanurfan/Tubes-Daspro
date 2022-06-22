from misc import print_matrix, len

def list_game(user_id, matrixKepemilikan, matrixgame):
    # Spesifikasi : Memberikan daftar game yang dimiliki oleh pengguna.
    # I.S. : matrixKepemilikan terdefinisi
    # F.S. : Menampilkan daftar game yang dimiliki. Memberikan pesan khusus jika user tidak memiliki game

    # KAMUS LOKAL
    # my_game_id : array of string {menyimpan id game yang dimiliki}
    # my_game : matrix of string {menyimpan data game}
    # temp : array of string {menyimpan sementara data game}

    # ALGORITMA
    # Mencari game_id yang dimiliki
    my_game_id = []
    for i in matrixKepemilikan:
        if i[1] == user_id:
            my_game_id += [i[0]]
    
    # Mencari data game yang dimiliki berdasar id game
    my_game = []
    for i in my_game_id:
        for j in matrixgame:
            if i == j[0]:
                # Menambahkan kecuali stok
                temp = []
                for k in range(5):
                    temp += [j[k]]
                my_game += [temp]
     
    # Kasus user belum memiliki game
    if len(my_game) == 0:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk melakukan pembelian.")

    # Kasus user sudah memiliki game
    else:
        print_matrix(my_game)
