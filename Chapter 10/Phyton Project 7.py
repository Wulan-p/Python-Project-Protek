
def enkripsi(teks, n) :
    teksData = list(teks)

    for i in range(len(teksData)) :
        if(teksData[i] != ' ') :
            teks = ord(teksData[i])
            acak = teks - geseran
            teksData[i] = chr(acak)

        else :
            continue

    hasil = ''.join(teksData)
    return hasil

try : 
    teks = input ("Masukkan teks hasil enkripsi     : ")
    geseran = int(input("Masukkan jumlah geseran enkripsi : "))
    hasil = enkripsi(teks, geseran)
    
    print("Teks asli dari {0} adalah : {1}".format(teks, hasil))

except ValueError :
    print("Inputan invalid")
