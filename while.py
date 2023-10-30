sayilar = [4,6,9,10,35,57,89,125,244]

# 1: sayilar listesini while ile ekrana yazdırın.
i=0
while (i < len(sayilar)):
       print (sayilar[i])
       i+=1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# ekrana yazdırın.
baslangicDeger=int(input("Başlangıç değeri giriniz: "))
bitisDeger=int(input("Bitiş değeri giriniz: "))

a=baslangicDeger

while (a < bitisDeger):
    a+=1
    if (a%2==1):
        print (a)
           


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
x=100

while (x >0):
    print (x)
    x-=1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
count=[]
y=0
while (y<5):
    sayi=int(input("sayı giriniz: "))
    count.append(sayi)
    y+=1
count.sort()
print(count)



