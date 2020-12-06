try :
    file=input('Masukkan nama file : ')
    buka=open(file, 'a')
    
    data=True
    while(data==True):
        tambahan = input('Masukkan data yang mau ditambahkan : ')
        file.write(' ' + tambahan)

        opsi=input('Mau lagi (y/n) : ')
        if (opsi=='y'):
            data = True
        elif (opsi=='n'):
            data = False
        else :
            print('Input tidak valid')
            break
    file.close()

except FileNotFoundError :
    print('File tidak dapat ditemukan')
