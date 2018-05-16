__author__='Abdullah UZGUR'

import tkinter
from random import choice


class Simon_Simon() :
    def __init__(self, master):

        self.master = master
        self.master.minsize(480, 360)
        self.master.title("Simon Simon")
        self.master.update()

        self.simon_canvas = tkinter.Canvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height(), highlightthickness=5)
        self.simon_canvas.pack()

        self.temelr = ("#ff0000", "#0066ff", "#00ff00", "#ffff00")
        self.parlak_renkler = ("darkred", "darkblue", "darkgreen", "orange")
        self.renkler = [color for color in self.temelr]
        self.dörtgen = []

        self.sira = [choice(self.temelr)]
        self.sıralanan = 0
        self.canvas_ciz()
        self.diziyi_göster()
        self.master.mainloop()

    def diziyi_göster(self):

        self.flash(self.sira[self.sıralanan])
        if(self.sıralanan < len(self.sira) - 1):
            self.sıralanan += 1
            self.master.after(1500, self.diziyi_göster)
        else :
            self.sıralanan = 0

    def flash(self, color):
        index = self.temelr.index(color)
        if self.renkler[index] == self.temelr[index] :
            self.renkler[index] = self.parlak_renkler[index]
            self.master.after(1250, self.flash, color)
        else :
            self.renkler[index] = self.temelr[index]
        self.canvas_ciz()


    def kontrolet(self):
        dortgen_kimligi = self.simon_canvas.find_withtag("current")[0]
        dörtgen_index = self.dörtgen.index(dortgen_kimligi)
        color = self.temelr[dörtgen_index]
        if color == self.sira[self.sıralanan]:
            if self.sıralanan < len(self.sira) - 1:
                self.sıralanan += 1
            else :
                self.master.title("Simon - Skor: {}".format(len(self.sira)))
                self.sira.append(choice(self.temelr))
                self.sıralanan = 0
                self.diziyi_göster()
        else :
            self.master.title("Simon  - Kaybettin! | Skorun: {}".format(len(self.sira)))
            self.sira[:] = []
            self.sira.append(choice(self.temelr))
            self.sıralanan = 0
            self.diziyi_göster()

    def canvas_ciz(self):
        self.dörtgen[:] = []
        self.simon_canvas.delete("all")
        for index, color in enumerate(self.renkler):
            if index <= 1:
                rectangle = self.simon_canvas.create_rectangle(
                                          index * self.master.winfo_width(),
                                          0, self.master.winfo_width() / 2,
                                          self.master.winfo_height() / 2,
                                          fill = color, outline = color)
            else:
                rectangle = self.simon_canvas.create_rectangle(
                                        (index - 2) * self.master.winfo_width(),
                                        self.master.winfo_height(),
                                        self.master.winfo_width() / 2,
                                        self.master.winfo_height() / 2,
                                        fill = color, outline = color)
            self.dörtgen.append(rectangle)
        for id in self.dörtgen:
            self.simon_canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.kontrolet())

def main():
    root=tkinter.Tk()
    pencere0=Simon_Simon(root)

if __name__ == "__main__" : main()
