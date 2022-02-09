#19010011062
#Necmettin Alver

from random import randint

def gemi1yeri(dizi):
    satır=randint(0,alan-1)
    sutun=randint(0,alan-1)
    while dizi[satır][sutun]==1:
        satır = randint(0, alan-1)
        sutun = randint(0, alan-1)
    dizi[satır][sutun]=1
    return [satır,sutun]

def gemi2yeri(dizi):
    kontrol=1
    while kontrol:
        satır = randint(0, alan-1)
        sutun = randint(0, alan-1)
        if dizi[satır][sutun] == 1:
            continue
        if satır<=0 or satır>=9 or sutun<=0 or sutun>=9:
            continue
        satır2=randint(satır-1,satır+1)
        sutun2=randint(sutun-1,sutun+1)
        if satır2==satır and sutun2!=sutun:
                kontrol=0
        elif satır2!=satır and sutun2==sutun:
                kontrol=0
        if dizi[satır2][sutun2]==1:
            kontrol=1
    dizi[satır][sutun] = 1
    dizi[satır2][sutun2] = 1
    return [[satır,sutun],[satır2,sutun2]]

def gemi3yeri(dizi):
        kontrol = 1
        while kontrol:
            satır = randint(0, alan - 1)
            sutun = randint(0, alan - 1)
            if dizi[satır][sutun] == 1:
                continue
            if satır <= 1 or satır >= 8 or sutun <= 1 or sutun >= 8:#2 lide 0 olmaz çünkü yanına gelcek 3 lüde 1 olmaz çünkü2 yanına gelebilir
                continue
            satır2 = randint(satır - 1, satır + 1)
            sutun2 = randint(sutun - 1, sutun + 1)
            if satır2 == satır and sutun2 != sutun:
                kontrol = 0
            elif satır2 != satır and sutun2 == sutun:
                kontrol = 0
            if dizi[satır2][sutun2] == 1:
                kontrol = 1
            if dizi[satır2-1][sutun2] == 1:
                kontrol = 1
            if dizi[satır2+1][sutun2] == 1:
                kontrol = 1
            if dizi[satır2][sutun2-1] == 1:
                kontrol = 1
            if dizi[satır2][sutun2+1] == 1:
                kontrol = 1
        dizi[satır][sutun] = 1
        dizi[satır2][sutun2] = 1
        if satır+1==satır2 and sutun==sutun2:
            dizi[satır+2][sutun] = 1
            satır3=satır+2
            sutun3=sutun
        if satır-1==satır2 and sutun==sutun2:
            dizi[satır - 2][sutun] = 1
            satır3 = satır - 2
            sutun3 = sutun
        if satır==satır2 and sutun-1==sutun2:
            dizi[satır][sutun-2] = 1
            satır3 = satır
            sutun3 = sutun-2
        if satır == satır2 and sutun+1 == sutun2:
            dizi[satır][sutun +2] = 1
            satır3 = satır
            sutun3 = sutun+2
        return [[satır,sutun],[satır2,sutun2],[satır3,sutun3]]

def gemi4yeri(dizi):
        kontrol = 1
        while kontrol:
            satır = randint(0, alan - 1)
            sutun = randint(0, alan - 1)
            if dizi[satır][sutun] == 1:
                continue
            if satır <= 2 or satır >= 7 or sutun <= 2 or sutun >= 7:#2 lide 0 olmaz çünkü yanına gelcek 3 lüde 1 olmaz çünkü2 yanına gelebilir
                continue
            satır2 = randint(satır - 1, satır + 1)
            sutun2 = randint(sutun - 1, sutun + 1)
            if satır2 == satır and sutun2 != sutun:
                kontrol = 0
            elif satır2 != satır and sutun2 == sutun:
                kontrol = 0
            if dizi[satır2][sutun2] == 1:
                kontrol = 1
            if dizi[satır2-1][sutun2] == 1:
                kontrol = 1
            if dizi[satır2+1][sutun2] == 1:
                kontrol = 1
            if dizi[satır2][sutun2-1] == 1:
                kontrol = 1
            if dizi[satır2][sutun2+1] == 1:
                kontrol = 1
            if dizi[satır2-2][sutun2] == 1:
                kontrol = 1
            if dizi[satır2+2][sutun2] == 1:
                kontrol = 1
            if dizi[satır2][sutun2-2] == 1:
                kontrol = 1
            if dizi[satır2][sutun2+2] == 1:
                kontrol = 1
        dizi[satır][sutun] = 1
        dizi[satır2][sutun2] = 1
        if satır+1==satır2 and sutun==sutun2:
            dizi[satır+2][sutun] = 1
            dizi[satır + 3][sutun] = 1
            satır3=satır+2
            satır4=satır+3
            sutun3=sutun
            sutun4=sutun
        if satır-1==satır2 and sutun==sutun2:
            dizi[satır - 2][sutun] = 1
            dizi[satır - 3][sutun] = 1
            satır3 = satır - 2
            satır4 = satır - 3
            sutun3 = sutun
            sutun4 = sutun
        if satır==satır2 and sutun-1==sutun2:
            dizi[satır][sutun-2] = 1
            dizi[satır][sutun - 3] = 1
            satır3 = satır
            satır4 = satır
            sutun3 = sutun-2
            sutun4 = sutun-3
        if satır == satır2 and sutun+1 == sutun2:
            dizi[satır][sutun +2] = 1
            dizi[satır][sutun +3] = 1
            satır3 = satır
            satır4 = satır
            sutun3 = sutun+2
            sutun4 = sutun+3
        return [[satır,sutun],[satır2,sutun2],[satır3,sutun3],[satır4,sutun4]]
