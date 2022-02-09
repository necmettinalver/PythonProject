veri = ["numara", "ad", "soyad", "yas", "aylık", "boy", "kilo", "boyun", "omuz", "gogus","kol", "bel", "kalca", "bacak"]

def listeleme():  # dosyamızın içindeki değerleri sözlüğe aktarıyor ve kullanıcı yada son numarayı gönderiyor
    def okuma():
        with open("19010011062.txt", "r+") as sporcudosya:
            liste = sporcudosya.readlines()
            format(liste)

    def format(liste):
        for deger in liste:
            deger2 = deger.split("\t")
            data = dict()
            for ind in range(1, len(deger2)):
                data[veri[ind]] = deger2[ind]
                kullanici[deger2[0]] = data

    kullanici = dict()
    okuma()
    a=0

    if len(kullanici) == 0:
        a = 0
    else:
        for numara in kullanici.keys():
            a = numara

    return a, kullanici

def listele():  # dosyamızın içindeki değerleri listeleyip yazmaya yarıyor
    def okuma():
        with open("19010011062.txt", "r+") as sporcudosya:
            liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
            format(liste)

    def format(liste):
        for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
            deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
            data = dict()
            for ind in range(1, len(deger2)):  # satırdaki kelimeleri sozluk olusturup icine atiyor
                data[veri[ind]] = deger2[ind]
                kullanici[deger2[0]] = data

    kullanici = dict()
    okuma()
    print("")

    for numara in kullanici.keys():  # kullanıcının keylerini yani numaraları dolaşıyor
        print("Sporcu numarası={}".format(numara), end=" ")

        for bilgi in kullanici[numara].keys():  # her numaranin elemanlarini yani değerlerini yazdırıyor
            print("{}={}  ".format(bilgi, kullanici[numara][bilgi]), end=" ")
    print("\nListeleme tamamlandı.\nMenüye yönlendiriliyorsunuz...")


def menu():
    anahtar = 1

    while anahtar:
        print("\n========================================")
        print("""Fitness salonuna hoşgeldiniz
            ---------------------
            1.Yeni sporcu ekle
            2.Sporcu sil
            3.Sporcu Sorgula
            4.Sporcu bilgi guncelleme
            5.Listele
            6.Vucut kitle indeksi hesabı
            7.Kalori hesabı
            8.Ogrenci olculeri
            9.Ucret hesabı
            10.Cıkıs
            ----------------------""")
        secim = input("Yapmak istediginiz islemi seciniz :")
        print("========================================")

        if secim == "1":
            sonnum, b = listeleme()
            sonnum = int(sonnum)
            sonnum = sonnum + 1
            sonnum = str(sonnum)
            ogrenciekle(sonnum)
        elif secim == "2":
            ogrencisil()
        elif secim == "3":
            ogrenciarayaz()
        elif secim == "4":
            guncelleme()
        elif secim == "5":
            listele()
        elif secim == "6":
            vki()
        elif secim == "7":
            kalori()
        elif secim == "8":
            olculeri()
        elif secim == "9":
            ucret()
        elif secim == "10":
            anahtar = cikis()
        else:
            print("Yanlış rakam girdiniz.Tekrarlayınız")


def ogrenciekle(num):
    sporculiste = []
    ad = input("Sporcunun adını giriniz :")
    soyad = input("Sporcunun soyadını giriniz :")
    yas = input("Sporcunun yaşını giriniz :")
    aylik = input("Spor aylik kayit suresini giriniz :")
    boy = input("Boyunu giriniz (cm) :")
    kilo = input("Kilosunu giriniz (kg) :")
    boyun = input("Boyun olcusunu giriniz:")
    omuz = input("Omuz olcusunu giriniz:")
    gogus = input("Gogus olcusunu giriniz:")
    kol = input("Kol olcusunu giriniz:")
    bel = input("Bel olcusunu giriniz :")
    kalca = input("Kalca olcusunu giriniz :")
    bacak = input("Bacak olcusunu giriniz :")
    a = str(num)
    sporculiste.append(a + "\t")
    sporculiste.append(ad + "\t")
    sporculiste.append(soyad + "\t")
    sporculiste.append(yas + "\t")
    sporculiste.append(aylik + "\t")
    sporculiste.append(boy + "\t")
    sporculiste.append(kilo + "\t")
    sporculiste.append(boyun + "\t")
    sporculiste.append(omuz + "\t")
    sporculiste.append(gogus + "\t")
    sporculiste.append(kol + "\t")
    sporculiste.append(bel + "\t")
    sporculiste.append(kalca + "\t")
    sporculiste.append(bacak + "\n")  # txtde alta almak için
    with open("19010011062.txt", "a+") as sporcudosya:
        sporcudosya.writelines(sporculiste)
    print("\nSporcu Başarıyla eklenmiştir.\nMenüye yönlendiriliyorsunuz...")


