kolom=5
baris=5

i=0
while i in range(5):
    kolom=baris

    j=0
    while (j <= baris ):
        baris=kolom
        baris=baris-1
        print(' * ', end='')
        j+=1
    print('')
    i+=1
