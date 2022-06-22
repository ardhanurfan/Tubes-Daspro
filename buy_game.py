import datetime
from misc import len

def buy_game(matrixUser, matrixGame, matrixRiwayat, matrixKepemilikan, useridx):
    # Spesifikasi : melakukan operasi pembelian game
    # I.S. matrixUser, matrixGame, matrixRiwayat, matrixKepemilikan, dan userid terdefinisi
    # F.S. keempat matrix diubah sesuai pembelian

    # KAMUS LOKAL
    # gameid, userid : string
    # gameidx, useridx : int
    # hargaGame, namaGame, tahun : string
    # i : int

    # ALGORITMA
    gameid = input("Masukkan ID Game: ")
    userid = str(useridx)
    gameidx = 0
    for i in range(1,len(matrixGame)):
        if(matrixGame[i][0] == gameid):
            gameidx = i
            break
    
    # ID Game tidak valid
    if(gameidx == 0):
        print("ID Game tidak valid!")
        return 
    
    # Game sudah dimiliki user
    for i in range(1,len(matrixKepemilikan)):
        if(matrixKepemilikan[i][0] == gameid and matrixKepemilikan[i][1] == userid):
            print("Anda sudah memiliki Game tersebut!")
            return 
    
    # User tidak memiliki saldo yang cukup
    hargaGame = matrixGame[gameidx][4]
    if(int(matrixUser[useridx][5]) < int(hargaGame)):
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        return 
    
    # Tidak terdapat stok Game
    if(int(matrixGame[gameidx][5]) == 0):
        print("Stok Game tersebut sedang habis!")
        return 

    # Semua kondisi terpenuhi
    namaGame = matrixGame[gameidx][1]
    tahun = str(datetime.date.today().year)

    matrixUser[useridx][5] = str(int(matrixUser[useridx][5]) - int(hargaGame))
    matrixGame[gameidx][5] = str(int(matrixGame[gameidx][5]) - 1)
    matrixKepemilikan += [[gameid, userid]]
    matrixRiwayat += [[gameid, namaGame, hargaGame, userid, tahun]]
    print(f"Game \"{namaGame}\" Berhasil dibeli!")