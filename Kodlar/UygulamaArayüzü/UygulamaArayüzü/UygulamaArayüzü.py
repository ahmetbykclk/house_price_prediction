from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Canvas
from tkinter import ttk
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pandas as pd

df = pd.read_excel("emlakjet.xlsx")
df2 = df.copy()

df = df[["brut_metrekare","binanin_yasi","binanin_kat_sayisi","net_metrekare","oda_sayisi","bulundugu_kat",
         "isitma_tipi","fiyat"]]
X = df.drop(["fiyat"], axis = 1)
y = df["fiyat"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.27, random_state = 11)

xgb = XGBRegressor()
xgb1 = XGBRegressor(colsample_bytree = 0.6, learning_rate = 0.09, max_depth = 2, n_estimators = 1000)
model_xgb = xgb1.fit(X_train, y_train)


pencere = Tk()
pencere.title("Ev Fiyat Tahmini")

pencere.configure(background='#81e6d9')
pencere.geometry("1700x900")
pencere.state("normal")

def mesaj():
    messagebox.showinfo(title="Basarili", message="Secim basarili")

def olumsuz():
    messagebox.showwarning(title="Dikkat", message="Secim Yapmadiniz")


def brut_duzenle():
    global brut
    brut_deger = int(brut_entry.get())
    if(brut_deger > 0):
        brut = brut_deger
        mesaj()
        print(brut_deger)
    else:
        olumsuz()


def yas_duzenle():
    global yas
    yas_deger = yaslar_kutu.get()
    if(yas_deger == "0"):
        yas = 0
        mesaj()
    elif(yas_deger == "1"):
        yas = 1
        mesaj()
    elif(yas_deger == "2"):
        yas = 4
        mesaj()
    elif(yas_deger == "3"):
        yas = 6
        mesaj()
    elif(yas_deger == "4"):
        yas = 7
        mesaj()
    elif(yas_deger == "5-10"):
        yas = 8
        mesaj()
    elif(yas_deger == "11-15"):
        yas = 2
        mesaj()
    elif(yas_deger == "16-20"):
        yas = 3
        mesaj()
    elif(yas_deger == "21 ve uzeri"):
        yas = 5
        mesaj()
    else:
        olumsuz()


def kat1_duzenle():
    global kat1
    kat1_deger = kat1_kutu.get()
    if(kat1_deger == "1"):
        kat1 = 1
        mesaj()
    elif(kat1_deger == "2"):
        kat1 = 2
        mesaj()
    elif(kat1_deger == "3"):
        kat1 = 3
        mesaj()
    elif(kat1_deger == "4"):
        kat1 = 4
        mesaj()
    elif(kat1_deger == "5"):
        kat1 = 5
        mesaj()
    elif(kat1_deger == "6"):
        kat1 = 6
        mesaj()
    elif(kat1_deger == "7"):
        kat1 = 7
        mesaj()
    elif(kat1_deger == "8"):
        kat1 = 8
        mesaj()
    elif(kat1_deger == "9"):
        kat1 = 9
        mesaj()
    elif(kat1_deger == "10"):
        kat1 = 10
        mesaj()
    elif(kat1_deger == "11"):
        kat1 = 11
        mesaj()
    else:
        olumsuz()



def net_duzenle():
    global net
    net_deger = int(net_entry.get())
    if(net_deger > 0):
        net = net_deger
        mesaj()
        print(net_deger)
    else:
        olumsuz()


def oda_duzenle():
    global oda
    oda_deger = oda_kutu.get()
    if(oda_deger == "1"):
        oda = 0
        mesaj()
    elif(oda_deger == "1+1"):
        oda = 1
        mesaj()
    elif(oda_deger == "2+1"):
        oda = 2
        mesaj()
    elif(oda_deger == "3+1"):
        oda = 3
        mesaj()
    elif(oda_deger == "3+2"):
        oda = 4
        mesaj()
    elif(oda_deger == "3.5+1"):
        oda = 5
        mesaj()
    elif(oda_deger == "4+1"):
        oda = 6
        mesaj()
    elif(oda_deger == "4+2"):
        oda = 7
        mesaj()
    elif(oda_deger == "5+1"):
        oda = 8
        mesaj()
    elif(oda_deger == "5+2"):
        oda = 9
        mesaj()
    else:
        olumsuz()


def kat2_duzenle():
    global kat2
    kat2_deger = kat2_kutu.get()
    if(kat2_deger == "-1"):
        kat2 = 0
        mesaj()
    elif(kat2_deger == "-2"):
        kat2 = 1
        mesaj()
    elif(kat2_deger == "1"):
        kat2 = 2
        mesaj()
    elif(kat2_deger == "10"):
        kat2 = 3
        mesaj()
    elif(kat2_deger == "2"):
        kat2 = 4
        mesaj()
    elif(kat2_deger == "3"):
        kat2 = 5
        mesaj()
    elif(kat2_deger == "4"):
        kat2 = 6
        mesaj()
    elif(kat2_deger == "5"):
        kat2 = 7
        mesaj()
    elif(kat2_deger == "7"):
        kat2 = 8
        mesaj()
    elif(kat2_deger == "Bahce Dubleks"):
        kat2 = 9
        mesaj()
    elif(kat2_deger == "Bahce Kati"):
        kat2 = 10
        mesaj()
    elif(kat2_deger == "Duz Giris"):
        kat2 = 11
        mesaj()
    elif(kat2_deger == "Mustakil Kat"):
        kat2 = 12
        mesaj()
    elif(kat2_deger == "Yuksek Giris"):
        kat2 = 13
        mesaj()
    elif(kat2_deger == "Cati Dubleks"):
        kat2 = 14
        mesaj()
    else:
        olumsuz()


