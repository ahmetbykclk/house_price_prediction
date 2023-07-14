from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Bu hazýr fonksyonumuz adýndan da anlaþýlacaðý üzere listeyi string türüne çeviriyor.
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

# Bu aþamada selenium ile veri çekmeye baþlýyoruz.

# chrome driverin yolunu veriyoruz. Selenium u kullanmak için gereklidir.
driver_path = "C:\Driver\chromedriver.exe"
# browser adýnda bi deðiþken oluþturuyoruz ve driver yolumuzu veriyoruz. 
browser = webdriver.Chrome(driver_path)
# browser ý tam ekran yapýyoruz
browser.maximize_window()
# browser get ile verdiðimiz adres de ki web sitesine gitmiþ oluyoruz.
browser.get("https://www.emlakjet.com/satilik-konut/tekirdag-kapakli/17/")

# þimdi bu sayfa içinde her linke týklayarak verileri çekeceðiz sonra o sayfadan çýkýp bi altýnda ki evin linke girip onun 
# verilerini alarak sýrayla bu iþlemi devam ettireceðiz.

# Þuan da web sitesinin arayüzündeyiz. Amacýmýz evlerin detaylarýna bakmak için linke týklamak. Bunu da xpathlere göre yapacaðýz
# neden hepsini tek döngü de yapmadýk. çünkü arada reklamlar olduðu için pathler karýþýyor. Reklamlarý atlamak için
# böyle bi yol izledim.
a = 1
while a<=2:
    # týkla adýnda deðiþkene find diyerek bu xpath de 1. olana gidiyor.
    tikla = browser.find_element("xpath","/html/body/div/div/div[3]/div[1]/div/div[7]/div[1]/div["+str(a)+"]")
    # click diyerek de bu linke týklýyor ve evin detaylarýna bakmak için sayfaya girmiþ oluyoruz.
    tikla.click()
    # sitenin yüklenmesini bekliyoruz.
    time.sleep(1)
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloðuna göre veriyi çekeceðiz.
    elements = browser.find_elements(By.CSS_SELECTOR, "._3tH_Nw")
    # özellikleri bir önceki kodda aldýk þimdi de evin fiyatýný alýyoruz ve deðiþkene kaydediyoruz.
    fiyatlar = browser.find_elements(By.CSS_SELECTOR,"._2TxNQv")
    # 2 tane boþ liste oluþturuyoruz. Elimizde ki daðýnýk veriyi düzenleyip listeye atacaðýz.
    detaylar = []
    fiyat = []
    # çektiðimiz veriler text string olmadýðý için verileri stringe çevirip demin oluþturduðumuz boþ listeye atýyoruz.
    # veriler çekildiðinde liste olarak gelir
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atýyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    # elimizde string olan liste halinde veriler var.
    # Önceden oluþturduðumuz listeden stringe çevirme fonksyonuyla stringe çeviyoruz.
    det_str = listToString(detaylar)
    # string verimizi split ile satýrlara göre ayýrýyoruz. Ve ayrý adýnda deðiþkene atýyoruz.
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
    # verimizi csv dosyasýna çeviriyoruz ve modu append yapýyoruz. Çünkü diðer çektiðimiz verileri de oraya ekleyeceðiz.
    # eðer mode = a yapmassak diðer gelen veriyi üzerine yazacaktýr.
    df_icerikler.to_csv(r"emlakjet.csv",encoding="utf-8-sig",index=False, mode="a")
    
    # a deðiþkeni sayfada ki evlerin xpath de ki sayýsýydý
    a = a+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
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