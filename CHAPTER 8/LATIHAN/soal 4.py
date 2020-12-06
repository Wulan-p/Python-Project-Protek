#menambah dan menghapus data

sayuran = ['bayam', 'kangkung', 'wortel', 'selada']

def tambahSayuran() :
    sayuranAdd = input("Masukkan nama sayur yang ingin ditambahkan : ").lower()
    sayur.append(sayuranAdd)
    return sayur

def hapusSayuran():
    sayuranDel = input("Masukkan nama sayur yang ingin dihapus : ").lower()
    if(sayuranDel in sayuran):
        sayuran.remove(sayuranDel)
    else:
        print("Sayur tidak ada dalam daftar.")
    return sayuran

def liatSayuran() :
    print(Sayuran)

print("Menu: ")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print("Selesai")

while True :
    pilihan = input("Pilihan Anda : ")
    if(pilihan=='A' or pilihan=='a') :
        tambahSayuran()     
    elif(pilihan=='B' or pilihan=='b') :
        hapusSayuran()
    elif(pilihan=='C' or pilihan=='c') :
        liatSayuran()
    elif(pilihan=='SELESAI' or pilihan=='selesai' or pilihan=='Selesai') :
        break   
    else :
        print('Input Invalid')
        continue