def ogrencisil():  # önce dosyayı okuyor listeye atıyor listeden elemanı siliyor
    print("Silmek icin")
    b = ogrenciara()
    kullanici = []
    gecicilist = []

    if b != 0:
        with open("19010011062.txt", "r+") as sporcudosya:
            liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor

        b = int(b)
        b = b - 1
        liste.pop(b)  # silmek istedigim kullanıcıyı sildim
        print("\nSporcu başarıyla silinmiştir.\nMenüye yönlendiriliyorsunuz...")

        with open("19010011062.txt", "w+") as sporcudosya:
            sporcudosya.writelines(liste)

        def okuma():
            with open("19010011062.txt", "r+") as sporcudosya:
                liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
                format(liste)

        def format(liste):
            for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
                deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
                data = []
                for ind in range(0, len(deger2)):  # satırdaki kelimeleri listeye icine atiyor
                    data.append(deger2[ind])
                kullanici.append(data)  # listeyi liste içine atıyorum

        okuma()

        with open("19010011062.txt", "w+") as sporcudosya:
            pass

        for i in range(0, len(kullanici)):
            if i >= b:
                c = i + 1
                c = str(c)
                gecicilist.append(c + "\t")
                gecicilist.append(kullanici[i][1] + "\t")
                gecicilist.append(kullanici[i][2] + "\t")
                gecicilist.append(kullanici[i][3] + "\t")
                gecicilist.append(kullanici[i][4] + "\t")
                gecicilist.append(kullanici[i][5] + "\t")
                gecicilist.append(kullanici[i][6] + "\t")
                gecicilist.append(kullanici[i][7] + "\t")
                gecicilist.append(kullanici[i][8] + "\t")
                gecicilist.append(kullanici[i][9] + "\t")
                gecicilist.append(kullanici[i][10] + "\t")
                gecicilist.append(kullanici[i][11] + "\t")
                gecicilist.append(kullanici[i][12] + "\t")
                gecicilist.append(kullanici[i][13])


            else:
                gecicilist.append(kullanici[i][0] + "\t")
                gecicilist.append(kullanici[i][1] + "\t")
                gecicilist.append(kullanici[i][2] + "\t")
                gecicilist.append(kullanici[i][3] + "\t")
                gecicilist.append(kullanici[i][4] + "\t")
                gecicilist.append(kullanici[i][5] + "\t")
                gecicilist.append(kullanici[i][6] + "\t")
                gecicilist.append(kullanici[i][7] + "\t")
                gecicilist.append(kullanici[i][8] + "\t")
                gecicilist.append(kullanici[i][9] + "\t")
                gecicilist.append(kullanici[i][10] + "\t")
                gecicilist.append(kullanici[i][11] + "\t")
                gecicilist.append(kullanici[i][11] + "\t")
                gecicilist.append(kullanici[i][13])

            with open("19010011062.txt", "a+") as sporcudosya:
                sporcudosya.writelines(gecicilist)
            gecicilist = []


