#mencetak formasi bintang
def bintang(n) :
    i=1
    for i in range(0, n+1) :
        formasi = "*" * (1 + (i-1)*2)
        print(formasi.center(25))


#exp
bintang(4)

