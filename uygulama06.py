__author__='Abdullah UZGUR'

import random
from tkinter import *
class tekerleme:
    def __init__(self, master):
        self.master = master
        master.title("Tekerleme")

        self.label = Label(master, text="     TEKERLEMELER     ")
        self.label.pack()

        self.tekerleme = Button(master, text="Tekerleme",command=self.tekerleme)
        self.tekerleme.pack()

        self.exit = Button(master, text="Kapat",command=master.quit)
        self.exit.pack()

    def tekerleme(self):
        tekerlemeler = ("\nGünlerden bir gün Türkçe dersinde\nİşler karıştı tersi tersine\nNokta, virgül, satır başı\nİşin yoksa başını kaşı\nBen yandım, tıp!","\nOcak kıvılcımlandırıcılardan mısın,\nKapı gıcırdatıcılardan mısın?\nNe ocak kıvılcımlandırıcılardanım,\nNe de kapı gıcırdatıcılardanım.","\nÜç tunç tas kayısı hoşafı.\nÜç tuç tas has kayısı hoşafı.\nPaşa tası ile beş has tas kayısı hoşafı.","\nbu tarlaya bir şinik, kekere mekere ekmişler.\nbu tarlaya da bir şinik kekere mekere ekmişler.\nbu tarlaya ekilen bir şinik kekere mekereye boz ala boz başlı pis porsuk dadanmış,\nbu tarlaya ekilen bir şinik kekere mekereye de boz ala boz başlı pis porsuk dadanmış,\no tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlı pis porsuk,... \ndiğer tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlı pis porsuk'a demiş ki,\nsen ne zamandan beri bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlı pis porsuksun?\no da ona cevaben!\nsen ne zaman o tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlı pis porsuk san,\nbende o zamandan beri bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlı pis porsuğum demiş.","\nÇatalca’da topal çoban çatal yapıp çatal satar.\nNesi için çatalca’da topal çoban çatal yapıp çatal satar ?\nKarı için çatalca’da topal çoban çatal yapıp çatal satar.")
        secilenTekerleme = random.choice(tekerlemeler)
        self.tekerle = Label(self.master, text=secilenTekerleme)
        self.tekerle.pack()

root = Tk()
bby = tekerleme(root)
root.mainloop()
