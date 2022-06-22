from save import save

def exit_program(matrixUser,matrixGame,matrixRiwayat,matrixKepemilikan):
    # Prosedur untuk keluar dari program
    # I.S. program berjalan
    # F.S. mengakhiri program bisa save atau tidak save

    # Kamus Lokal
    # cek : boolean {validasi input}
    # konfirm : string {"y" atau "Y" : (yes), "n" atau "N" : (no)}

    # Algoritma
    cek = False
    while not cek:
        konfirm = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
        if konfirm == 'n' or konfirm == 'N' or konfirm == 'Y' or konfirm == 'y':
            cek = True
        else:
            print('Masukan tidak valid. Coba lagi!')
    
    if konfirm == 'y' or konfirm == 'Y':
            save(matrixUser,matrixGame,matrixRiwayat,matrixKepemilikan)
        