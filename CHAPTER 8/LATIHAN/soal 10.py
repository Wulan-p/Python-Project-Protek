#menentukan harga total dengan penambahan pembelian

buah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}

def jumlahBuah():
    jumlah =int(input('Berapa Kg        : '))
    print("-------------------------")
    harga=buah.get(nama, 0)*jumlah
    return harga

print("Buah yang tersedia : ")

for x,y in buah.items() :
    print("- ", x, ":", y)

totalHarga=[]

i=True
while (i==True):
    nama = input("Buah yang dibeli : ").lower()
    
    if(nama not in buah.keys()) :
        print("Maaf, buah sedang kosong")
        continue

    else :
        try :
            harga=jumlahBuah()
            totalHarga.append(harga)

            lanjut=input("Ingin membeli buah yang lain? (y/n) : ")
            if(lanjut=="y"):
                i=True
                print("----------------------------------------")
            elif(lanjut=="n"):
                i=False
            else:
                print("Input invalid")
                break
        except ValueError:
            print("Input invalid")
            continue

print("----------------------------------------")
print ("Total Harga : ",sum(totalHarga))

