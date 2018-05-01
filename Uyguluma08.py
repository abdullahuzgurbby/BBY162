from tkinter import *
from PIL import ImageTk,Image
class Kutuphane:
    def __init__(self,anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Kütüphane Otomasyonu")
        anasayfa.configure(background="white")

        self.foto = Image.open("HÜ.jpg")
        self.tkimage = ImageTk.PhotoImage(self.foto)
        self.resim = Label(root, image=self.tkimage)
        self.resim.grid()

        self.kitapları_listele = Button(anasayfa, text="Kitapları Listele",bg="white",fg="red",cursor="star",font="bold", command=self.kitaplari_listele)
        self.kitapları_listele.grid(row="1")

        self.kitap_ekle = Button(anasayfa, text="Kitap Ekle", bg="white",fg="red",cursor="star",font="bold",command = self.kitap_ekle)
        self.kitap_ekle.grid(row="2")

        self.kitap_ara = Button(anasayfa, text="Kitap Ara", bg="white",fg="red",cursor="star",font="bold",command=self.kitap_ara)
        self.kitap_ara.grid(row="5")

        self.cikis = Button(anasayfa, text ="Kapat", command=exit, fg="white", bg="red",cursor="man")
        self.cikis.grid(row="6")

    def kitap_ekle(self):
        global kitap_adi,yazar_adi,tur,isbn,yayin_evi,yayin_yili
        pencere1 = Tk()
        baslik1 = pencere1.title("Kitap Kayıt Penceresi")
        pencere1.configure(background="white")

        kitap_adi= Entry(pencere1,width=27)
        kitap_adi.grid(column=2, row=3)
        yazar_adi = Entry(pencere1, width=27)
        yazar_adi.grid(column=2, row=4)
        tur = Entry(pencere1, width=27)
        tur.grid(column=2, row=5)
        isbn = Entry(pencere1, width=27)
        isbn.grid(column=2, row=6)
        yayin_evi = Entry(pencere1, width=27)
        yayin_evi.grid(column=2, row=7)
        yayin_yili = Entry(pencere1, width=27)
        yayin_yili.grid(column=2, row=8)
        self.kaydet = Button(pencere1, text= "Kaydet",command=self.kitap_kaydet, fg="black", bg="yellow")
        self.kaydet.grid(column=1, row=9)

        self.cıkıs = Button(pencere1 ,text = "Kapat", command=pencere1.destroy, fg="black", bg="yellow",cursor="man")
        self.cıkıs.grid(column=3, row=9)
        Label(pencere1,bg="white",fg="red", text='Kitap Adı: ').grid(column=1, row=3)
        Label(pencere1,bg="white",fg="red", text='Yazar Adı: ').grid(column=1, row=4)
        Label(pencere1,bg="white",fg="red", text='Kitabın Türü: ').grid(column=1, row=5)
        Label(pencere1,bg="white",fg="red", text='ISBN :').grid(column=1, row=6)
        Label(pencere1,bg="white",fg="red", text='Yayınevi : ').grid(column=1, row=7)
        Label(pencere1,bg="white",fg="red", text='Yayın Yılı :').grid(column=1, row=8)
    def kitap_kaydet(self):
        kayit_sis = str(("\n" + kitap_adi.get() + " - " + yazar_adi.get() + " - " + tur.get() + " - " + isbn.get() + " - " + yayin_evi.get() + " - " + yayin_yili.get()))
        dosya= open("katalog.txt","a")
        for i in kayit_sis:
            dosya.write(i)
        dosya.close()
        #self.kaydet.destroy()

    def kitaplari_listele(self):
        pencerex= Tk()

        file = open("katalog.txt")
        data = file.read()
        file.close()
        kitap_liste = Label(pencerex, text=data)
        kitap_liste.grid(row=1, column=2)


    def kitap_ara(self):
        global kitap_adi, yazar_adi, tur, isbn, yayin_evi, yayin_yili
        pencere4 = Tk()
        baslik4 = pencere4.title("Kitap Kayıt Penceresi")
        pencere4.configure(background="white")

        kitapAra= Entry(pencere4, width=27)
        kitapAra.grid(column=2, row=3)
        self.ara = Button(pencere4, text="Ara", command=self.kitap_ara, fg="red", bg="white")
        self.ara.grid(column=2, row=9)

        kitap_adi= Entry(pencere4,width=27)
        kitap_adi.grid(column=2, row=3)
        yazar_adi = Entry(pencere4, width=27)
        yazar_adi.grid(column=2, row=4)
        tur = Entry(pencere4, width=27)
        tur.grid(column=2, row=5)
        isbn = Entry(pencere4, width=27)
        isbn.grid(column=2, row=6)
        yayin_evi = Entry(pencere4, width=27)
        yayin_evi.grid(column=2, row=7)
        yayin_yili = Entry(pencere4, width=27)
        yayin_yili.grid(column=2, row=8)

        Label(pencere4,bg="white",fg="red", text='Kitap Adı: ').grid(column=1, row=3)
        Label(pencere4,bg="white",fg="red", text='Yazar Adı: ').grid(column=1, row=4)
        Label(pencere4,bg="white",fg="red", text='Kitabın Türü: ').grid(column=1, row=5)
        Label(pencere4,bg="white",fg="red", text='ISBN :').grid(column=1, row=6)
        Label(pencere4,bg="white",fg="red", text='Yayınevi : ').grid(column=1, row=7)
        Label(pencere4,bg="white",fg="red", text='Yayın Yılı :').grid(column=1, row=8)

    



root = Tk()
yeniPencere = Kutuphane(root)
root.mainloop()
