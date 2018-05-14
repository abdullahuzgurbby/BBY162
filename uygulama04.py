__author__ = "Abdullah UZGUR"

kadinismi = input("Bir kadın adı giriniz  :")
erkekismi = input("Bir erkek adı giriniz  :")
misra    = int(input("Mısra sayısı giriniz. Maksimum 10 mısra yazdırılabilir.."))

siir = ["Kız " + kadinismi + " "+ kadinismi, "Niçin durmazsın yerinde", "Gözlerine aşık oldum", "Bak sarardım soldum", "Al" + erkekismi + "yanına", "Kanım kaynadı sana", "Gel çıkalım dağlara", "Suyu soğuk yaylalara", "Gözden ırak yaşamaya", "Başlayalım" + kadinismi , "Al beni yanına", erkekismi + "muhtaç inana sana"]

for yazdirilacakSiir in siir[:misra]:
    print(yazdirilacakSiir)


if misra > 12:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 10")
else:
    print("Yazdırılan mısra sayısı:", misra)
