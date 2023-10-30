# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.

benzinFiyat = 6.69
dizelFiyat = 5.86

ortalamaYakitTuketimi = float(input('100 km deki ortalama yakıt tüketimi: '))
yakitTipi=input("Araba benzin mi dizel mi belirtiniz:")
yol=float(input("Kaç km yol gittiniz:"))

toplamYakitTüketimi=yol*(ortalamaYakitTuketimi/100)

if (yakitTipi=="benzin"):
    print(f"Ödeyeceğiniz tutar={toplamYakitTüketimi*benzinFiyat} ")
elif (yakitTipi=="dizel"):
    print(f"Ödeyeceğiniz tutar={toplamYakitTüketimi*dizelFiyat} ")
else:
    print("yanlış işlem yaptınız")





