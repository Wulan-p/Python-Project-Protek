def enkripsi(teks, n):
    teksData = list(teks)

    for i in range(len(teksData)):
        if(teksData[i] != ' '):
            teks = ord(teksData[i])
            acak = teks + n
            teksData[i] = chr(acak)
        else :
            continue

    hasil=''.join(teksData)
    return hasil

try: 
    teks = input ("Masukkan teks yang akan enkripsi     : ")
    n = int(input("Masukkan jumlah geseran enkripsi     : "))
    hasil = enkripsi(teks, n)
    
    print("Hasil enkripsian dari teks {0} adalah : {1}".format(teks, hasil))

except ValueError:
    print("Input invalid")
