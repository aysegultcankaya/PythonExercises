#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

i=0
urunler=[]
urunSayi=int((input("Ürün saysı giriniz= ")))

while (i<urunSayi):
    urunAd=input("Ürün adı:")
    urunFiyat=int(input("Ürün Fiyatı:"))
    urunler.append({"urunAd":urunAd,"urunFiyat":urunFiyat})
    # urunler.update({"urunAd":urunAd,"urunFiyat":urunFiyat})
    i+=1

print(urunler)


