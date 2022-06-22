def cekMenang(papan):
    # Mengembalikan 'X' jika pemain 1 menang, 'O' jika pemain 2 menang,
    # '#' jika belum ada yang menang, dan '-' jika seri

    # KAMUS LOKAL
    # full : bool
    # win : str
    # i : int

    # ALGORITMA
    win = '#'
    full = True

    # Cek penuh/tidaknya papan
    for lc in papan:
        for c in lc:
            if c == '#':
                full = False

    # Cek menang horizontal
    for lc in papan:
        if lc[0] == lc[1] and lc[1] == lc[2] and lc[0] != '#':
            win = lc[0]
    
    # Cek menang vertikal
    for i in range(3):
        if papan[0][i] == papan[1][i] and papan[1][i] == papan[2][i] and papan[0][i] != '#':
            win = papan[0][i]

    # Cek menang diagonal
    if papan[0][0] == papan[1][1] and papan[1][1] == papan[2][2] and papan[0][0] != '#':
        win = papan[0][0]
    if papan[2][0] == papan[1][1] and papan[1][1] == papan[0][2] and papan[2][0] != '#':
        win = papan[2][0]

    # Sudah ada yang menang
    if win != '#':
        return win
    # Papan sudah penuh
    elif full:
        return '-'
    # Belum ada yang menang dan masih bisa lanjut
    else:
        return '#'



def printPapan(papan):
    # I.S. papan terdefinisi
    # F.S. output papan

    # KAMUS LOKAL
    # lc : list[1..3] of string
    # c : string

    print("Status Papan")
    for lc in papan:
        for c in lc:
            print(c,end='')
        print()
    print()

def tictactoe():
    # I.S. -
    # F.S. program menjalankan permainan tictactoe

    # KAMUS LOKAL
    # papan : matrix[1..3][1..3] of string
    # giliranX : bool
    # i,j,x,y : int
    # pemenang : string

    # ALGORITMA
    print("Legenda:")
    print("# Kosong")
    print("X Pemain 1")
    print("O Pemain 2")
    print()

    papan = [['' for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            papan[i][j] = '#'
    
    printPapan(papan)

    giliranX = True
    while(cekMenang(papan) == '#'):
        if giliranX:
            print("Giliran Pemain \"X\"")
        else:
            print("Giliran Pemain \"O\"")
        
        x = int(input('X: '))
        y = int(input('Y: '))
        print()

        # Validasi x,y masuk range [1,3]
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Kotak tidak valid. Silakan pilih kotak lain.")
            continue

        # Ubah 1-based indexing ke 0-based
        x -= 1
        y -= 1

        # Validasi papan[x][y] belum ditempati
        if papan[x][y] != '#':
            print(f"Posisi ({x+1} , {y+1}) sudah ditempati. Silakan pilih kotak lain")
            continue

        # Sudah valid, masukkan data ke papan
        papan[x][y] = 'X' if giliranX else 'O'
        printPapan(papan)

        # Ganti giliran
        giliranX ^= True
    
    # Game selesai, mengeluarkan verdict
    pemenang = cekMenang(papan)
    if pemenang == '-':
        print("Permainan berakhir seri.")
    else:
        print(f"Pemain \"{pemenang}\" menang.")


        