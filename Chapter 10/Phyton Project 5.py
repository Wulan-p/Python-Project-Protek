file = open('dataBilangan.txt', 'r')
fileHasil = open('hasilPenjumlahan.txt', 'a')
line = file.readlines()

for i in range(len(line)) :
    a = line[i].split('|')
    tambah=int(a[0])+int(a[1])
    hasil=str(tambah)
    fileHasil.write(hasil)
    fileHasil.write('\n')
fileHasil.close()

print ("Silahkan buka hasilPenjumlahan.txt untuk melihat hasil")
