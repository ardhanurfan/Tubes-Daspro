from misc import lowercase, sortMatrix, print_matrix, len


def listing_game(matrixGame):
    # I.S. matrixGame terdefinisi
    # F.S. output matrixGame yang sudah disort

    # KAMUS LOKAL
    # matrixOutput : matrix of string 
    # urutan : list of string
    # n, m : int
    # sortScheme : string { skema sorting matrix }
    # i, j, pos : int { indeks pengulangan }
    
    # ALGORITMA
    sortScheme = input("Skema sorting: ")
    urutan = ["id", "nama", "harga", "kategori", "tahun_rilis", "stok"]
    n = len(matrixGame)
    if n <= 1:
        # Validasi ukuran matrixGame
        return
    m = len(matrixGame[0])
    matrixOutput = [[0 for j in range(m)] for i in range(n-1)]

    # Urutkan matrix sesuai list urutan
    for i in range(m):
        for pos in range(m):
            if lowercase(urutan[i]) == lowercase(matrixGame[0][pos]):
                for j in range(1,n):
                    matrixOutput[j-1][i] = matrixGame[j][pos]
                break
    
    # Urutkan matrix sesuai sortScheme
    sortScheme = lowercase(sortScheme)
    if sortScheme == "harga+":
        # harga ascending
        matrixOutput = sortMatrix(matrixOutput, 2, True)
    elif sortScheme == "harga-":
        # harga descending
        matrixOutput = sortMatrix(matrixOutput, 2, False)
    elif sortScheme == "tahun+":
        # tahun_rilis ascending
        matrixOutput = sortMatrix(matrixOutput, 4, True)
    elif sortScheme == "tahun-":
        # tahun_rilis descending
        matrixOutput = sortMatrix(matrixOutput, 4, False)
    elif sortScheme == "":
        # id ascending
        # tidak perlu disort karena defaultnya ascending
        pass
    else:
        print("Skema sorting tidak valid!")
        return

    print_matrix(matrixOutput)