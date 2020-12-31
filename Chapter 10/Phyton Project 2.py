file = open('fileDataMhs.txt', 'a+')

i = True
while ( i == True) :
    nim = input("Masukkan NIM : ")
    namaMhs = input("Masukkan Nama Mhs : ")
    alamat = input("Masukkan Alamat : ")

    file.write(nim+"|"+namaMhs+"|"+alamat+"\n")  
    ulang = input("Silakan input ulang (y/n) : ")
    
    if (ulang == "y"):
        i = True
    elif  (ulang == "n"):
        i = False
    else :
        print ("Input invalid")
        continue
    
file.seek(0,0)
isi = file.read()
print (isi)
file.close()
