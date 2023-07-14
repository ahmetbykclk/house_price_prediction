import pandas as pd
from sklearn import preprocessing 
le = preprocessing.LabelEncoder()

df = pd.read_excel("emlakjet.xlsx")
df_2 = df.copy()
df_3 = df.copy()

df_3["turu"] = le.fit_transform(df_2.turu)
df_3["kategorisi"] = le.fit_transform(df_2.kategorisi)
df_3["oda_sayisi"] = le.fit_transform(df_2.oda_sayisi)
df_3["binanin_yasi"] = le.fit_transform(df_2.binanin_yasi)
df_3["isitma_tipi"]  = le.fit_transform(df_2.isitma_tipi)
df_3["kullanim_durumu"] = le.fit_transform(df_2.kullanim_durumu)

df_2.loc[df.bulundugu_kat == "Kot 1 (-1).Kat" , "bulundugu_kat"] = "-1"
df_2.loc[df.bulundugu_kat == "Kot 2 (-2).Kat" , "bulundugu_kat"] = "-2"
df_3['bulundugu_kat'] = df_2['bulundugu_kat'].astype(str)
df_3["bulundugu_kat"] = le.fit_transform(df_2.bulundugu_kat)
df_3.info()
df_3.to_excel("islenmis.xlsx")
