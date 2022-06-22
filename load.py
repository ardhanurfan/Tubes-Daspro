from misc import len
def split(str):
    # Spesifikasi : Menerima sebuah string berisi data yang dipisahkan oleh semicolon(;)
    #               dan mengembalikan sebuah array berisi data yang sudah dipisahkan

    # KAMUS LOKAL
    # arrLine : list of string
    # strMemo : string { tempat mencatat karakter sebelum masuk arrLine }
    # c : char 
    # i : int { iterator }

    arrLine = []
    strMemo = ""
    # Manual parse
    for i in range(0,len(str)):
        # karakter pertama dari depan dan kedua dari belakang diabaikan karena berupa petik dua
        if i == 0 or i == len(str) - 2:
            continue

        # Jika karakter = karakter pemisah (; atau newline), 
        # simpan karakter sebelumnya yang dicatat dalam array
        c = str[i]
        if c == ';' or c == '\n':
            arrLine += [strMemo]
            strMemo = ""
        else:
            strMemo += c

    return arrLine


def loadOneFile(path):
    # Spesifikasi : Menerima path menuju sebuah file dan mengembalikan matrix sesuai dengan isi file

    # KAMUS LOKAL
    # mat : matrix
    # arrLine : list of string
    # line : string
    # file : list of string

    mat = []
    with open(path,'r') as file:
        for line in file:
            arrLine = split(line)
            mat += [arrLine]
    return mat

                

def load(path):
    # Spesifikasi : menerima path menuju folder save dan mengembalikan matrix dari user.csv, 
    #               game.csv, riwayat.csv, dan kepemilikan.csv
    # Asumsi : urutan save file tidak berubah

    # KAMUS LOKAL
    # pathUser, pathGame, pathRiwayat, pathKepemilikan : string
    # matrixUser, matrixGame, matrixRiwayat, matrixKepemilikan : matrix of string

    pathUser = path + "\\user.csv"
    pathGame = path + "\\game.csv"
    pathRiwayat = path + "\\riwayat.csv"
    pathKepemilikan = path + "\\kepemilikan.csv"

    matrixUser = loadOneFile(pathUser)
    matrixGame = loadOneFile(pathGame)
    matrixRiwayat = loadOneFile(pathRiwayat)
    matrixKepemilikan = loadOneFile(pathKepemilikan)

    return matrixUser, matrixGame, matrixRiwayat, matrixKepemilikan