def isitma_duzenle():
    global isitma
    isitma_deger = isitma_kutu.get()
    if(isitma_deger == "Kat kaloriferi"):
        isitma = 0
        mesaj()
    elif(isitma_deger == "Kombi dogalgaz"):
        isitma = 1
        mesaj()
    elif(isitma_deger == "Merkezi dogalgaz"):
        isitma = 2
        mesaj()
    elif(isitma_deger == "Yerden isitma"):
        isitma = 3
        mesaj()
    else:
        olumsuz()


baslik_label = Label(pencere, text = "Ev Fiyat Tahmini", font="helvetica 50",borderwidth=20, padx = 550, pady = 40,
                     background = "#90cdf4")        
baslik_label.place(x = 70 ,y = 20)



brut_label = Label(text = "Brut Metrekareyi Giriniz", font="helvetica 12",borderwidth=6)
brut_label.place(x = 100, y = 300)

brut_entry = Entry()
brut_entry.place(x = 100, y = 350)

brut_buton = Button(pencere, text = "Sec", command = brut_duzenle, font="helvetica 12",borderwidth=6)
brut_buton.place(x = 100, y = 400)



yas_label = Label(text = "Bina Yasini Seciniz", font="helvetica 12",borderwidth=6)
yas_label.place(x = 300, y = 300)

yaslar = ["0","1","2","3","4","5-10","11-15","16-20","21 ve uzeri"]
yaslar_kutu = Combobox(pencere, values = yaslar)
yaslar_kutu.place(x = 300, y = 350)

yaslar_buton = Button(pencere, text = "Sec", command = yas_duzenle, font="helvetica 12",borderwidth=6)
yaslar_buton.place(x = 300, y = 400)



kat1_label = Label(pencere, text = "Binanin Kat Sayisini Seciniz", font="helvetica 12",borderwidth=6)
kat1_label.place(x = 500, y = 300)

kat1lar = ["1","2","3","4","5","6","7","8","9","10","11"]
kat1_kutu = Combobox(pencere, values = kat1lar)
kat1_kutu.place(x = 500, y = 350)

kat1_buton = Button(pencere, text = "Sec", command = kat1_duzenle, font="helvetica 12",borderwidth=6)
kat1_buton.place(x = 500, y = 400)



net_label = Label(text = "Net Metrekareyi Giriniz", font="helvetica 12",borderwidth=6)
net_label.place(x = 750, y = 300)

net_entry = Entry()
net_entry.place(x = 750, y = 350)

net_buton = Button(pencere, text = "Sec", command = net_duzenle, font="helvetica 12",borderwidth=6)
net_buton.place(x = 750, y = 400)



oda_label = Label(text = "Oda Sayisini Seciniz", font="helvetica 12",borderwidth=6)
oda_label.place(x = 100, y = 500)

odalar = ["1","1+1","2+1","3+1","3+2","3.5+1","4+1","4+2","5+1","5+2"]
oda_kutu = Combobox(pencere, values = odalar)
oda_kutu.place(x = 100, y = 550)

oda_buton = Button(pencere, text = "Sec", command = oda_duzenle, font="helvetica 12",borderwidth=6)
oda_buton.place(x = 100, y = 600)



kat2_label = Label(text = "Bulundugu Kati Seciniz", font="helvetica 12",borderwidth=6)
kat2_label.place(x = 300, y = 500)

kat2lar = ["-1","-2","1","2","3","4","5","7","10",
            "Bahce Dubleks","Bahce Kati","Mustakil Kat","Cati Dubleks","Duz Giris","Yuksek Giris"]
kat2_kutu = Combobox(pencere, values = kat2lar)
kat2_kutu.place(x = 300, y = 550)

kat2_buton = Button(pencere, text = "Sec", command = kat2_duzenle, font="helvetica 12",borderwidth=6)
kat2_buton.place(x = 300, y = 600)



isitma_label = Label(text = "Isitma Turunu Seciniz", font="helvetica 12",borderwidth=6)
isitma_label.place(x = 500, y = 500)

isitmalar = ["Kat kaloriferi","Kombi dogalgaz",
            "Merkezi dogalgaz","Yerden isitma"]
isitma_kutu = Combobox(pencere, values = isitmalar)
isitma_kutu.place(x = 500, y = 550)

isitma_buton = Button(pencere, text = "Sec", command = isitma_duzenle, font="helvetica 12",borderwidth=6)
isitma_buton.place(x = 500, y = 600)




def hesapla():
    yeni_veri = [[brut],[yas],[kat1],[net],[oda],[kat2],
         [isitma]]  
    yeni_veri = pd.DataFrame(yeni_veri).T

    df = yeni_veri.rename(columns = {0:"brut_metrekare",
                        1:"binanin_yasi",
                        2:"binanin_kat_sayisi",
                        3:"net_metrekare",
                        4:"oda_sayisi",
                        5:"bulundugu_kat",
                        6:"isitma_tipi",})

    pred = model_xgb.predict(df)
    
    if(pred < 0):
        pred = -1*pred
    
    pred = int(pred)
    para_birimi = "TL"
    pred_with_para_birimi = str(pred) + " " + para_birimi
    s2 = Label(pencere, text = pred_with_para_birimi, font="helvetica 20",borderwidth=6, padx = 200, pady = 40)
    s2.place(x = 1210, y = 700)


hesapla_buton = Button(pencere, text = "HESAPLA", command = hesapla, font="helvetica 15",borderwidth=60, padx = 100, pady = 40, background = "#f7fafc")
hesapla_buton.place(x = 1200, y = 300)

mainloop()