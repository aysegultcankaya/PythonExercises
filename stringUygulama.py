website = "http://www.aysegulturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(kursAdi))
print(len(website))

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.
"""print(website[22:])"""
karakterSayi=len(website)
print(website[karakterSayi-3:karakterSayi])

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
part1=kursAdi[:15]
part2=kursAdi[-15:]
print(part1)
print(part2)

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
print(kursAdi[::-1])

# 6- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

text="Hello world"
text=text[:6] +"W"+text[-4:]
print(text)

#7 - 'abc' ifadesini yan yana 3 defa yazdırın.
print("abc "*3)

name, surname, age, job = 'Ali','Turan', 37, 'öğretmen' 

# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Ali Turan, Yaşım 37 ve mesleğim öğretmen.' 
print(f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}")