def ogrenciara():
    anahtar1=1
    while anahtar1 :
        arad = input("Aramak istediginiz kullanıcının adını giriniz:")
        arasoy = input("Aramak isteginiz kullanıcının soyadını giriniz:")
        a, kullanici = listeleme()

        i = 0
        anahtar1=0
        for numara in kullanici.keys():  # kullanıcının keylerini yani numaraları dolaşıyor
            if kullanici[numara]["ad"] == arad and kullanici[numara]["soyad"] == arasoy:
                i = numara
        print("\nTaranıyor.\nLütfen bekleyiniz...")

        if i == 0:
            print("\nKullanıcı bulunamadı.")
            while True :
                tekrar = input("Tekrar denemek istiyorsanız = 1"
                               "\nİstemiyorsanız =2 Tuşlayınız.\nSeçiminiz :")

                if tekrar == "1":
                    anahtar1=1
                    break
                elif tekrar == "2":
                    anahtar1 = 0
                    print("Menüye yönlendiriliyorsunuz...")
                    break
                else:
                    print("\nHatalı tuşlama yaptınız.")
            print("")

    return i


def ogrenciarayaz():
    anahtar1=1
    while anahtar1:
        print("Sorgulama yapmak için")
        arad = input("Aramak istediginiz kullanıcının adını giriniz:")
        arasoy = input("Aramak isteginiz kullanıcının soyadını giriniz:")
        a, kullanici = listeleme()

        i = 0
        for numara in kullanici.keys():  # kullanıcının keylerini yani numaraları dolaşıyor
            if kullanici[numara]["ad"] == arad and kullanici[numara]["soyad"] == arasoy:
                i = numara

        sayac = 0
        print("\nTaranıyor.\nLütfen bekleyiniz...")
        if i != 0:
            anahtar1=0
            print("\nKullanıcı bulundu\nBilgileri yazdırılıyor...\n")
            for bilgi in kullanici[i].keys():  # her numaranin elemanlarini yani değerlerini yazdırıyor
                print("{}={}  ".format(bilgi, kullanici[i][bilgi]), end=" ")
                if sayac >= 5:
                    break
                sayac = sayac + 1
            print("\n\nSporcu bilgileri gösterildi.\nMenüye yönlendiriliyorsunuz...")

        if i == 0:
            print("\nKullanıcı bulunamadı.")
            while True:
                tekrar = input("Tekrar denemek istiyorsanız = 1"
                               "\nİstemiyorsanız =2 Tuşlayınız.\nSeçiminiz :")

                if tekrar== "1":
                    break
                elif tekrar == "2":
                    anahtar1 = 0
                    print("Menüye yönlendiriliyorsunuz...")
                    break
                else:
                    print("\nHatalı tuşlama yaptınız.")
            print("")

    return i


def olculeri():
    print("Olculerini gormek icin")
    a = ogrenciara()
    kullanici = []  # burda ödevde istenilen liste şartınıda uygulamış oluyorum

    def okuma():
        with open("19010011062.txt", "r+") as sporcudosya:
            liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
            format(liste)

    def format(liste):
        for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
            deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
            data = []
            for ind in range(0, len(deger2)):  # satırdaki kelimeleri listeye icine atiyor
                data.append(deger2[ind])
            kullanici.append(data)  # listeyi liste içine atıyorum

    okuma()
    a = int(a)

    if a != 0:
        print("Kullanıcının boyun olcusu = {}".format(kullanici[a - 1][7]))
        print("Kullanıcının omuz olcusu = {}".format(kullanici[a - 1][8]))
        print("Kullanıcının gogus olcusu = {}".format(kullanici[a - 1][9]))
        print("Kullanıcının kol olcusu = {}".format(kullanici[a - 1][10]))
        print("Kullanıcının bel olcusu = {}".format(kullanici[a - 1][11]))
        print("Kullanıcının kalca olcusu = {}".format(kullanici[a - 1][12]))
        print("Kullanıcının bacak olcusu = {}".format(kullanici[a - 1][13]))

    print("Ölçü gösterimi tamamlandı.\nMenüye yönlendiriliyorsunuz...")


