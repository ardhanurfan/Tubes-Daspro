# Cipher Program
# Spesifikasi : Mengenkripsi dan Mendekripsi kata yang dimasukan

# key encryption
def key1(a,b,x) :
    return (a*x+b)%26

# Function untuk encryption
def enc(kata_awal,a,b) :
    char = ''
    for i in kata_awal :
        if i >= 'a' and i <= 'z':
            char += chr(key1(a,b,ord(i)-97)+97)
        else :
            char += chr(key1(a,b,ord(i)-65)+65)
    return char 

# Inverse modulo
def inversemod(x,y) :
    hasil = 0
    for i in range(y+1) :
        if ((x*i)%y==1) :
            hasil = i 
    return hasil

# key decryption
def key2(a,b,x) :
    return (inversemod(a,26)*(x-b))%26
    

# Function untuk decryption
def dec(ciphered,a,b) :
    char = ''
    for i in ciphered :
        if i >= 'a' and i <= 'z':
            char += chr(key2(a,b,ord(i)-97)+97)
        else :
            char += chr(key2(a,b,ord(i)-65)+97)
    return char

def cipher():
    print("""
Pilihan:
a. Enkripsi
b. Dekripsi
""")

    cek = False
    while not cek:
        pilih = input("Masukan pilihan: ")
        if pilih == 'a' or pilih == 'A' or pilih == 'b' or pilih == 'B':
            cek = True
        else:
            print('Masukan tidak valid. Coba lagi!')
    
    if pilih == 'a' or pilih == 'A':
        password = input("Masukan kata semula: ")
        print('Kata Ciphered:', enc(password, 9, 3))
    else:
        ciphered = input("Masukan kata Ciphered: ")
        print('Kata semula:', dec(ciphered, 9, 3))