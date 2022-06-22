# PROGRAM program_bnmo
# Spesifikasi : Main program tugas besar Dasar Pemrograman

# KAMUS
# parser : argparse.ArgumentParser
# saveFolderFound : boolean
# saveFolderPath : string
# matrixUser, matrixGame, matrixRiwayat, matrixKepemilikan : matrix of string
# role, func : string
# useridx : int
# run : boolean


# IMPORT MODUL
import os
import argparse
from Cipher import cipher
from list_game import list_game
from load import load
from listing_game import listing_game
from misc import lowercase, validasi
from register import register
from riwayat import riwayat
from tambahgame import tambah_game
from tictactoe import tictactoe
from MagicConchShell import magic_conch_shell
from SearchGameStore import search_game_at_store
from SearchMyGame import search_my_game
from UbahGame import ubah_game
from buy_game import buy_game
from exit import exit_program
from ubahstok import ubah_stok
from login import login
from topup import topup
from save import save
from help import help

# ALGORITMA

# Input nama folder
parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument("saveFolder",nargs='?')
args = parser.parse_args()

# Guards
if(not args.saveFolder):
    print("Tidak ada nama folder yang diberikan!")
    parser.print_usage()
    parser.exit()

# Mencari path saveFolder
saveFolderFound = False
saveFolderPath = ""
for root, dirs, files in os.walk("."):
    for name in dirs:
        if(name == args.saveFolder):
            saveFolderFound = True
            saveFolderPath = os.path.join(root,name)

if(not saveFolderFound):
    print(f"Folder \"{args.saveFolder}\" tidak ditemukan")
    exit()

# Load data
print("Loading...")
matrixUser, matrixGame, matrixRiwayat, matrixKepemilikan = load(saveFolderPath)

# Menu Utama
print("Selamat datang di antarmuka \"Binomo\"")
role = ''
useridx = -1 # -1 jika tidak ada user login

run = True
while (run):
    func = input('>>> ')
    func = lowercase(func)
    if func == 'register':
        if validasi(role,['admin']):
            register(matrixUser)
    
    elif func == 'login':
        if role == '' and useridx == -1:
            role, useridx = login(matrixUser) 
        else:
            print("Anda sudah login ke dalam sistem.")

    elif func == 'tambah_game':
        if validasi(role,['admin']):
            tambah_game(matrixGame)

    elif func == 'ubah_game':
        if validasi(role,['admin']):
            ubah_game(matrixGame)

    elif func == 'ubah_stok':
        if validasi(role,['admin']):
            ubah_stok(matrixGame)
                
    elif func == 'list_game_toko':
        if validasi(role,['admin', 'user']):
            listing_game(matrixGame)

    elif func == 'buy_game':
        if validasi(role,['user']):
            buy_game(matrixUser,matrixGame,matrixRiwayat,matrixKepemilikan,useridx)
    
    elif func == 'list_game':
        if validasi(role,['user']):
            list_game(str(useridx), matrixKepemilikan, matrixGame)

    elif func == 'search_my_game':
        if validasi(role,['user']):
            search_my_game(str(useridx), matrixKepemilikan, matrixGame)
    
    elif func == 'search_game_at_store':
        if validasi(role,['admin', 'user']):
            search_game_at_store(matrixGame)

    elif func == 'topup':
        if validasi(role,['admin']):
            topup(matrixUser)

    elif func == 'riwayat':
        if validasi(role,['user']):
            riwayat(str(useridx), matrixRiwayat, matrixGame)
    
    elif func == 'help':
        help(role)

    elif func == 'save':
        if validasi(role,['admin','user']):
            save(matrixUser,matrixGame,matrixRiwayat,matrixKepemilikan)

    elif func == 'tictactoe':
        if validasi(role,['admin','user']):
            tictactoe()
    
    elif func == 'kerangajaib':
        if validasi(role,['admin','user']):
            magic_conch_shell()

    elif func == 'cipher':
        if validasi(role,['admin','user']):
            cipher()
    
    elif func == 'exit':
        exit_program(matrixUser,matrixGame,matrixRiwayat,matrixKepemilikan)
        run = False

    else: # perintah salah
        print("Perintah tidak ditemukan. Ketik 'help' untuk melihat daftar perintah.")

    print()
