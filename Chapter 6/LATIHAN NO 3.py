def faktorial(n):
    faktorial1=1
    while(n>0):
        faktorial1=faktorial1*n
        n-=1
    return faktorial1

def kombinasi(a,b):
    c=a-b
    hasil=faktorial(a)/(faktorial(c)*faktorial(b))
    print(hasil)

def permutasi(a,b):
    c=a-b
    hasil=faktorial(a)/faktorial(c)
    print(hasil)

#A
a=5
b=3
permutasi(a,b)


#B
a=10
b=7
kombinasi(a,b)