def guncelleme():
    print("Guncelleme yapmak için ")
    b = ogrenciara()
    kullanici = []
    gecicilist = []

    if b != 0:
        print("\nKullanıcı bulundu\nBilgileri isteniyor...")

        def okuma():
            with open("19010011062.txt", "r+") as sporcudosya:
                liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
                format(liste)

        def format(liste):
            for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
                deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
                data = []
                for ind in range(0, len(deger2)):  # satırdaki kelimeleri listeye icine atiyor
                    data.append(deger2[ind])
                kullanici.append(data)  # listeyi liste içine atıyorum

        okuma()
        b = int(b)
        b = b - 1

        print("\nSporcunun")
        yas=input("Yaşını giriniz :")
        aylik = input("Spor aylik kayit suresini giriniz :")
        boy = input("Boyunu giriniz :")
        kilo = input("Kilosunu giriniz :")
        boyun = input("Boyun olcusunu giriniz:")
        omuz = input("Omuz olcusunu giriniz:")
        gogus = input("Gogus olcusunu giriniz:")
        kol = input("Kol olcusunu giriniz:")
        bel = input("Bel olcusunu giriniz :")
        kalca = input("Kalca olcusunu giriniz :")
        bacak = input("Bacak olcusunu giriniz :")

        kullanici[b][3] = yas
        kullanici[b][4] = aylik
        kullanici[b][5] = boy
        kullanici[b][6] = kilo
        kullanici[b][7] = boyun
        kullanici[b][8] = omuz
        kullanici[b][9] = gogus
        kullanici[b][10] = kol
        kullanici[b][11] = bel
        kullanici[b][12] = kalca
        kullanici[b][13] = bacak

        with open("19010011062.txt", "w+") as sporcudosya:
            pass

        for i in range(0, len(kullanici)):
            if i == b:
                gecicilist.append(kullanici[i][0] + "\t")
                gecicilist.append(kullanici[i][1] + "\t")
                gecicilist.append(kullanici[i][2] + "\t")
                gecicilist.append(kullanici[i][3] + "\t")
                gecicilist.append(kullanici[i][4] + "\t")
                gecicilist.append(kullanici[i][5] + "\t")
                gecicilist.append(kullanici[i][6] + "\t")
                gecicilist.append(kullanici[i][7] + "\t")
                gecicilist.append(kullanici[i][8] + "\t")
                gecicilist.append(kullanici[i][9] + "\t")
                gecicilist.append(kullanici[i][10] + "\t")
                gecicilist.append(kullanici[i][11] + "\t")
                gecicilist.append(kullanici[i][12] + "\t")
                gecicilist.append(kullanici[i][13] + "\n")
            else:
                gecicilist.append(kullanici[i][0] + "\t")
                gecicilist.append(kullanici[i][1] + "\t")
                gecicilist.append(kullanici[i][2] + "\t")
                gecicilist.append(kullanici[i][3] + "\t")
                gecicilist.append(kullanici[i][4] + "\t")
                gecicilist.append(kullanici[i][5] + "\t")
                gecicilist.append(kullanici[i][6] + "\t")
                gecicilist.append(kullanici[i][7] + "\t")
                gecicilist.append(kullanici[i][8] + "\t")
                gecicilist.append(kullanici[i][9] + "\t")
                gecicilist.append(kullanici[i][10] + "\t")
                gecicilist.append(kullanici[i][11] + "\t")
                gecicilist.append(kullanici[i][12] + "\t")
                gecicilist.append(kullanici[i][13])

            with open("19010011062.txt", "a+") as sporcudosya:
                sporcudosya.writelines(gecicilist)
            gecicilist = []

    print("\nGüncellenme tamamlandı.\nMenüye yönlendiriliyorsunuz...")


