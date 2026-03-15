import math
import time

def topla(a,b):
    return a + b


def cikar(a,b):
    return a - b


def carpma(a,b):
    return a * b


def bolme(a, b):                      
    if b == 0:
        return "0 ile bölme yapamazsın"
    return a / b


def usalma(a,b):
    return a ** b


def karekok(a):
    return math.sqrt(a)


def mutlakdeger(a):     
    if a < 0:
        return -a
    return a


def modalma(a,b):
    return a % b


def ortalama(a, b):            
    return (a + b) / 2


def enbuyuk(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "İki sayıda eşit"
    


def ucgencevre(a, b, c):
    return a + b + c

def ucgenalan(t, y):
    return t*y/2

def karecevre(a):
    return a*4

def karealan(a):
    return a*a

def dikdortgencevre(a, b):
    return 2*(a+b)

def dikdortgenalan(a, b):
    return a*b




while True:
    girisSecim = input("""Lütfen Kaydolun
1-Kaydol      2-Giriş Yap      3-Çıkış
Seçiminiz: """)
    if girisSecim == "1":       
        print("Hesap oluşturmak için aşağıdakileri doldurunuz")
        isim = input("İsminizi Girin(Nickname): ")
        mail = input("Mail Adresiniz(gmail, hotmail): ")
        sifre = input("Bir Şifre oluşturun(en az 3 karakter): ")
        if len(sifre) <= 3:
            print("lütfen daha uzun bir şifre giriniz...")
        else: 
            print("Tebrikler Hesabınız oluşturuldu şimdi giriş bölümünde 'Giriş Yap'a girip e-posta ve şifrenizi giriniz...'")

    elif girisSecim == "2":
        print("Hesabınıza girmek için bilgilerinizi giriniz")
        girisMail = input("Mail Adresiniz: ")
        girisSifre = input("Şifreniz: ")
        if girisMail == mail and girisSifre == sifre:
            print("Tebrikler! Giriş yaptınız, Ana Menüye Hoşgeldiniz.")
            while True:
                anaMenu = input(f"""- ANA MENÜ - Bilgiler: İsim: {isim}   Mail: {mail}
1-Hesap Makinesi
2-Geometri Hesaplama
3-Trendyol Süper Lig Puan Durumu
4-Çıkış
                                
Seçiminiz: """)
                if anaMenu == "1":
                    while True:
                        hesapMankinesi = input("""- HESAP MAKİNESİ -
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
5- Üs alma
6- Karekök
7- Mutlak değer
8- Mod alma
9- Ortalama (2 sayı)
10- En büyük (2 sayı)
11- Çıkış
                                               
Seçiminiz: """)
                        if hesapMankinesi == "1":
                            toplamasayi1 = int(input("1. Sayı: "))
                            toplamasayi2 = int(input("2. Sayı: "))
                            sonuc = topla(toplamasayi1, toplamasayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "2":
                            cikarmasayi1 = int(input("1. Sayı: "))
                            cikarmasayi2 = int(input("2. Sayı: "))
                            sonuc = cikar(cikarmasayi1, cikarmasayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "3":
                            carpmasayi1 = int(input("1. Sayı: "))
                            carpmasayi2 = int(input("2. Sayı: "))
                            sonuc = carpma(carpmasayi1, carpmasayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "4":
                            bolmesayi1 = int(input("1. Sayı: "))
                            bolmesayi2 = int(input("2. Sayı: "))
                            sonuc = bolme(bolmesayi1, bolmesayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "5":
                            ussayi1 = int(input("1. Sayı: "))
                            ussayi2 = int(input("2. Sayı: "))
                            sonuc = usalma(ussayi1, ussayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "6":
                            karekoksayi1 = int(input("Sayıyı Girin: ")),
                            sonuc = karekok(karekoksayi1)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "7":
                            mutlakdegersayi1 = int(input("Sayıyı Girin: "))
                            sonuc = mutlakdeger(mutlakdegersayi1)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "8":
                            modalsayi1 = int(input("1. Sayıyı Girin: "))
                            modalsayi2 = int(input("2. Sayıyı Girin: "))
                            sonuc = modalma(modalsayi1, modalsayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "9":
                            ortalamasayi1 = int(input("1. Sayıyı Girin: "))
                            ortalamasayi2 = int(input("2. Sayıyı Girin: "))
                            sonuc = ortalama(ortalamasayi1, ortalamasayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "10":
                            enbuyuksayi1 = int(input("1. Sayıyı Girin: "))
                            enbuyuksayi2 = int(input("2. Sayıyı Girin: "))
                            sonuc = enbuyuk(enbuyuksayi1, enbuyuksayi2)
                            print("Sonuç:", sonuc)


                        elif hesapMankinesi == "11":
                            cikis = input("Çıkmak istediğine emin misin?(e,h): ")
                            if cikis == "e":
                                print("Çıkılıyor...")
                                time.sleep(2)
                                break
                        
                        else:
                            print("Yanlış tuşlama bir daha deneyiniz...")
                            

                elif anaMenu == "2":
                    while True:
                        geometriHesaplama = input("""- GEOMETRİ HESAPLAMA -
1- Üçgenin Çevresini Hesaplama
2- Üçgenin Alanını Hesaplama
3- Karenin Çevresini Hesaplama
4- Karenin Alanını Hesaplama
5- Dikdörtgenin Çevresini Hesaplama
6- Dikdörtgenin Alanını Hesaplama
7- Çıkış
                                                  
Seçiminiz: """)
                        if geometriHesaplama == "1":
                            sayi1 = int(input("1. Sayıyı giriniz: "))
                            sayi2 = int(input("2. Sayıyı giriniz: "))
                            sayi3 = int(input("3. Sayıyı giriniz: "))
                            sonuc = ucgencevre(sayi1, sayi2, sayi3)
                            print("Sonuç:",sonuc)

                        elif geometriHesaplama == "2":
                            sayi1 = int(input("Taban değerini giriniz: "))
                            sayi2 = int(input("Yükseklik değerini giriniz: "))
                            sonuc = ucgenalan(sayi1, sayi2)
                            print("Sonuc:",sonuc)

                        elif geometriHesaplama == "3":
                            sayi1 = int(input("Kenar uzunluğunu giriniz: "))
                            sonuc = karecevre(sayi1)
                            print("Sonuc:",sonuc)

                        elif geometriHesaplama == "4":
                            sayi1 = int(input("Kenar uzunluğunu giriniz: "))
                            sonuc = karealan(sayi1)
                            print("Sonuc:",sonuc)

                        elif geometriHesaplama == "5":
                            sayi1 = int(input("Kısa kenar değerini giriniz: "))
                            sayi2 = int(input("Uzun kenar değerini giriniz: "))
                            sonuc = dikdortgencevre(sayi1, sayi2)
                            print("Sonuc:",sonuc)

                        elif geometriHesaplama == "6":
                            sayi1 = int(input("Kısa kenar değerini giriniz: "))
                            sayi2 = int(input("Uzun kenar değerini giriniz: "))
                            sonuc = dikdortgenalan(sayi1, sayi2)
                            print("Sonuc:",sonuc)

                        elif geometriHesaplama == "7":
                            cikis = input("Emin misin(e,h): ")
                            if cikis == "e":
                                print("Çıkılıyor...")
                                time.sleep(2)
                                break

                        else:
                            print("Yanlış Tuşlama bir daha deneyiniz...")



                elif anaMenu == "3":
                    print(f"""- TRENDYOL SÜPER LİG PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A   P     Son 5
1-Galatasaray            26  20  4  2  62  18  44  64    GMGGG
2-Fenerbahçe             26  16  9  1  57  27  30  57    GBBGM
3-Trabzonspor            26  17  6  3  52  29  23  57    MGGGG
4-Beşiktaş               26  14  7  5  47  30  17  49    GGGMG
5-Göztepe                26  11  10 5  30  20  10  43    BMBMB
6-Başakşehir             26  12  6  8  44  30  14  42    MGGGM
7-Samsunspor             26  8   11 7  29  31  -2  35    MBBMG
8-Kocaelispor            26  9   6  11 23  27  -4  33    GMMGM
9-Gaziantep FK           26  8   9  9  35  42  -7  33    MMBBG
10-Rizespor              26  7   9  10 32  36  -4  30    BGGGM
11-Alanyaspor            26  5   13 8  28  32  -4  28    GMMBB
12-Konyaspor             26  6   9  11 30  39  -9  27    MGMBG
13-Gençlerbirliği        26  6   7  13 28  36  -8  25    BMBBM
14-Kasımpaşa             26  5   9  12 22  36  -14 24    GBMBG
15-Antalyaspor           26  6   6  14 25  43  -18 24    GMBMM
16-Eyüpspor              26  6   7  14 19  37  -18 22    MGBMM
17-Kayserispor           26  3   11 12 20  48  -28 20    BGBMM
18-Karagümrük            26  4   5  17 24  46  -22 17    MBMBG
                          
UEFA Şampiyonlar Ligi grup aşaması ---> 1.                   Son 5 maç
Avrupa Ligi eleme turu katılımcıları ---> 3.                 G ---> Galibiyet
Avrupa Konferans Ligi eleme turu katılımcıları ---> 4.       B ---> Berabere
Küme düşme 16. ,17. , 18.                                    M ---> Mağlubiyet""")
                elif anaMenu == "4":
                    cikis = input("Emin misin(e,h): ")
                    if cikis == "e":
                        print("Çıkılıyor...")
                        time.sleep(2)
                        break

                else:
                    print("Yanlış Tuşlama bir daha deneyiniz...")



    elif girisSecim == "3":
        cikis = input("Emin misin(e,h): ")
        if cikis == "e":
            print("Çıkılıyor...")
            time.sleep(2)
            break
    
    
    
    else:
        print("Yanlış Tuşlama bir daha deneyiniz...")
