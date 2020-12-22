#menentukan harga total

buah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}

def jumlahBuah():
    jumlah =int(input('Berapa Kg        : '))
    print("-------------------------")
    print("Total Harga : ", buah.get(nama, 0)*jumlah)

print("Buah yang tersedia : ")

for x,y in buah.items() :
    print("- ", x, ":", y)

while True :
    nama = input("Buah yang dibeli : ")
    
    if(nama not in buah.keys()) :
        print("Buah sedang kosong")
        continue

    else :
        while True :
            try :
                jumlahBuah()
                break
            except ValueError :
                continue
        break