def kalori():
    print("Kalori hesabı yapmak için")
    a = ogrenciara()
    kullanici=[]
    if a != 0:
        a = int(a)
        a=a-1
        def okuma():
            with open("19010011062.txt", "r+") as sporcudosya:
                liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
                format(liste)

        def format(liste):
            for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
                deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
                data = []
                for ind in range(0, len(deger2)):  # satırdaki kelimeleri listeye icine atiyor
                    data.append(deger2[ind])
                kullanici.append(data)  # listeyi liste içine atıyorum

        okuma()

        yas = kullanici[a][3]
        boy = kullanici[a][5]
        kilo = kullanici[a][6]
        yas = int(yas)
        kilo = int(kilo)
        boy = int(boy)

        def hareket ():
            while True :
                hareketsec = input("\nMasa başı ve durağan bir yaşamınız varsa = 1\nHafif düzeyde hareketliyseniz = 2"
                                   "\nOrta düzeyde hareketli olup çok oturmuyorsanız = 3"
                                   "\nYüksek düzeyde aktifseniz ve düzenli spor yapıyorsanız = 4"
                                   "\nSeçiminizi karşısındaki numarayı tuşlayarak yapınız :")

                if hareketsec == "1":
                    aktivite = 1.2
                    return aktivite
                    break

                elif hareketsec == "2":
                    aktivite = 1.3
                    return aktivite
                    break

                elif hareketsec == "3":
                    aktivite = 1.4
                    return aktivite
                    break

                elif hareketsec == "4":
                    aktivite = 1.5
                    return aktivite
                    break

                else :
                    print("Lütfen doğru tuşlayınız.")


        while True:
            cinsiyet = input("\nSporcunun cinsiyetini\nErkek = E\nKadın = K \nolacak şekilde tuşlayınız :")
            if cinsiyet == "E" or cinsiyet == "e":

                bmh=66.5 + (13.75 * kilo) + (5 * boy) - (6.77 * yas)
                aktivite=hareket()
                mh=bmh*aktivite
                mh=mh+mh*0.1

                print("\nYaşamaya devam etmesi için alması gereken kalori : {:.2f}".format(bmh))
                print("Kilosunu korumak için alması gereken kalori : {:.2f}".format(mh))
                print("Kilo almak için alması gereken en az kalori : {:.2f}".format(mh + 200))
                print("Kilo vermek için alması gereken en yüksek kalori : {:.2f}".format(mh - 200))
                break

            elif cinsiyet == "K" or cinsiyet == "k":

                bmh=655.1 + (9.56 * kilo) + (1.85 * boy) - (4.67 * yas)
                aktivite = hareket()
                mh = bmh * aktivite
                mh = mh + mh * 0.1

                print("\nYaşamaya devam etmesi için alması gereken kalori : {:.2f}".format(bmh))
                print("Kilosunu korumak için alması gereken kalori : {:.2f}".format(mh))
                print("Kilo almak için alması gereken en az kalori : {:.2f}".format(mh + 200))
                print("Kilo vermek için alması gereken en yüksek kalori : {:.2f}".format(mh - 200))
                break

            else:
                print("Lütfen doğru tuşlayınız.")
        print("Kaloriler yazdırıldı.Menüye yönlendiriliyorsunuz...")

def vki () :
    print("Vücut kitle indeksi hesabı yapmak için")
    a = ogrenciara()
    kullanici = []
    if a != 0:
        a = int(a)
        a=a-1

        def okuma():
            with open("19010011062.txt", "r+") as sporcudosya:
                liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
                format(liste)

        def format(liste):
            for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
                deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
                data = []
                for ind in range(0, len(deger2)):  # satırdaki kelimeleri listeye icine atiyor
                    data.append(deger2[ind])
                kullanici.append(data)  # listeyi liste içine atıyorum

        okuma()

        boy = kullanici[a][5]
        kilo = kullanici[a][6]
        kilo = int(kilo)
        boy = int(boy)

        hesapvki=kilo/((boy/100)*(boy/100))

        while True:
            cinsiyet = input("\nSporcunun cinsiyetini\nErkek = E\nKadın = K \nolacak şekilde tuşlayınız :")

            if hesapvki <= 18.5:
                print("\nSporcunun vücut kitle indeksi :{:.2f}".format(hesapvki))
                print("İdeal kilonun altında.")
            elif 18.5 < hesapvki <= 25:
                print("\nSporcunun vücut kitle indeksi :{:.2f}".format(hesapvki))
                print("Sporcu İdeal Kilo aralığında.")
            elif 25 < hesapvki <= 30:
                print("\nSporcunun vücut kitle indeksi :{:.2f}".format(hesapvki))
                print("Sporcu İdeal kilonuzun üstünde.")
            elif 30 < hesapvki <= 40:
                print("\nSporcunun vücut kitle indeksi :{:.2f}".format(hesapvki))
                print("Sporcu Obez 1 seviyesinde.")
            else:
                print("\nSporcunun vücut kitle indeksi :{:.2f}".format(hesapvki))
                print("Sporcu Obez 2 seviyesinde.")

            if cinsiyet == "E" or cinsiyet == "e" :
                ideal =50 + (2.3 / 2.54) * (boy - 152.4)
                yagsiz=((1.1*kilo)-128*(kilo*kilo)/(boy*boy))
                yagorani=((kilo-yagsiz)*100)/kilo
                print("\nSporcunun ideal kilosu ={:.2f}".format(ideal))
                print("Sporcunun yağ oranı ={:.2f}".format(yagorani))
                print("Sporcunun yağsız kas kütlesi ={:.2f}".format(yagsiz))
                break

            elif cinsiyet == "K" or cinsiyet == "k" :
                ideal=45.5 + (2.3 / 2.54) * (boy - 152.4)
                yagsiz=((1.07*kilo)-148*(kilo*kilo)/(boy*boy))
                yagorani=((kilo-yagsiz)*100)/kilo
                print("\nSporcunun ideal kilosu ={:.2f}".format(ideal))
                print("Sporcunun yağ oranı ={:.2f}".format(yagorani))
                print("Sporcunun yağsız kas kütlesi ={:.2f}".format(yagsiz))
                break

            else:
                print("Lütfen doğru tuşlayınız.")

        print("\nVki yazdırıldı.Menüye yönlendiriliyorsunuz...")

