try:
    file = input('Masukkan nama file :')
    print('Isi File',file,'adalah :')
    print(open (file,'r').read())
except FileNotFoundError:
    print('Maaf File Tidak Ditemukan')
    print("Maaf penulisan file salah")
except UnicodeDecodeError:
    print('Maaf File Tidak Dapat Diakses')
