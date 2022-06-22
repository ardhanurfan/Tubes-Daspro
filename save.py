from misc import len

def rewrite(matrix,path):
    # I.S. matrix dan path terdefinisi
    # F.S. data pada matrix ditulis ke file pada path

    # KAMUS LOKAL

    # ALGORITMA
    with open(path,'w') as file:
        for arr in matrix:
            line = '\"'
            for i in range(len(arr)):
                line += arr[i]
                if i < len(arr) - 1:
                    line += ';'
            file.write(line)
            file.write('\"\n')


def save(matrixUser,matrixGame,matrixRiwayat,matrixKepemilikan):
    # I.S. matrixUser, matrixGame, matrixRiwayat, dan matrixKepemilikan terdefinisi
    # F.S. seluruh matrix disimpan dalam file user.csv, game.csv, riwayat.csv, dan kepemilikan.csv
    #      dalam folder yang ditentukan input
    # Asumsi seluruh folder save disimpan dalam folder 'Save folders'

    # KAMUS LOKAL
    # namaFolder, savePath : string
    import os

    # ALGORITMA
    namaFolder = input("Masukkan nama folder penyimpanan: ")
    savePath = os.getcwd() + "\\Save folders\\" + namaFolder

    # Buat folder jika belum ada
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    # Rewrite isi file
    pathUser = savePath + "\\user.csv"
    pathGame = savePath + "\\game.csv"
    pathRiwayat = savePath + "\\riwayat.csv"
    pathKepemilikan = savePath + "\\kepemilikan.csv"

    rewrite(matrixUser,pathUser)
    rewrite(matrixGame,pathGame)
    rewrite(matrixRiwayat,pathRiwayat)
    rewrite(matrixKepemilikan,pathKepemilikan)

    # Menyimpan data
    print("\nSaving...")


    # Akhir
    print(f"Data telah disimpan pada folder {namaFolder} !")