def cıkıs ():
        a = int(input("\nOynamaya devam etmek istiyorsanız 1'e \nÇıkmak istiyorsanız 0'a tıklayınız:"))
        if a == 1 or a == 0:
            pass
        else:
            while 1:
                a = int(input("Lütfen geçerli bir sayı giriniz:"))
                if a == 1 or a == 0:
                    break
        return a

a=1
sayacatış=0
anahtar2=0
anahtar=1
while(a):#bu while oyundan çıkmak istemezse tekrar oyun olurturmak içi içini anahtar yapıcam 1 olucak
    while(1):
        alan=int(input("oynamak istediğiniz alan boyutunu giriniz:"))
        if alan<10:
            print("Lütfen 10 ve 10 dan büyük alan giriniz")
        else :
            break

    hak=(alan*alan)//3
    oyunalanı=[]#1 ve 0 larla oyun alanı yarattım kontrolü burdan sağladım
    gostergealanı=[]#kullanıcıya işaretlerle oyun alanını gösterdiğim dizi

    for i in range(0,alan):
        oyunalanı.append([0]*alan)
    for i in range(0,alan):
        gostergealanı.append(["?"]*alan)

    dizigemi1=gemi1yeri(oyunalanı)#fonksiyonla çağırdın 1 yazdırdın oyun alanına
    dizigemi2=gemi2yeri(oyunalanı)
    dizigemi3=gemi3yeri(oyunalanı)
    dizigemi4=gemi4yeri(oyunalanı)

    mod=int(input("\nGizli mod için 1'e\nAçık mod için 2'ye\nBasınız:"))
    if mod == 1 or mod == 2:
        pass
    else:
        while 1:
            mod = int(input("\nLütfen geçerli bir sayı giriniz:"))
            if mod == 1 or mod == 2:
                break
    print("\n")
    if mod==2 :
        for i in oyunalanı:#17 ve 18. satırı görmek için yaptın sonra silersin
            print(i)
    else:
        for i in gostergealanı:
            print(i)

    print("\nHak sayınız :{}".format(hak))

    for i in range(0,hak):
        tahminsatır=int(input("\nvurmak istediğiniz noktasının satır sayısını giriniz:"))
        tahminsutun = int(input("vurmak istediğiniz noktasının sutun sayısını giriniz:"))

        print("\n==================================================================\n")
        if oyunalanı[tahminsatır-1][tahminsutun-1]==1:
            gostergealanı[tahminsatır-1][tahminsutun-1]="X"
            oyunalanı[tahminsatır-1][tahminsutun-1]=0
            sayacatış=sayacatış+1
            if mod==1:
                for i in gostergealanı:
                    print(i)
            print("\nTebrikler bir gemi vurdunuz.")

            if tahminsatır-1==dizigemi1[0] and tahminsutun-1==dizigemi1[1] :
                print("Tebrikler bir gemi batırdınız.")

            elif ((tahminsatır - 1 == dizigemi2[0][0] and tahminsutun - 1 == dizigemi2[0][1] and oyunalanı[dizigemi2[1][0]][dizigemi2[1][1]]==0) or (tahminsatır - 1 == dizigemi2[1][0] and tahminsutun - 1 == dizigemi2[1][1] and oyunalanı[dizigemi2[0][0]][dizigemi2[0][1]]==0)):
                print("Tebrikler bir gemi batırdınız.")#2 birimlik

            elif ((tahminsatır - 1 == dizigemi3[0][0] and tahminsutun - 1 == dizigemi3[0][1] and oyunalanı[dizigemi3[1][0]][dizigemi3[1][1]]==0 and oyunalanı[dizigemi3[2][0]][dizigemi3[2][1]]==0)
            or (tahminsatır - 1 == dizigemi3[1][0] and tahminsutun - 1 == dizigemi3[1][1] and oyunalanı[dizigemi3[0][0]][dizigemi3[0][1]]==0 and oyunalanı[dizigemi3[2][0]][dizigemi3[2][1]]==0)
            or (tahminsatır - 1 == dizigemi3[2][0] and tahminsutun - 1 == dizigemi3[2][1] and oyunalanı[dizigemi3[1][0]][dizigemi3[1][1]]==0 and oyunalanı[dizigemi3[0][0]][dizigemi3[0][1]]==0)):
                print("Tebrikler bir gemi batırdınız.")#3birimliğin etrafını kontrol ettirdim 1 var mı diye

            elif ((tahminsatır - 1 == dizigemi4[0][0] and tahminsutun - 1 == dizigemi4[0][1] and oyunalanı[dizigemi4[1][0]][dizigemi4[1][1]]==0 and oyunalanı[dizigemi4[2][0]][dizigemi4[2][1]]==0 and oyunalanı[dizigemi4[3][0]][dizigemi4[3][1]]==0)or
            (tahminsatır - 1 == dizigemi4[1][0] and tahminsutun - 1 == dizigemi4[1][1] and oyunalanı[dizigemi4[0][0]][dizigemi4[0][1]]==0 and oyunalanı[dizigemi4[2][0]][dizigemi4[2][1]]==0 and oyunalanı[dizigemi4[3][0]][dizigemi4[3][1]]==0) or
            (tahminsatır - 1 == dizigemi4[2][0] and tahminsutun - 1 == dizigemi4[2][1] and oyunalanı[dizigemi4[1][0]][dizigemi4[1][1]]==0 and oyunalanı[dizigemi4[0][0]][dizigemi4[0][1]]==0 and oyunalanı[dizigemi4[3][0]][dizigemi4[3][1]]==0) or
            (tahminsatır - 1 == dizigemi4[3][0] and tahminsutun - 1 == dizigemi4[3][1] and oyunalanı[dizigemi4[1][0]][dizigemi4[1][1]]==0 and oyunalanı[dizigemi4[2][0]][dizigemi4[2][1]]==0 and oyunalanı[dizigemi4[0][0]][dizigemi4[0][1]]==0)):
                print("Tebrikler bir gemi batırdınız.")#4 birimlik gemilerin etrafını kontrol ettirdim 1 var mı diye

        else :
            gostergealanı[tahminsatır-1][tahminsutun-1] = "*"
            if mod == 1:
                for i in gostergealanı:
                    print(i)
            print("\nMalesef bir gemi vuramadınız.")
            sayacatış=sayacatış+1
            continue

        if (oyunalanı[dizigemi1[0]][dizigemi1[1]]==0 and oyunalanı[dizigemi2[0][0]][dizigemi2[0][1]]==0 and oyunalanı[dizigemi2[1][0]][dizigemi2[1][1]]==0 and oyunalanı[dizigemi3[0][0]][dizigemi3[0][1]]==0\
                and oyunalanı[dizigemi3[1][0]][dizigemi3[1][1]]==0 and oyunalanı[dizigemi3[2][0]][dizigemi3[2][1]]==0 and oyunalanı[dizigemi4[1][0]][dizigemi4[1][1]]==0 and oyunalanı[dizigemi4[2][0]][dizigemi4[2][1]]==0
                and oyunalanı[dizigemi4[3][0]][dizigemi4[3][1]]==0 and oyunalanı[dizigemi4[0][0]][dizigemi4[0][1]]==0):
            anahtar2 = 1
            anahtar = 0

        if anahtar2:
            print("Tebrikler tüm gemileri batırdınız.")
            puan=hak-sayacatış
            print("Puanınız={}".format(puan))
            break

    if (anahtar):
        print("Malesef kaybettiniz.")


    b = cıkıs()
    if b == 0:
        a = 0
        break
    else:
        print("\n")



