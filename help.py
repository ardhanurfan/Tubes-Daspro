from misc import lowercase
def help(role):
    # Spesifikasi : Menampilkan panduan penggunaan sistem berdasarkan role pengguna.
    # I.S. role yang dimiliki oleh pengguna
    # F.S. Panduan penggunaan sistem diberikan

    # KAMUS LOKAL


    # ALGORITMA
    if lowercase(role) == 'admin':
        # Menampilkan panduan penggunaan sistem untuk admin

        print ("--- HELP ---", end = "\n")
        print ("1. register - Untuk melakukan registrasi user baru", end = "\n")
        print ("2. login - Untuk melakukan login ke dalam sistem", end = "\n")
        print ("3. tambah_game - Untuk menambah game yang dijual pada toko", end = "\n")
        print ("4. list_game_toko - Untuk melihat list game yang dijual pada toko", end = "\n")
        print ("5. ubah_game - Untuk mengubah informasi game pada toko game", end = "\n")
        print ("6. ubah_stok - Untuk mengubah stok sebuah game di toko", end = "\n")
        print ("7. search_game_at_store - Untuk mencari sebuah game di toko", end = "\n")
        print ("8. topup - Untuk menambahkan saldo kepada User", end = "\n")
        print ("9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan", end = "\n")
        print ("10. exit - Untuk keluar dari aplikasi")

    
    elif lowercase(role) == 'user':
        # Menampilkan panduan penggunaan sistem untuk user atau pengguna yang belum login

        print ("--- HELP ---", end = "\n")
        print ("1. login - Untuk melakukan login ke dalam sistem", end = "\n")
        print ("2. list_game_toko - Untuk melihat list game yang dijual pada toko", end = "\n")
        print ("3. buy_game - Untuk membeli game", end = "\n")
        print ("4. list_game - Untuk memberikan daftar game yang dimiliki pengguna", end = "\n")
        print ("5. search_my_game - Untuk mendapatkan informasi game sesuai dengan query yang diminta oleh pengguna pada inventory", end = "\n")
        print ("6. search_game_at_store - Untuk mencari sebuah game di toko", end = "\n")
        print ("7. riwayat - Untul melihat riwayat pembelian game", end = "\n")
        print ("8. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan", end = "\n")
        print ("9. exit - Untuk keluar dari aplikasi")


    else:

        print ("--- HELP ---", end = "\n")
        print ("1. login - Untuk melakukan login ke dalam sistem", end = "\n")
        print ("2. exit - Untuk keluar dari aplikasi")
