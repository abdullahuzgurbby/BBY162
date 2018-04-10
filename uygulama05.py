__author__ = "Abdullah UZGUR"

#adam asmaca oyunu

import random

secilenKelime = random.choice(["çilek", "ıspanak", "marul", "muz", "roka", "ciynak", "ıspanak", "portakal", "mandalina", "üzüm", "kivi"])
canSayisi = 5
kelimeler = []
altCizgi = "_"


for kelime in secilenKelime:

    kelimeler.append(altCizgi)

print(kelimeler)

while canSayisi > 0:

    i = 0

    girdi = input("\nBir harf giriniz: ").lower()

    if girdi in secilenKelime:
        for kontrol in secilenKelime:
            if secilenKelime[i] == girdi:
                kelimeler[i] = girdi
            i += 1

        print("")
        print(kelimeler)
        print("\n \"%s\" harfi " %girdi)

    else:
        canSayisi -= 1
        print("")
        print(kelimeler)
        print("\n\"%s\" harfi yanlış. Başka harf gir" % girdi)
        print("\nKalan can sayısı = " + "[" + canSayisi * " ♥ " + "] = " + str(canSayisi))

    if canSayisi == 0:
        print("Başaramadın! Doğru kelime: %s" %secilenKelime)
        break

    if altCizgi not in kelimeler:
        print("\nTebrikler! Doğru kelimeyi buldun")
        break
