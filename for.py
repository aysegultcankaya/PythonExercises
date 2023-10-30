sayilar = [1,5,16,35,57,72,75,10]

# 1- sayilar listesindeki her bir elemanı yazdırın.
for i in sayilar:
    print(i)

# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
for a in sayilar:
    if (a%5==0):
        print(a) 

# 3- Sayilar listesinde sayıların toplamı kaçtır ?
toplam=0
for b in sayilar:
    toplam=toplam+b
print(toplam)


# 4- Sayilar listesindeki çift sayıların karesini alınız.
for x in sayilar:
    if (x%2==0):
        print(x,x**2)

urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']

# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
for urun in urunler:
    print(urun[1])   


# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)
count=0
for uruns in urunler:
   index= uruns.find("iphone")
   if (index>-1):
       count=count+1
print(count)




