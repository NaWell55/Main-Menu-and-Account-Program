import math
import time
from fonksiyonlar import *


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
1- Hesap Makinesi
2- Geometri Hesaplama
3- 5 Büyük Lig Puan Durumları
4- Çıkış
                                
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
                            karekoksayi1 = int(input("Sayıyı Girin: "))
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
                            elif cikis == "h":
                                continue
                        
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
                            elif cikis == "h":
                                continue

                        else:
                            print("Yanlış Tuşlama bir daha deneyiniz...")



                elif anaMenu == "3":
                    while True:
                        ligsecim = input("""- 5 BÜYÜK LİG PUAN DURUMLARI -
1- Trendyol Süper Lig (Türkiye)
2- Premier League (İngiltere)
3- La Liga (İspanya)
4- Serie A (İtalya)
5- Bundesliga (Almanya)
6- League 1 (Fransa)
7- Çıkış

Seçiminiz: """)
                        if ligsecim == "1":
                            superlig()
                    
                        elif ligsecim == "2":
                            premierlig()

                        elif ligsecim == "3":
                            laliga()

                        elif ligsecim == "4":
                            seriea()

                        elif ligsecim == "5":
                            bundesliga()

                        elif ligsecim == "6":
                            lig1()

                        elif ligsecim == "7":
                            cikis = input("Emin misin(e,h): ")
                            if cikis == "e":
                                print("Çıkılıyor...")
                                time.sleep(2)
                                break
                            elif cikis == "h":
                                continue

                        else:
                            print("Yanlış Tuşlama bir daha deneyiniz...")
                    



                elif anaMenu == "4":
                    cikis = input("Emin misin(e,h): ")
                    if cikis == "e":
                        print("Çıkılıyor...")
                        time.sleep(2)
                        break
                    elif cikis == "h":
                        continue

                else:
                    print("Yanlış Tuşlama bir daha deneyiniz...")



    elif girisSecim == "3":
        cikis = input("Emin misin(e,h): ")
        if cikis == "e":
            print("Çıkılıyor...")
            time.sleep(2)
            break
        elif cikis == "h":
            continue
    
    
    
    else:
        print("Yanlış Tuşlama bir daha deneyiniz...")
