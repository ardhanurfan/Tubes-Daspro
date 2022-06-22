from misc import print_matrix, len

def riwayat(user_id, matrixriwayat, matrixgame):
    # Spesifikasi : Menampilkan riwayat pembelian game pengguna. Menampilkan pesan khusus ketika pengguna
    #               tidak memiliki riwayat.
    # I.S. : matrixUser, matrixriwayat terdefinisi
    # F.S. : Menampilkan list game yang dimiliki oleh pengguna (jika ada)

    # KAMUS LOKAL
    # riwayat_game_id : array of string {menyimpan id riwayat game}
    # riwayat_game : matrix of string {menyimpan riwayat game}
    # temp : array of string {menyimpan sementara data game}

    # ALGORITMA

    # Mencari game_id berdasar data riwayat
    riwayat_game_id = []
    for i in matrixriwayat:
        if i[3] == user_id:
            riwayat_game_id += [i[0]]
    
    # Mencari data game yang dimiliki berdasar id game
    riwayat_game = []
    for i in riwayat_game_id:
        for j in matrixgame:
            if i == j[0]:
                # Menambahkan kecuali stok
                temp = []
                for k in [0,1,4,3]:
                    temp += [j[k]]
                riwayat_game += [temp]

    # Kasus pengguna tidak memiliki riwayat pembelian
    if len(riwayat_game) == 0:
      print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk melakukan pembelian.")

    # Kasus pengguna memiliki riwayat pembelian
    else:
      print_matrix(riwayat_game)


