_auther_='Abdullah UZGUR'

#Uygulama02
#Saniye cinsinden verilen veriyi yıl, ay, gün, saat, dakika ve saniyeye dönüştüren formül..

deger = int(input("Saniye cinsinden bir değer giriniz...:"))

yil = deger / 31557600

ay = (deger % 31557600) / 2629800

gun = ((deger % 31557600) % 2629800) / 86400

saat = (((deger % 31557600) % 2629800) % 86400) / 3600

dakika = ((((deger % 31557600) % 2629800) % 86400)% 3600) / 60

saniye = (((((deger % 31557600) % 2629800) % 86400) % 3600) % 60)

print(int(yil) , "Yıl" , " " , int(ay) ,"Ay" , " " , int(gun) ,"Gün" , " " , int(saat) , "Saat" , " " , int(dakika)  ,"Dakika", " " , int(saniye) , "Saniye")
