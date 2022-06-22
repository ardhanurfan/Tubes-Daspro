from misc import gameidgenerator

def tambah_game(matrixGame):
    # Spesifikasi : Menambahkan game pada toko melalui pengisian informasi game yang akan ditambahkan. Jika ada 
    #               informasi yang belum dimasukkan, program akan meminta input lagi pada pengguna.
    # I.S. matrixGame terdefinisi
    # F.S. matrixgame menerima tambahan satu baris berisi game baru

    # KAMUS LOKAL
    # nama, kategori, tahun_rilis : string
    # harga, stok : integer


    # ALGORITMA
      nama = input("Masukkan nama game: ")
      kategori = input("Masukkan kategori: ")
      tahun_rilis = input("Masukkan tahun rilis: ")
      harga = int(input("Masukkan harga (contoh: 11000): "))
      stok = int(input("Masukkan stok awal: "))

      # Validasi kelengkapan input pengguna
      while nama == '' or kategori == '' or tahun_rilis == '' or harga == '' or stok == '':
          print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
          nama = input("Masukkan nama game: ")
          kategori = input("Masukkan kategori: ")
          tahun_rilis = input("Masukkan tahun rilis: ")
          harga = int(input("Masukkan harga: "))
          stok = int(input("Masukkan stok awal: "))

      # Semua masukan sudah valid
      matrixGame += [[gameidgenerator(matrixGame), nama, kategori, tahun_rilis, harga]]
      print("Selamat! Berhasil menambahkan game ", nama, " .")
