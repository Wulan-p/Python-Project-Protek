print('--------------------------')
print(' PROGRAM HITUNG RATA-RATA  ')
print('--------------------------')
    
a = True
jmlhX = 0
b = 0
    
while(a == True):
    try :
        bil = int(input('Masukkan bilangan bulat : '))
        jmlhX += bil
        b += 1
        
        opsi = input('Lagi (y/n): ')
        
        if(opsi=='y'):
            a = True
            
        elif(opsi=='n'):
            a = False
            
        else:
            print('Input invalid')
            break

    except ValueError:
            print('Bukan bilangan bulat')
            continue
    
rata2 = jmlhX/b
print(' ')
print('Rata - ratanya adalah  : ', rata2)
