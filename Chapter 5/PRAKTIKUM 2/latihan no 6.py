
import random
print ("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
random_number = random.randint(0,100)
guess_number = []
allowed_gueses = 50
score = 100
while len(guess_number)<50:
    input_number = input ("guess your number from 0 to 100: ")
    try:
        pass_number = int(input_number)
    except:
        print("it's not a number")
        break
     
    if pass_number < 0 or pass_number > 100:
        print ("your number not in range")
        break
    
    guess_number.append(pass_number)
    if pass_number > random_number:
        print("Hehehe… Bilangan tebakan Anda terlalu besar #{}".format(len(guess_number)))
        score-=2
        continue
    elif pass_number < random_number:
        print("Hehehe… Bilangan tebakan Anda terlalu kecil #{}".format(len(guess_number)))
        score-=2
        continue
    else:
        print("Yeeee… Bilangan tebakan anda BENAR :-)".format(pass_number))
        print("percobaan {} kali".format(len(guess_number)))

    print("score anda= ",score)
    break
