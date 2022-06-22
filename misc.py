# Spesifikasi : fungsi-fungsi kecil yang harus diimplementasikan sendiri,
#               tetapi dapat dipakai di banyak tempat


def len(x):
    # Spesifikasi : mengembalikan panjang string/array

    # KAMUS LOKAL
    # panjang : integer

    # ALGORITMA
    panjang = 0
    for i in x:
        panjang += 1
    return panjang

def lowercase(str):
    # Spesifikasi : mengembalikan str yang seluruh hurufnya dibuat lowercase

    # KAMUS LOKAL
    # str_lower : string

    # ALGORITMA
    str_lower = ""
    for c in str:
        if ord('A') <= ord(c) and ord(c) <= ord('Z'):
            str_lower += chr(ord(c) + 32)
        else:
            str_lower += c
    return str_lower

def sortMatrix(matrix, key, asc):
    # Spesifikasi : mengembalikan matrix yang sudah disort
    #               key bernilai indeks yang mempengaruhi sort
    #               asc bernilai True jika sort ascending, False jika sort descending

    # KAMUS LOKAL
    # mid : int
    # matrix_l, matrix_r, matrix_sorted : matrix of string
    # itr_l, itr_r : int

    # ALGORITMA
    # Basis
    if len(matrix) <= 1: 
        return matrix
    # Rekurens
    mid = len(matrix) // 2

    # Sort paruh kiri matrix
    matrix_l = []
    for i in range(0,mid):
        matrix_l += [matrix[i]]
    matrix_l = sortMatrix(matrix_l, key, asc)

    # Sort paruh kanan matrix
    matrix_r = []
    for i in range(mid,len(matrix)):
        matrix_r += [matrix[i]]
    matrix_r = sortMatrix(matrix_r, key, asc)

    # Merge kedua bagian matrix
    itr_l = 0
    itr_r = 0
    matrix_sorted = []
    while(itr_l < len(matrix_l) or itr_r < len(matrix_r)):
        if(itr_l == len(matrix_l)):
            matrix_sorted += [matrix_r[itr_r]]
            itr_r += 1
        elif(itr_r == len(matrix_r)):
            matrix_sorted += [matrix_l[itr_l]]
            itr_l += 1
        elif(( ((int)(matrix_l[itr_l][key])) <= ((int)(matrix_r[itr_r][key])) ) ^ (not asc)):
            matrix_sorted += [matrix_l[itr_l]]
            itr_l += 1
        else:
            matrix_sorted += [matrix_r[itr_r]]
            itr_r += 1
    return matrix_sorted

def print_matrix(matrix):
    # I.S. matrix terdefinisi, yaitu sebuah list 2D 
    # F.S. matrix tercetak di layar dengan rapi

    # Contoh masukan matrix dan hasil cetaknya
    # [ ["GAME001", "Bensin Impact", "0", "Adventure", "2020", "10"], 
    #   ["GAME002", "Suram Online", "0", "MMORPG", "2015", "100"]   ]
    #
    # 1. GAME001 | Bensin Impact | 0 | Adventure | 2020 | 10
    # 2. GAME002 | Suram Online  | 0 | MMORPG    | 2015 | 100

    # KAMUS LOKAL
    # width : list of integer
    # width_num : int
    # n,m : int

    # ALGORITMA
    # Validasi ukuran matrix
    if(len(matrix) == 0 or len(matrix[0]) == 0):
        return 0
    
    # Cari elemen terpanjang untuk dijadikan lebar kolom
    n = len(matrix)
    m = len(matrix[0])
    width = [0 for i in range(m)]
    width_num = len((str)(n))

    for i in range(n):
        for j in range(m):
            if(width[j] < len((str)(matrix[i][j]))):
                width[j] = len((str)(matrix[i][j]))
    
    # Print matrix
    for i in range(n):
        print(" " * (width_num - len( (str)(i) ) ), end = '')
        print(i+1 , end='.')
        for j in range(0,m):
            print(' ', end = '')
            print(matrix[i][j], end='')
            print(" " * (width[j] - len( (str)(matrix[i][j]) )), end = '')
            if(j < m-1):
                print(' |', end = '')
        print()

def validasi(role, access):
    # Return True jika role bagian dari akses
    # Return False dan mengeluarkan pesan error jika tidak

    # KAMUS LOKAL
    # c : string
    
    # ALGORITMA
    # Belum login
    if role == '': 
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
        return False
    
    for c in access:
        if lowercase(role) == lowercase(c):
            return True

    # user tidak memiliki akses
    if access == ['admin']:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    elif access == ['user']:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        
    return False

def gameidgenerator(matrixGame):
    # Return GAME00(len(matrixGame)) jika panjang matrixGame < 10
    # Return GAME0(len(matrixGame)) jika panjang matrixGame >= 10 dan < 100
    # Return GAME(len(matrixGame)) jika panjang matrixGame >= 100

    # KAMUS LOKAL

    # ALGORITMA

      # Panjang matrixGame kurang dari 10
      if len(matrixGame) < 10:
          return ("GAME00" + str(len(matrixGame)))

      # Panjang matrixGame sama dengan atau lebih dari 10 dan kurang dari 100
      elif len(matrixGame) >= 10 and len(matrixGame) < 100:
          return ("GAME0" + str(len(matrixGame)))

      # Panjang matrixGame sama dengan atau lebih dari 100
      else:
          return ("GAME" + str(len(matrixGame)))
