urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
    {'name':'iphone XR', 'price': '7000' },
    {'name':'iphone 11', 'price': '8000' },
    {'name':'samsung s10', 'price': '6000' },
]

# 1- Tüm ürün bilgilerini listeleyiniz.
for a in urunler:
     print(f"ürün adı: {a['name']} ve ürün fiyatı: {a['price']} TL")


# 2- Ürünlerin fiyatları toplamı nedir ?
toplam=0
for i in urunler:
     price=int(a['price'])
     toplam=toplam+price
print(toplam)
     
# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
for x in urunler:
    fiyat=int(x["price"])
    if (fiyat<=6000):
        print(f"ürün adı {x['name']} ürün fiyatı: {x['price']}")

# for urun in urunler:
#      if (int(urun['price']) <= 6000):
#          print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")

# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.

kelime = input('aramak istediğiniz ürün: ')
for z in urunler:
    if (z["name"].find(kelime.lower()))>-1:
        print(z["name"])