def ucret ():
    print("Ucret hesabı yapmak için")
    a = ogrenciara()
    kullanici = []
    birim=300
    if a != 0:
        a = int(a)
        a = a - 1

        def okuma():
            with open("19010011062.txt", "r+") as sporcudosya:
                liste = sporcudosya.readlines()  # her satırı listeye eleman olarak alıyor
                format(liste)

        def format(liste):
            for deger in liste:  # listenin elemanini yani satiirlari tek tek dolasiyor
                deger2 = deger.split("\t")  # satirlardaki her kelimeyi ayırıp listeye atıyor
                data = []
                for ind in range(0, len(deger2)):  # satırdaki kelimeleri listeye icine atiyor
                    data.append(deger2[ind])
                kullanici.append(data)  # listeyi liste içine atıyorum

        okuma()
        yas=kullanici[a][3]
        aylik=kullanici[a][4]
        yas=int(yas)
        aylik=int(aylik)

        kontrol1=0#öğrenci indirimden yaralanıp yaralanmadığını kontrol ediyor
        kontrol2=0#aylık indirimden yaralanıp yaralanmadığını kontrol ediyor

        if yas <= 18:#öğrenci indirimi kaydı tuttum
            ogindirim=5/100
            kontrol1=1

        elif 18 < yas <= 22:
            ogindirim=10/100
            kontrol1=1

        else :
            ogindirim=1


        if aylik==1 :#aylık indirimi kaydı tuttum
            para=aylik*birim
        elif 1<aylik<=3:
            ayindirim=90/100
            para=aylik*(birim*(ayindirim-ogindirim))
            kontrol2=1

        elif 3<aylik<=6 :
            ayindirim=85/100
            para=aylik*(birim*(ayindirim-ogindirim))
            kontrol2 = 1

        elif 6<aylik<=12 :
            ayindirim = 80 / 100
            para=aylik*(birim*(ayindirim-ogindirim))
            kontrol2 = 1

        else :
            ayindirim = 75 / 100
            para=aylik*(birim*(ayindirim-ogindirim))
            kontrol2 = 1

        if kontrol1 :
            print("\n%{} öğrenci indiriminden yaralandınız".format(ogindirim*100))
        if kontrol2 :
            print("%{} öğrenci indiriminden yaralandınız".format(100-ayindirim * 100))

        print("\nSporcunun spor salonu ücreti ={}".format(para))
        print("\nÜcret yazdırıldı.Menüye yönlendiriliyorsunuz...")

def cikis():
    print("""\nCıkıs yapmak istediginize emin misiniz?
    Cıkıs icin 0'ı
    Iptal etmek icin 1'i""")
    secim = int(input("Seciniz :"))
    return secim

menu()