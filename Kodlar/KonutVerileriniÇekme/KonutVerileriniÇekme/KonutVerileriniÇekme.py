from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Bu haz�r fonksyonumuz ad�ndan da anla��laca�� �zere listeyi string t�r�ne �eviriyor.
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

# Bu a�amada selenium ile veri �ekmeye ba�l�yoruz.

# chrome driverin yolunu veriyoruz. Selenium u kullanmak i�in gereklidir.
driver_path = "C:\Driver\chromedriver.exe"
# browser ad�nda bi de�i�ken olu�turuyoruz ve driver yolumuzu veriyoruz. 
browser = webdriver.Chrome(driver_path)
# browser � tam ekran yap�yoruz
browser.maximize_window()
# browser get ile verdi�imiz adres de ki web sitesine gitmi� oluyoruz.
browser.get("https://www.emlakjet.com/satilik-konut/tekirdag-kapakli/17/")

# �imdi bu sayfa i�inde her linke t�klayarak verileri �ekece�iz sonra o sayfadan ��k�p bi alt�nda ki evin linke girip onun 
# verilerini alarak s�rayla bu i�lemi devam ettirece�iz.

# �uan da web sitesinin aray�z�ndeyiz. Amac�m�z evlerin detaylar�na bakmak i�in linke t�klamak. Bunu da xpathlere g�re yapaca��z
# neden hepsini tek d�ng� de yapmad�k. ��nk� arada reklamlar oldu�u i�in pathler kar���yor. Reklamlar� atlamak i�in
# b�yle bi yol izledim.
a = 1
while a<=2:
    # t�kla ad�nda de�i�kene find diyerek bu xpath de 1. olana gidiyor.
    tikla = browser.find_element("xpath","/html/body/div/div/div[3]/div[1]/div/div[7]/div[1]/div["+str(a)+"]")
    # click diyerek de bu linke t�kl�yor ve evin detaylar�na bakmak i�in sayfaya girmi� oluyoruz.
    tikla.click()
    # sitenin y�klenmesini bekliyoruz.
    time.sleep(1)
    # �zelliklerin hepsini almak i�in bu sefer bu kod ile orda ki css blo�una g�re veriyi �ekece�iz.
    elements = browser.find_elements(By.CSS_SELECTOR, "._3tH_Nw")
    # �zellikleri bir �nceki kodda ald�k �imdi de evin fiyat�n� al�yoruz ve de�i�kene kaydediyoruz.
    fiyatlar = browser.find_elements(By.CSS_SELECTOR,"._2TxNQv")
    # 2 tane bo� liste olu�turuyoruz. Elimizde ki da��n�k veriyi d�zenleyip listeye ataca��z.
    detaylar = []
    fiyat = []
    # �ekti�imiz veriler text string olmad��� i�in verileri stringe �evirip demin olu�turdu�umuz bo� listeye at�yoruz.
    # veriler �ekildi�inde liste olarak gelir
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # �zellikleri de stringe �evirerek listeye at�yoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    # elimizde string olan liste halinde veriler var.
    # �nceden olu�turdu�umuz listeden stringe �evirme fonksyonuyla stringe �eviyoruz.
    det_str = listToString(detaylar)
    # string verimizi split ile sat�rlara g�re ay�r�yoruz. Ve ayr� ad�nda de�i�kene at�yoruz.
    ayri = det_str.split("\n")
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[4:26]
    df_yeni.iloc[21] = df_yeni.iloc[21]
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    icerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        icerikler.append(df_liste[i])
        i= i+2
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    e=10
    while e <=100:
        fiyat_sade = fiyat_sade.replace("arrow_downward%"+str(e),"")
        e = e+1
    d=0
    while d <=10:
        fiyat_sade = fiyat_sade.replace("arrow_downward%"+str(d),"")
        d = d+1
    icerikler.append([fiyat_sade])
    df_icerikler = pd.DataFrame(icerikler).T
    # verimizi csv dosyas�na �eviriyoruz ve modu append yap�yoruz. ��nk� di�er �ekti�imiz verileri de oraya ekleyece�iz.
    # e�er mode = a yapmassak di�er gelen veriyi �zerine yazacakt�r.
    df_icerikler.to_csv(r"emlakjet.csv",encoding="utf-8-sig",index=False, mode="a")
    
    # a de�i�keni sayfada ki evlerin xpath de ki say�s�yd�
    a = a+1
    # bu kod ile bi �nceki sayfaya ge�iyoruz.
    browser.execute_script("window.history.go(-1)")
print("ilk kisim calisti")
fiyat_sade = 0
j = 4
while j <= 7:
    tikla = browser.find_element("xpath","/html/body/div/div/div[3]/div[1]/div/div[7]/div[1]/div["+str(j)+"]")
    tikla.click()
    time.sleep(1)
    elements = browser.find_elements(By.CSS_SELECTOR, "._3tH_Nw")
    fiyatlar = browser.find_elements(By.CSS_SELECTOR,"._2TxNQv")
    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    
    det_str = listToString(detaylar)
    ayri = det_str.split("\n")
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[4:26]
    df_yeni.iloc[21] = df_yeni.iloc[21]
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    icerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        icerikler.append(df_liste[i])
        i= i+2
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    e=10
    while e <=100:
        fiyat_sade = fiyat_sade.replace("arrow_downward%"+str(e),"")
        e = e+1
    d=0
    while d <=10:
        fiyat_sade = fiyat_sade.replace("arrow_downward%"+str(d),"")
        d = d+1
    icerikler.append([fiyat_sade])
    df_icerikler = pd.DataFrame(icerikler).T

    df_icerikler.to_csv(r"emlakjet.csv",encoding="utf-8-sig",index=False, mode="a")
    j = j+1
    browser.execute_script("window.history.go(-1)")

