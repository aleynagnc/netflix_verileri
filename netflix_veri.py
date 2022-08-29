import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime


netflix_v = pd.read_csv("NetflixOriginals.csv", encoding="ISO-8859-1")

#print(netflix_v.to_string())

#1-)Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.

uzun_soluklu_film_suresi=100

uzun_soluklu_filmler = netflix_v[netflix_v.Runtime > uzun_soluklu_film_suresi]
uzun_soluklu_filmler.reset_index(drop=True, inplace=True)

#print(uzun_soluklu_filmler.to_string())

#sayi = uzun_soluklu_filmler["Language"].value_counts()
#print(sayi)

fig = plt.figure(figsize=(12,12))
grafik= plt.bar( uzun_soluklu_filmler["Language"], uzun_soluklu_filmler["Runtime"], label="Dillere göre süreler")
plt.title("Dillere göre süre grafiği")
plt.xticks(rotation = 90)
#print(plt.show())

#2-)2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.

netflix_v["Premiere"]=pd.to_datetime(netflix_v["Premiere"])
#netflix_v.sort_values(by="IMDB Score", inplace=True)

tarih_siralama = netflix_v[(netflix_v["Genre"] == "Documentary") & (netflix_v["Premiere"] >= "2019-01-01") & (netflix_v["Premiere"] <= "2020-06-01") ]
print(tarih_siralama.to_string())

fig2 = plt.figure(figsize=(10,10))
grafik2= plt.bar( tarih_siralama["Title"], tarih_siralama["IMDB Score"])
plt.title("Documentary türünde çekilmiş filmlerin IMDB skoru")
plt.xticks(rotation = 90)
#print(plt.show())

#3-)İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?

ingilizce = netflix_v[netflix_v["Language"] == "English"].sort_values(by="IMDB Score")
ingilizce.reset_index(drop=True, inplace=True)
print(ingilizce.tail(1).Genre)

#4-)'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?

hindi_dili = netflix_v[netflix_v["Language"]=="Hindi"]
ortalama_hindi = hindi_dili.Runtime.mean()
print(ortalama_hindi)

#5-)'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.

genre_ = netflix_v["Genre"].value_counts()
print(genre_.to_string())

fig3=plt.figure(figsize= (12,12))
grafik3 = sns.countplot( netflix_v["Genre"] )
plt.title("Kategori sayıları")
plt.xticks(rotation = 90)
#print(plt.show())

#6-)Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.

en_cok_kullanilan_dil = netflix_v["Language"].value_counts()
print(en_cok_kullanilan_dil.head(3))


#7-)IMDB puanı en yüksek olan ilk 10 film hangileridir?


en_yuksek = netflix_v.sort_values(by="IMDB Score", ascending = False)
print(en_yuksek.head(10).to_string())

#8-)IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.


fig5= plt.figure(figsize=(15,15))
grafik5=plt.scatter(netflix_v["Runtime"], netflix_v["IMDB Score"])
plt.title("IMDB puanı ile 'Runtime' korelasyonu")
#print(plt.show())


#9-)IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.

yuksek_genre = netflix_v.sort_values(by="IMDB Score", ascending=False).drop_duplicates("Genre")[:10]
print(yuksek_genre.to_string())
fig6= plt.figure(figsize=(12,6))
grafik6=plt.bar(yuksek_genre["Genre"], yuksek_genre["IMDB Score"])
plt.title("IMDB puanı yüksek olan ilk 10 tür")
plt.xticks(rotation = 90)
#print(plt.show())

#10-)'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.

runtime_yuksek = netflix_v.sort_values(by="Runtime", ascending=False)[:10]
print(runtime_yuksek.to_string())

fig7= plt.figure(figsize=(12,6))
grafik7=plt.bar(runtime_yuksek["Title"], runtime_yuksek["Runtime"])
plt.title("Runtime yüksek olan ilk 10 tür")
plt.xticks(rotation = 90)
print(plt.show())








