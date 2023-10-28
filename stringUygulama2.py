website = "http://www.aysegulturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
text="   Hello World    "
print(text.strip())

# 2- 'www.aysegulturan.com' içindeki aysegulturan bilgisi haricindeki her karakteri silin.

wsite="http://www.aysegulturan.com".split(".")
print(wsite[1])

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
print(kursAdi.lower())

# 4- 'website' içinde kaç tane a karakteri vardır ? 
print(website.count("a"))


# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
print(website.startswith("www"),website.endswith("com"))


# 6- 'website' içinde '.com' ifadesi var mı?
print(website.find(".com"))


# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(kursAdi.isalpha())
print(kursAdi.isdigit())


# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
text2="Contents"
print(text2.center(50,"*"))

# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(kursAdi.replace(" ","-"))

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
text1="Hello World"
text1=text1.replace("World","There")
print(text1)


# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.

print(kursAdi.split(" "))