print("ikinci kisim calisti")

k = 9
while k<=10:
    tikla = browser.find_element("xpath","/html/body/div/div/div[3]/div[1]/div/div[7]/div[1]/div["+str(k)+"]")
    tikla.click()
    time.sleep(1)
    elements = browser.find_elements(By.CSS_SELECTOR, "._3tH_Nw")
    fiyatlar = browser.find_elements(By.CSS_SELECTOR,"._2TxNQv")
    detaylar = []
    fiyat = []

    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    
    det_str = listToString(detaylar)
    ayri = det_str.split("\n")
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[4:26]
    df_yeni.iloc[21] = df_yeni.iloc[21]
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    icerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        icerikler.append(df_liste[i])
        i = i+2
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    e=10
    while e <=100:
        fiyat_sade = fiyat_sade.replace("arrow_downward%"+str(e),"")
        e = e+1
    d=0
    while d <=10:
        fiyat_sade = fiyat_sade.replace("arrow_downward%"+str(d),"")
        d = d+1
    icerikler.append([fiyat_sade])
    df_icerikler = pd.DataFrame(icerikler).T

    df_icerikler.to_csv(r"emlakjet.csv",encoding="utf-8-sig",index=False, mode="a")
    k = k+1
    browser.execute_script("window.history.go(-1)")

print("ucuncu kisim calisti")
df_emlakjet = pd.read_csv("emlakjet.csv", error_bad_lines=False)
i = 1
while i <= 14:
    df_emlakjet.drop(i,inplace = True)
    i=i+2
df_emlakjet = df_emlakjet.reset_index()
df_emlakjet.drop("index", axis = 1, inplace = True)
df_emlakjet.to_excel("emlakjet.xlsx")

#l = 12
#while l<=13:
 #   browser.execute_script("window.scrollBy(0,400)","")
 #   tikla = browser.find_element("xpath","/html/body/div/div/div[3]/div[1]/div/div[7]/div[1]/div["+str(l)+"]")
 #   tikla.click()
 #   time.sleep(1)
 #   elements = browser.find_elements(By.CSS_SELECTOR, "._3tH_Nw")
 #   fiyatlar = browser.find_elements(By.CSS_SELECTOR,"._2TxNQv")
 #   detaylar = []
#    fiyat = []

#    for i in fiyatlar:
 #       print(i.text)
 #       fiyat.append(i.text)
    
 #   for i in elements:
 #       print(i.text)
 #       detaylar.append(i.text)
    
#    det_str = listToString(detaylar)
#    ayri = det_str.split("\n")
#    df = pd.DataFrame(ayri)
 #   df_yeni = df.iloc[4:26]
#    df_yeni = df_yeni.reset_index()
#    df_yeni.drop("index", axis = 1, inplace = True)
#    df_liste = df_yeni.values.tolist()
#    icerikler =[]
#    fiyat_sade = fiyat[1].strip()
#    fiyat_sade = fiyat_sade.replace("TL","")
#    i = 1
#    while i <= 21:
#        print(df_liste[i])
#        icerikler.append(df_liste[i])
#        i= i+2
#    fiyat_sade = fiyat[1].strip()
#    fiyat_sade = fiyat_sade.replace("TL","")
#    icerikler.append([fiyat_sade])
#    df_icerikler = pd.DataFrame(icerikler).T

#    df_icerikler.to_csv(r"emlakjet.csv",encoding="utf-8-sig",index=False, mode="a")
#    l = l+1
#    browser.execute_script("window.history.go(-1)")

#print("dorduncu kisim calisti")
#m = 15
#while m<=34:
#    browser.execute_script("window.scrollBy(0,225)","")
#    tikla = browser.find_element("xpath","/html/body/div/div/div[3]/div[1]/div/div[7]/div[1]/div["+str(m)+"]")
#    tikla.click()
#    time.sleep(1)
#    elements = browser.find_elements(By.CSS_SELECTOR, "._3tH_Nw")
#    fiyatlar = browser.find_elements(By.CSS_SELECTOR,"._2TxNQv")
#    detaylar = []
#    fiyat = []

#    for i in fiyatlar:
#        print(i.text)
#        fiyat.append(i.text)
    
#    for i in elements:
#        print(i.text)
#        detaylar.append(i.text)
    
#    det_str = listToString(detaylar)
#    ayri = det_str.split("\n")
#    df = pd.DataFrame(ayri)
#    df_yeni = df.iloc[4:26]
#    df_yeni.iloc[21] = df_yeni.iloc[21]
#    df_yeni = df_yeni.reset_index()
#    df_yeni.drop("index", axis = 1, inplace = True)
#    df_liste = df_yeni.values.tolist()
#    icerikler =[]
#    fiyat_sade = fiyat[1].strip()
#    fiyat_sade = fiyat_sade.replace("TL","")
#    i = 1
#    while i <= 21:
#        print(df_liste[i])
#        icerikler.append(df_liste[i])
#        i= i+2
#    fiyat_sade = fiyat[1].strip()
#    fiyat_sade = fiyat_sade.replace("TL","")
#    icerikler.append([fiyat_sade])
#    df_icerikler = pd.DataFrame(icerikler).T

#    df_icerikler.to_csv(r"emlakjet.csv",encoding="utf-8-sig",index=False, mode="a")
#    m = m+1
#    browser.execute_script("window.history.go(-1)")

#print("besinci kisim calisti")