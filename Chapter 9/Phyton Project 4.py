#menghasilkan list dengan elemen berbeda yg berupa pengacakan

import random

def randomstring(x,n) :
    randomlist = []
    
    for i in range(n) :
        a = list(random.sample(x, len(x)))
        b = ''.join(a)
        
        if(b in randomlist) :
            continue
        else :
            randomlist.append(b)
            print(b)

            
kata = input("Masukkan kata yang ingin diacak : ")
jumlah = int(input("Masukkan jumlah hasil acakan yang diinginkan : "))

randomstring(kata,jumlah)
