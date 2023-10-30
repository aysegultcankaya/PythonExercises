a, b, c = 2, 5, 12

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir ?
x=int(input("sayı 1:"))
y=int(input("sayı 2:"))
carpim=x*y
toplam=a+b+c
print(carpim-toplam)



# 2- c' nin  b' ye kalansız bölümünü hesaplayınız.
print("c' nin  b' ye kalansız bölümünü",c//b)

# 3- (a,b,c) toplamının mod 3' ü nedir ?
print("a,b,c toplamının mod 3'ü=",toplam%3)


# 4- b' nin a. kuvvetini hesaplayınız.
print("b' nin a. kuvveti=",b**a)

# 5- a, *b, c = sayilar işlemine göre c' nin küpü kaçtır ? 
sayilar = 1, 5, 7, 10, 3
a, *b, c = sayilar
print(c**3)



# 6- a, *b, c = sayilar işlemine göre b nin değerleri toplamı kaçtır ?

print(b[0]+b[1]+b[2])