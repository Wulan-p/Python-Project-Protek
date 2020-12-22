buah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}

def hargaRata2(buah):
    jumlah=0
    n=0
    for i,j in buah.items():
        jumlah+=j
        n+=1
    rata2 = jumlah/n
    return rata2

hasil=hargaRata2(buah)

print("Harga rata-rata buah adalah", hasil)
