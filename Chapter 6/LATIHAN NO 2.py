def starFormation1(n):
    kolom=0
    baris=n

    k=0
    while(k<=n):
        l=0
        while(l<kolom):
            print ("* ", end="")
            l+=1
        print ("")
        k+=1
        kolom += 1

#contoh
starFormation1(5)
print('\n')
def starFormation2(n):
    kolom=n
    baris=n

    k=0
    while(k<=n):
        l=0
        while(l<kolom):
            print ("* ", end="")
            l+=1
        print ("")
        k+=1
        kolom -= 1
        
#contoh
starFormation2(5)
print('\n')
def starFormation3(n):
    kolom=0
    baris=n
    puncak=(n+1)/2


    k=0
    while(k<=n):
        l=0
        while(l<kolom):
            print ("* ", end="")
            l+=1
        print ("")
        k+=1
        kolom += 1


        if(kolom==puncak):
            kolom=puncak
            baris=puncak


            k=0
            while(k<=n):
                l=0
                while(l<kolom):
                    print ("* ", end="")
                    l+=1
                print ("")
                k+=1
                kolom -= 1
            
#contoh
starFormation3(7)
