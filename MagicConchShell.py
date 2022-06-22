import time

def random():
    # Menghasilkan angka random dari waktu lokal
    # I.S. localtime() terdefinisi
    # F.S. mengembalikan angka random

    # Kamus Lokal
    # waktu : time.localtime {waktu lokal}
    # seconds : waktu.tm_sec {detik lokal}
    # min : waktu.tm_min {menit lokal}
    # hour : waktu.tm_hour {jam lokal}
    # day : waktu.tm_mday {hari lokal}
    # month : waktu.tm_mon {bulan lokal}
    # tahun : waktu.tm_year {tahun lokal}
    # angka_random : integer {hasil angka random}
    
    # Algoritma
    waktu = time.localtime()

    seconds = waktu.tm_sec
    min = waktu.tm_min
    hour = waktu.tm_hour
    day = waktu.tm_mday
    month = waktu.tm_mon
    year = waktu.tm_year

    angka_random = ((seconds*min)**hour)+day+month+year
    angka_random = angka_random%6
    return angka_random

def magic_conch_shell ():
    # Prosedur program kerang ajaib
    # I.S. angka random terinisalisasi, beserta input pertanyaan(string)
    # F.S. menampilkan jawaban secara acak sesuai list jawaban

    # Kamus Lokal
    # answer : array of string {daftar jawaban}
    # question : string {input pertanyaan}
    # function random() => integer
    #    {I.S. localtime() terdefinisi
    #     F.S. mengembalikan angka random}

    # Algoritma
    answer = ['Ya', 'Tidak', 'Mungkin', 'Bisa Jadi', 'Tentunya', 'Tidak Mungkin']
    question = input("Apa pertanyaanmu? ")

    print(answer[random()])
