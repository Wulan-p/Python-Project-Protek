bindo=int(input("Masukan Nilai Bahasa Indonesia: "))
ipa  =int(input("Masukan Nilai IPA             : "))
mtk  =int(input("Masukan Nilai Matematika      : "))
sttus=(input("Status Kelulusan              : "))   
if (bindo>-60) and (ipa>-60) and (mtk>-70) :
    print("TIDAK LULUS")
else :
    print("LULUS")
hemmc=(input("Sebab                         : "))
if (bindo>-60) and (ipa>-60) and (mtk>-70) :
    print("Nilai Bahasa Indonesia kurang dari 60")
    print("Nilai Bahasa Matematikanya kurang dari 70")
else:
    print("Nilai Bahasa Indonesia lebih dari 60")
    print("Nilai Matematikanya lebih dari 70")
    
