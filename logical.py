# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
x=int(input("sayı giriniz:"))

print(f"{x} sayısı 50-100 arasındadır: {x>50 and x<100}")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
y=(x%2)
print(f"{x} pozitif tek sayıdır : {x>0 and y==1}")

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
# _username = "aysegulturan"
# _password = "1234"

_username = "aysegulturan"
_password = "1234"

username=input("username giriniz=")
password=input("parola:")

isUsername=(username.lower().strip()==_username)
isParola=(password.strip()==_password)

print(f"username doğru mu {isUsername}, parola doğruluğu {isParola}")



# 4- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


ad = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndeks = kg / (hg ** 2)

zayif = (kiloIndeks >= 0) and (kiloIndeks <=18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <=24.9)
kilolu = (kiloIndeks > 24.9) and (kiloIndeks <=29.9)
obez = (kiloIndeks >= 29.9) and (kiloIndeks <=34.9)

print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal: {normal}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez: {obez}")