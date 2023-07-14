import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("emlakjet.xlsx")
#df.info()
#print(df.describe().T)
#print(df.head())
#print(df.binanin_kat_sayisi.value_counts())
print(df.brut_metrekare.describe())
print(df.net_metrekare.describe())
print(df.fiyat.describe())
df.binanin_kat_sayisi.value_counts().plot.barh()
plt.show()
df.oda_sayisi.value_counts().plot.barh()
plt.show()
df.bulundugu_kat.value_counts().plot.barh()
plt.show()
fig = plt.figure(figsize=(5,15))
df.binanin_yasi.value_counts().plot(kind = 'pie',autopct='%.1f%%');
plt.ylabel("yas", fontsize = 20)
plt.show()
fig = plt.figure(figsize=(20,5))
df.kullanim_durumu.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("Kullanim Durumu");
plt.show()
fig = plt.figure(figsize=(20,5))
df.isitma_tipi.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("isitma tipi");
plt.show()