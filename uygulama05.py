_author_ = "Abdullah UZGUR"

# Uygulama 05

import random

sehir = random.choice(["ankara", "çankırı", "tekirdağ", "amasya", "istanbul", "van", "şırnak", "bursa", "şanlıurfa", "gaziantep", "çorum", "çanakkale", "trabzon", "afyonkarahisar"])

harfler = []

kalanhak = 5

altcizgi = "_"


gosterimyazisi = list(altcizgi * len(sehir))

dongu = 1


while dongu:

    print(" ".join(gosterimyazisi),"\n") # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.

    secilenharf = input("Bir harf giriniz: ")

    try: # try, input ile alınan verinin sayı olup olmadığını kontrol eder.
        int(secilenharf)
        print("Doğru bir şeyler girdiğinden emin ol.\n")
    except: # Except alınan harf 1 den uzun olduğunda hata mesajı verir.

        if len(secilenharf) > 1:
            print("Harf giriniz!\n")
        else:

            if secilenharf in harfler:
                print("Bu harfi zaten girildi.\n")
            else:

                bulduk = None

                for i in range(len(sehir)):
                    # kullanıcının girdiği harf, bulunucak kelimenin "i" nin taşıdığı sayı değerindeki indeksteki harfe eşit ise,
                    if secilenharf == sehir[i]:

                        bulduk = True

                        gosterimyazisi[i] = secilenharf

                        harfler.append(secilenharf) # Alınan harf, harf havuzuna eklendi.

                        if altcizgi not in gosterimyazisi:

                            print(" ".join(gosterimyazisi)) # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.
                            print("\nTebrikler doğru kelime!")

                            dongu = 0
                            # Girilen harf aranan kelime içinde yoksa alttaki kodlar çalıştırılacak.
                else:

                    if bulduk != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan şansınız: %s\n" %kalanhak)

                        harfler.append(secilenharf) # Alınan harf, harf havuzuna eklendi

                if kalanhak == 0:
                    print("Kaybettin! Doğru kelime =  %s  \n" %sehir)

                    break
