#n bil ganjil
def bintang(n) :
    top = int(n/2 + 1)
    i=1
    for i in range(0, n+1) :
        formasi = "*" * (1 + 2*(i-1))
        print(formasi.center(25))
        if(i == top) :
            for i in range(top - 1, 0, -1) :
                formasi = "*" * (1 + 2*(i-1))
                print(formasi.center(25))
            break

#exp
bintang(7)
