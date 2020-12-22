#mengubah huruf 
#biasa
def ubahHuruf(teks, a, b) :
    huruf = list(teks)
    for i in range(len(huruf)) :     
        if(huruf[i] == a) :
            huruf[i] = b
    ubah = ''.join(huruf)
    return ubah

#replace
def ubahHuruf1(teks, a, b) :
    ubah = teks.replace(a, b)
    return ubah

teks = input("Masukkan teks yang ingin ubah : ")
a = input("Masukkan huruf apa yang ingin diubah : ")
b = input("Ubah {} menjadi : ".format(a))

Hasil = ubahHuruf(teks, a, b)
print(Hasil)

hasil = ubahHuruf1(teks, a, b)
print(hasil)
