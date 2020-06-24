from tkinter import *
from tkinter import filedialog, messagebox, ttk

import math
import matplotlib.pyplot as plt

from PIL import ImageTk, Image

class main:
    def __init__(self):
        self.num = 0
        self.img = Image
        self.master = root
        self.master.title("Изменение изображений")
        self.master.geometry('800x500+150+50')

        self.file_menu = Menu(tearoff=0)

        self.file_menu.add_command(label="Открыть", command=self.open_click)
        self.file_menu.add_command(label="Сохранить", command=self.save_click)

        self.canal_menu = Menu(tearoff=0)
        self.canal_menu.add_command(label="Красный", command=self.canal_red)
        self.canal_menu.add_command(label="Синий", command=self.canal_blue)
        self.canal_menu.add_command(label="Зелёный", command=self.canal_green)

        one_menu = Menu(tearoff=0)
        one_menu.add_command(label="Усреднение", command=self.average_click)
        one_menu.add_command(label="Коррекция под человеческий глаз", command=self.human_eye)
        one_menu.add_command(label="Градация по максимуму", command=self.max_grad)
        one_menu.add_command(label="Градация по минимуму", command=self.min_grad)
        one_menu.add_cascade(label="Поканальные преобразования", menu=self.canal_menu)
        one_menu.add_command(label="Метод эквализации гистограммы", command = self.eqvaliz_hist)
        one_menu.add_command(label="Отображение гистограммы", command=self.hist)

        two_menu = Menu(tearoff=0)
        two_menu.add_command(label="Фильтр", command=self.filt)

        three_menu = Menu(tearoff=0)
        three_menu.add_command(label="Кодировка", command=self.code)

        # four_menu = Menu(tearoff=0)
        # four_menu.add_command(label="Дилатация", command=self.dilatacia)
        # four_menu.add_command(label="Эрозия", command=self.erozia)
        # four_menu.add_command(label="Замыкание", command=self.zamikanie)
        # four_menu.add_command(label="Размыкание", command=self.razmikanie)

        five_menu = Menu(tearoff=0)
        five_menu.add_command(label="Бинаризация Оцу", command=self.osu)
        five_menu.add_command(label="Бинаризация Ниблэка", command=self.niblek)

        self.main_menu = Menu()
        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.main_menu.add_cascade(label="1 задание", menu=one_menu)
        self.main_menu.add_cascade(label="2 задание", menu=two_menu)
        self.main_menu.add_cascade(label="3 задание", menu=three_menu)
        #self.main_menu.add_cascade(label="4 задание", menu=four_menu)
        self.main_menu.add_cascade(label="5 задание", menu=five_menu)

        self.master.config(menu=self.main_menu)

        self.panel = Label(self.master)
        self.panel.pack()

        self.master.mainloop()

    def open_click(self):
        filename = filedialog.askopenfilename(title='open')
        self.img = Image.open(filename)
        # img= Image.open('col.jpg')
        # img = Image.open('pic.png')
        self.img.thumbnail((800, 500))
        imgp = ImageTk.PhotoImage(self.img)
        self.panel.configure(image=imgp)
        self.master.mainloop()

    def save_click(self):
        self.num+=1
        self.img.save('new' + str(self.num) + '.png')
        messagebox.showinfo("Сообщение", "Изображение сохранено")

    def average_click(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = (R + G + B) // 3
                img_tansform.putpixel((i, j), (S, S, S))
        child("Усреднение", img_tansform)

    def hist(self):
        #img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = self.img.load()
        S = []

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S.append((R + G + B) // 3)
        plt.figure()
        n, bins, patches = plt.hist(S, bins=255, facecolor='blue')
        plt.title('Гистограмма')
        plt.show()

    def human_eye(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = int(0.3 * R + 0.59 * G + 0.11 * B)
                img_tansform.putpixel((i, j), (S, S, S))
        child("Человеческий глаз", img_tansform)

    def max_grad(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = max(R, G, B)
                img_tansform.putpixel((i, j), (S, S, S))
        child("Градация по максимуму", img_tansform)

    def min_grad(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = min(R, G, B)
                img_tansform.putpixel((i, j), (S, S, S))
        child("Градация по минимуму", img_tansform)

    def canal_red(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()
        obj[4, 4]
        obj[4, s[1] - 4]
        obj[s[0] - 4, s[1] - 4]

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = R
                img_tansform.putpixel((i, j), (S, S, S))
        child("Красный канал",img_tansform)

    def canal_blue(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()
        R, G, B = obj[5, 5]

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = B
                img_tansform.putpixel((i, j), (S, S, S))
        child("Синий канал", img_tansform)

    def canal_green(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = G
                img_tansform.putpixel((i, j), (S, S, S))
        child("Зелёный канал", img_tansform)

    def eqvaliz_hist(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        h = [0] * 256
        for x in range(width):
            for y in range(height):
                h[(obj[x, y][0] + obj[x, y][1] + obj[x, y][2]) // 3] +=1

        col = width * height
        cd = [0]*256
        min=col
        sum = 0
        for i in range(256):
            sum += h[i]
            cd[i] += sum
            if 0 < cd[i] < min:
                min = cd[i]

        h = [0]*256
        for i in range(256):
            h[i] = (cd[i] - min) * 255 // (col - min)

        for i in range(width):
            for j in range(height):
                img_tansform.putpixel((i, j), (h[obj[i, j][0]], h[obj[i, j][0]], h[obj[i, j][0]]))

        child("Эквализация гистограммы", img_tansform)

    def filt(self):
        filt_param(self.img)

    def dilatacia(self):
        dilatacia_param(self.img)

    def code(self):
        arif_code()

    def osu(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        allpix=width*height
        obj = img_tansform.load()

        h = [0] * 256
        for x in range(width):
            for y in range(height):
                h[(obj[x, y][0] + obj[x, y][1] + obj[x, y][2]) // 3] += 1

        dispMax = 0
        disp = 0
        numMax=0
        w0 = 0
        w1 = 0
        nu0 = 0
        nu1 = 0
        sum0=0
        sum=0
        for i in range(256):
            sum += i * h[i]
        for t in range(256):
            w0+=h[t]
            if w0 == 0:
                continue
            w1 = allpix - w0
            if w1 == 0:
                break
            sum0 += t * h[t]
            nu0 = sum0 / w0
            nu1 = (sum -sum0)/w1
            disp = w0*w1*((nu1-nu0)**2)
            if disp > dispMax:
                dispMax = disp
                numMax = t

        for x in range(width):
            for y in range(height):
                if ((obj[x, y][0] + obj[x, y][1] + obj[x, y][2]) // 3) > numMax:
                    img_tansform.putpixel((x, y), (255,255,255))
                else:
                    img_tansform.putpixel((x, y), (0,0,0))

        child("Бинаризация Оцу", img_tansform)

    def niblek(self):
        nibl_param(self.img)

class child:

    def __init__(self,tite,my_image):
        self.num = 0
        self.img = my_image
        self.slave = Toplevel(root)
        self.slave.title(tite)
        self.slave.geometry('800x500+200+100')

        self.file_menu = Menu(tearoff=0)

        self.file_menu.add_command(label="Сохранить", command=self.save_click)

        self.canal_menu = Menu(tearoff=0)
        self.canal_menu.add_command(label="Красный", command=self.canal_red)
        self.canal_menu.add_command(label="Синий", command=self.canal_blue)
        self.canal_menu.add_command(label="Зелёный", command=self.canal_green)

        one_menu = Menu(tearoff=0)
        one_menu.add_command(label="Усреднение", command=self.average_click)
        one_menu.add_command(label="Коррекция под человеческий глаз", command=self.human_eye)
        one_menu.add_command(label="Градация по максимуму", command=self.max_grad)
        one_menu.add_command(label="Градация по минимуму", command=self.min_grad)
        one_menu.add_cascade(label="Поканальные преобразования", menu=self.canal_menu)
        one_menu.add_command(label="Метод эквализации гистограммы", command=self.eqvaliz_hist)
        one_menu.add_command(label="Отображение гистограммы", command=self.hist)

        two_menu = Menu(tearoff=0)
        two_menu.add_command(label="Фильтр", command=self.filt)

        four_menu = Menu(tearoff=0)
        four_menu.add_command(label="Дилатация", command=self.dilatacia)
        four_menu.add_command(label="Эрозия", command=self.erozia)
        four_menu.add_command(label="Замыкание", command=self.zamikanie)
        four_menu.add_command(label="Размыкание", command=self.razmikanie)

        self.main_menu = Menu()
        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.main_menu.add_cascade(label="1 задание", menu=one_menu)
        self.main_menu.add_cascade(label="2 задание", menu=two_menu)
        self.main_menu.add_cascade(label="4 задание", menu=four_menu)

        self.slave.config(menu=self.main_menu)

        self.panel = Label(self.slave)
        self.panel.pack()
        self.img.thumbnail((800, 500))
        imgp = ImageTk.PhotoImage(self.img)
        self.panel.configure(image=imgp)
        self.slave.mainloop()

    def average_click(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = (R + G + B) // 3
                img_tansform.putpixel((i, j), (S, S, S))
        child("Усреднение", img_tansform)

    def human_eye(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = int(0.3 * R + 0.59 * G + 0.11 * B)
                img_tansform.putpixel((i, j), (S, S, S))
        child("Человеческий глаз", img_tansform)

    def max_grad(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = max(R, G, B)
                img_tansform.putpixel((i, j), (S, S, S))
        child("Градация по максимуму", img_tansform)

    def min_grad(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = min(R, G, B)
                img_tansform.putpixel((i, j), (S, S, S))
        child("Градация по минимуму", img_tansform)

    def save_click(self):
        self.num+=1
        self.img.save('new' + str(self.num) + '.png')
        messagebox.showinfo("Сообщение", "Изображение сохранено")

    def canal_red(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()
        obj[4, 4]
        obj[4, s[1] - 4]
        obj[s[0] - 4, s[1] - 4]

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = R
                img_tansform.putpixel((i, j), (S, S, S))
        child("Красный канал",img_tansform)

    def canal_blue(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()
        R, G, B = obj[5, 5]

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = B
                img_tansform.putpixel((i, j), (S, S, S))
        child("Синий канал", img_tansform)

    def canal_green(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = G
                img_tansform.putpixel((i, j), (S, S, S))
        child("Зелёный канал", img_tansform)

    def hist(self):
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = self.img.load()
        S = []

        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S.append((R + G + B) // 3)
        plt.figure()
        n, bins, patches = plt.hist(S, bins=255, facecolor='blue')
        plt.title('Гистограмма')
        plt.show()

    def eqvaliz_hist(self):
        img_tansform = self.img.copy()
        s = self.img.size
        width = s[0]
        height = s[1]
        obj = img_tansform.load()

        h = [0] * 256
        for x in range(width):
            for y in range(height):
                h[(obj[x, y][0] + obj[x, y][1] + obj[x, y][2]) // 3] += 1

        col = width * height
        cd = [0] * 256
        min = col
        sum = 0
        for i in range(256):
            sum += h[i]
            cd[i] += sum
            if 0 < cd[i] < min:
                min = cd[i]

        h = [0] * 256
        for i in range(256):
            h[i] = (cd[i] - min) * 255 // (col - min)

        for i in range(width):
            for j in range(height):
                img_tansform.putpixel((i, j), (h[obj[i, j][0]], h[obj[i, j][0]], h[obj[i, j][0]]))

        child("Эквализация гистограммы", img_tansform)

    def filt(self):
        filt_param(self.img)

    def dilatacia(self):
        dilatacia_param(self.img)

    def erozia(self):
        erozia_param(self.img)

    def zamikanie(self):
        zamikanie_param(self.img)

    def razmikanie(self):
        razmikanie_param(self.img)


class filt_param:
    def __init__(self, my_image):
        self.num = 0
        self.img = my_image
        self.x = StringVar()
        self.y = StringVar()
        self.z = StringVar()
        self.slave = Toplevel(root)
        self.slave.title("Параметры фильтра")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="Кол-во эл-тов по горизонтали").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.slave.label2 = Label(self.slave, text="Кол-во эл-тов по вертикати").pack()
        self.slave.message2 = Entry(self.slave, textvariable=self.y).pack()
        self.slave.label3 = Label(self.slave, text="Значения фильтра").pack()
        self.slave.message3 = Entry(self.slave, textvariable=self.z).pack()
        self.button = Button(self.slave, text="Применить", command=self.do_filt)
        self.button.pack()

    def do_filt(self):
        x = int(self.x.get())
        y = int(self.y.get())
        z = self.z.get().split(' ')
        mas = []
        koef = 0
        k=0
        for i in range (y):
            mas_str = []
            for j in range (x):
                mas_str.append(float(z[k]))
                koef +=(float(z[k]))
                k+=1
            mas.append(mas_str)
        if koef == 0:
            koef = 1
        else:
            koef = 1/ koef
        img_tansform = self.img.copy()
        s = self.img.size

        width = s[0]
        height = s[1]
        nw=math.ceil(x/2)
        nh=math.ceil(y/2)
        new_image = Image.new("RGB", (width + nw*2 , height + nh*2 ), (0,0,0))
        new_image.paste(img_tansform, (nw,nh))
        trans_image = Image.new("RGB", (width + nw*2 , height + nh*2 ), (0,0,0))
        obj = new_image.load()

        for i in range(nw, width + nw):
            for j in range(nh, height + nh):
                rn,gn,bn=0,0,0
                for k in range(x):
                    for p in range(y):
                        rn += obj[i+k-nw+1, j+p-nh+1][0] *mas[k][p]*koef
                        gn += obj[i+k-nw+1, j+p-nh+1][1] * mas[k][p]*koef
                        bn += obj[i+k-nw+1, j+p-nh+1][2] * mas[k][p]*koef
                if rn < 0:
                    rn = 0
                if gn < 0:
                    gn = 0
                if bn < 0:
                    bn = 0
                trans_image.putpixel((i,j),(round(rn),round(gn),round(bn)))

        s = trans_image.size
        new_image= trans_image.crop((nw,nh,s[0]-nw,s[1]-nh))
        child("Фильтр", new_image)

class dilatacia_param:
    def __init__(self, my_image):
        self.img = my_image
        self.x = StringVar()
        self.y = StringVar()
        self.z = StringVar()
        self.slave = Toplevel(root)
        self.slave.title("Размеры структурирующего элемента")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="Кол-во эл-тов по горизонтали").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.slave.label2 = Label(self.slave, text="Кол-во эл-тов по вертикати").pack()
        self.slave.message2 = Entry(self.slave, textvariable=self.y).pack()
        self.slave.label3 = Label(self.slave, text="Значения структурирующего элемента").pack()
        self.slave.message3 = Entry(self.slave, textvariable=self.z).pack()
        self.button = Button(self.slave, text="Применить", command=self.do_dilatacia)
        self.button.pack()

    def do_dilatacia(self):
        x = int(self.x.get())
        y = int(self.y.get())
        z = self.z.get().split(' ')
        mas = []
        k = 0
        for i in range(y):
            mas_str = []
            for j in range(x):
                mas_str.append(int(z[k]))
                k += 1
            mas.append(mas_str)

        img_tansform = self.img.copy()
        s = self.img.size

        width = s[0]
        height = s[1]
        nw = math.ceil(x / 2)
        nh = math.ceil(y / 2)

        trans_image = Image.new("RGB", (width, height), (0, 0, 0))
        obj = img_tansform.load()

        for i in range(0, width):
            for j in range(0, height):
                rn = 0
                koef = 0
                for k in range(x):
                    for p in range(y):
                        if ((i + k - nw + 1) >= 0) and ((i + k - nw + 1) <= (width - 1)) and (
                                (j + p - nh + 1) >= 0) and ((j + p - nh + 1) <= (height - 1)) and (mas[k][p] != 0):
                            rn += obj[i + k - nw + 1, j + p - nh + 1][0]
                            koef += 1
                if rn == koef * 255:
                    trans_image.putpixel((i, j), (255, 255, 255))
                else:
                    trans_image.putpixel((i, j), (0, 0, 0))

        child("Эрозия", trans_image)



class erozia_param:
    def __init__(self, my_image):
        self.img = my_image
        self.x = StringVar()
        self.y = StringVar()
        self.z = StringVar()
        self.slave = Toplevel(root)
        self.slave.title("Размеры структурирующего элемента")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="Кол-во эл-тов по горизонтали").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.slave.label2 = Label(self.slave, text="Кол-во эл-тов по вертикати").pack()
        self.slave.message2 = Entry(self.slave, textvariable=self.y).pack()
        self.slave.label3 = Label(self.slave, text="Значения структурирующего элемента").pack()
        self.slave.message3 = Entry(self.slave, textvariable=self.z).pack()
        self.button = Button(self.slave, text="Применить", command=self.do_erozia)
        self.button.pack()

    def do_erozia(self):
        x = int(self.x.get())
        y = int(self.y.get())
        z = self.z.get().split(' ')
        mas = []
        k = 0
        for i in range(y):
            mas_str = []
            for j in range(x):
                mas_str.append(int(z[k]))
                k += 1
            mas.append(mas_str)

        img_tansform = self.img.copy()
        s = self.img.size

        width = s[0]
        height = s[1]
        nw = math.ceil(x / 2)
        nh = math.ceil(y / 2)

        trans_image = Image.new("RGB", (width, height), (0, 0, 0))
        obj = img_tansform.load()

        for i in range(0, width):
            for j in range(0, height):
                rn = 0
                for k in range(x):
                    for p in range(y):
                        # print(i, j, k, p)
                        # print(i + k - nw + 1, j + p - nh + 1)
                        if ((i + k - nw + 1) >= 0) and ((i + k - nw + 1) <= (width - 1)) and (
                                (j + p - nh + 1) >= 0) and ((j + p - nh + 1) <= (height - 1)) and (mas[k][p] != 0):
                            rn += obj[i + k - nw + 1, j + p - nh + 1][0]
                            # print("take")
                            # print(i,j,k,p)
                            # print(i+k-nw+1, j+p-nh+1)
                            # print("-------")
                if rn == 0:
                    trans_image.putpixel((i, j), (0, 0, 0))
                else:
                    trans_image.putpixel((i, j), (255, 255, 255))

        child("Дилатация", trans_image)

class zamikanie_param:
    def __init__(self, my_image):
        self.img = my_image
        self.x = StringVar()
        self.y = StringVar()
        self.z = StringVar()
        self.slave = Toplevel(root)
        self.slave.title("Размеры структурирующего элемента")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="Кол-во эл-тов по горизонтали").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.slave.label2 = Label(self.slave, text="Кол-во эл-тов по вертикати").pack()
        self.slave.message2 = Entry(self.slave, textvariable=self.y).pack()
        self.slave.label3 = Label(self.slave, text="Значения структурирующего элемента").pack()
        self.slave.message3 = Entry(self.slave, textvariable=self.z).pack()
        self.button = Button(self.slave, text="Применить", command=self.do_zamikanie)
        self.button.pack()

    def do_zamikanie(self):
        x = int(self.x.get())
        y = int(self.y.get())
        z = self.z.get().split(' ')
        mas = []
        k = 0
        for i in range(y):
            mas_str = []
            for j in range(x):
                mas_str.append(int(z[k]))
                k += 1
            mas.append(mas_str)

        img_tansform = self.img.copy()
        s = self.img.size

        width = s[0]
        height = s[1]
        nw = math.ceil(x / 2)
        nh = math.ceil(y / 2)

        trans_image = Image.new("RGB", (width, height), (0, 0, 0))
        obj = img_tansform.load()

        for i in range(0, width):
            for j in range(0, height):
                rn = 0
                for k in range(x):
                    for p in range(y):
                        if ((i + k - nw + 1) >= 0) and ((i + k - nw + 1) <= (width - 1)) and (
                                (j + p - nh + 1) >= 0) and ((j + p - nh + 1) <= (height - 1)) and (mas[k][p]!=0):
                            rn += obj[i + k - nw + 1, j + p - nh + 1][0]
                if rn == 0:
                    trans_image.putpixel((i, j), (0, 0, 0))
                else:
                    trans_image.putpixel((i, j), (255, 255, 255))

        trans_image2 = Image.new("RGB", (width, height), (0, 0, 0))
        obj2 = trans_image.load()

        for i in range(0, width):
            for j in range(0, height):
                rn=0
                koef=0
                for k in range(x):
                    for p in range(y):
                        if ((i+k-nw+1)>=0) and ((i+k-nw+1)<=(width-1)) and ((j+p-nh+1)>=0) and ((j+p-nh+1)<=(height-1)) and (mas[k][p]!=0):
                            rn += obj2[i+k-nw+1, j+p-nh+1][0]
                            koef+=1
                if rn == koef*255:
                    trans_image2.putpixel((i,j),(255,255,255))
                else:
                    trans_image2.putpixel((i, j), (0,0,0))

        child("Замыкание", trans_image2)

class razmikanie_param:
    def __init__(self, my_image):
        self.img = my_image
        self.x = StringVar()
        self.y = StringVar()
        self.z = StringVar()
        self.slave = Toplevel(root)
        self.slave.title("Размеры структурирующего элемента")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="Кол-во эл-тов по горизонтали").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.slave.label2 = Label(self.slave, text="Кол-во эл-тов по вертикати").pack()
        self.slave.message2 = Entry(self.slave, textvariable=self.y).pack()
        self.slave.label3 = Label(self.slave, text="Значения структурирующего элемента").pack()
        self.slave.message3 = Entry(self.slave, textvariable=self.z).pack()
        self.button = Button(self.slave, text="Применить", command=self.do_razmikanie)
        self.button.pack()

    def do_razmikanie(self):
        x = int(self.x.get())
        y = int(self.y.get())
        z = self.z.get().split(' ')
        mas = []
        k = 0
        for i in range(y):
            mas_str = []
            for j in range(x):
                mas_str.append(int(z[k]))
                k += 1
            mas.append(mas_str)

        img_tansform = self.img.copy()
        s = self.img.size

        width = s[0]
        height = s[1]
        nw = math.ceil(x / 2)
        nh = math.ceil(y / 2)

        trans_image = Image.new("RGB", (width, height), (0, 0, 0))
        obj = img_tansform.load()

        for i in range(0, width):
            for j in range(0, height):
                rn=0
                koef=0
                for k in range(x):
                    for p in range(y):
                        if ((i+k-nw+1)>=0) and ((i+k-nw+1)<=(width-1)) and ((j+p-nh+1)>=0) and ((j+p-nh+1)<=(height-1)) and (mas[k][p]!=0):
                            rn += obj[i+k-nw+1, j+p-nh+1][0]
                            koef+=1
                if rn == koef*255:
                    trans_image.putpixel((i,j),(255,255,255))
                else:
                    trans_image.putpixel((i, j), (0,0,0))

        trans_image2 = Image.new("RGB", (width, height), (0, 0, 0))
        obj2 = trans_image.load()

        for i in range(0, width):
            for j in range(0, height):
                rn=0
                for k in range(x):
                    for p in range(y):
                        if ((i+k-nw+1)>=0) and ((i+k-nw+1)<=(width-1)) and ((j+p-nh+1)>=0) and ((j+p-nh+1)<=(height-1)) and (mas[k][p]!=0):
                            rn += obj2[i+k-nw+1, j+p-nh+1][0]
                if rn == 0:
                    trans_image2.putpixel((i,j),(0,0,0))
                else:
                    trans_image2.putpixel((i, j), (255,255,255))

        child("Размыкание", trans_image2)


class nibl_param:
    def __init__(self, my_image):
        self.num = 0
        self.img = my_image
        self.x = StringVar()
        self.y = StringVar()

        self.slave = Toplevel(root)
        self.slave.title("Параметры бинаризации")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="W - размер окрестности").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.slave.label2 = Label(self.slave, text="Коэффициент K").pack()
        self.slave.message2 = Entry(self.slave, textvariable=self.y).pack()

        self.button = Button(self.slave, text="Применить", command=self.do_nibl)
        self.button.pack()

    # def do_nibl(self):
    #     w = int(self.x.get())
    #     koef = float(self.y.get())
    #     nw = int((w-1)/2)
    #     #nw = w
    #     img_tansform = self.img.copy()
    #     sz = self.img.size
    #     width = sz[0]
    #     height = sz[1]
    #     obj = img_tansform.load()
    #     new_image = Image.new("RGB", (width, height))
    #
    #     for i in range(width):
    #         for j in range(height):
    #             R, G, B = obj[i, j]
    #             S = (R + G + B) // 3
    #             new_image.putpixel((i, j), (S, S, S))
    #     new_obj = new_image.load()
    #
    #     for i in range(nw, width - nw):
    #         for j in range(nw, height - nw):
    #             mean = 0
    #             s=0
    #             t=0
    #             for k in range(w):
    #                 for p in range(w):
    #                     mean += new_obj[i+k-nw, j+p-nw][0]
    #             mean = mean/(w**2)
    #             for k in range(w):
    #                 for p in range(w):
    #                     s += (new_obj[i+k-nw, j+p-nw][0]-mean)**2
    #             s = math.sqrt(s/(w**2))
    #             t = mean + koef*s
    #             if new_obj[i, j][0] > t:
    #                 img_tansform.putpixel((i, j), (255, 255, 255))
    #             else:
    #                 img_tansform.putpixel((i, j), (0,0,0))
    #
    #     child("Фильтр", img_tansform)

    def do_nibl(self):
        w = int(self.x.get())
        koef = float(self.y.get())
        img_tansform = self.img.copy()
        sz = self.img.size
        width = sz[0]
        height = sz[1]
        obj = img_tansform.load()
        new_image = Image.new("RGB", (width, height))
        for i in range(width):
            for j in range(height):
                R, G, B = obj[i, j]
                S = (R + G + B) // 3
                new_image.putpixel((i, j), (S, S, S))
        new_obj = new_image.load()


        for i in range(width):
            for j in range(height):
                mean = 0
                s=0
                t=0
                razm =0
                for k in range(-w, w+1):
                    for p in range(-w, w+1):
                        if ((i+k)>0) and ((i+k)<width) and ((j+p)>0) and ((j+p)<height):
                            mean += new_obj[i+k, j+p][0]
                            razm+=1
                mean = mean/razm
                for k in range(-w, w + 1):
                    for p in range(-w, w + 1):
                        if ((i + k) > 0) and ((i + k) < width) and ((j + p) > 0) and ((j + p) < height):
                            s += (new_obj[i+k, j+p][0]-mean)**2
                s = math.sqrt(s/razm)
                t = mean + koef*s
                if new_obj[i, j][0] > t:
                    img_tansform.putpixel((i, j), (255, 255, 255))
                else:
                    img_tansform.putpixel((i, j), (0,0,0))

        child("Фильтр", img_tansform)

class arif_code:
    def __init__(self):
        self.x = StringVar()
        self.y = StringVar()
        self.slave = Toplevel(root)
        self.slave.title("Арифметическая кодировка")
        self.slave.geometry('400x300+200+100')
        self.slave.label1 = Label(self.slave, text="Текст для кодирования").pack()
        self.slave.message1 = Entry(self.slave, textvariable=self.x).pack()
        self.button1 = Button(self.slave, text="Кодировать", command=self.do_code)
        self.button1.pack()
        self.slave.message2 = Entry(self.slave, width = 60)
        self.slave.message2.pack()
        self.slave.label3 = Label(self.slave, text="Числовое значение для декодировки").pack()
        self.slave.message3 = Entry(self.slave, textvariable=self.y).pack()
        self.button2 = Button(self.slave, text="Декодировать", command=self.do_decode)
        self.button2.pack()
        self.slave.message4 = Entry(self.slave)
        self.slave.message4.pack()

        self.dict= {
            'А': [0, 0.06666666],
            'В': [0.0666666, 0.133333333333],
            'Е': [0.1333333333, 0.2],
            'И': [0.2, 0.266666666666],
            'К': [0.2666666666, 0.3333333333],
            'Л': [0.3333333333, 0.39999999999],
            'М': [0.3999999999, 0.46666666666],
            'Н': [0.4666666666, 0.5333333333333],
            'О': [0.533333333, 0.6],
            'Р': [0.6, 0.66666666666],
            'С': [0.66666666, 0.7333333333],
            'Т': [0.733333333, 0.7999999999],
            'У': [0.7999999999, 0.8666666666],
            'Я': [0.866666666, 0.9333333333],
            '!': [0.9333333333, 1]
        }

        # self.dict = {
        #     'a':[0, 0.2],
        #     'e':[0.2, 0.5],
        #     'i':[0.5, 0.6],
        #     'o':[0.6, 0.8],
        #     'u':[0.8, 0.9],
        #     '!':[0.9 , 1]
        #  }

    def do_code(self):
        x = list(self.x.get().upper())
        OldLow=0
        OldHigh=1
        for i in x:
            NewHigh = OldLow + (OldHigh - OldLow) * self.dict[i][1]
            NewLow = OldLow + (OldHigh - OldLow) * self.dict[i][0]
            OldLow = NewLow
            OldHigh = NewHigh
        out = str(NewLow)+': '+str(NewHigh)
        self.slave.message2.insert(0, out)

    def do_decode(self):
        y = float(self.y.get())
        s = ''
        while (y < self.dict['!'][0]):
            for i in self.dict:
                print(i)
                if (y < self.dict[i][1]) and (y >= self.dict[i][0]):
                    s = s+i
                    y = (y - self.dict[i][0])/(self.dict[i][1]-self.dict[i][0])
                    break
        self.slave.message4.insert(0, s)



# создание окна
root = Tk()

# запуск окна
main()