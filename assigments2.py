# 1- Girilen 2 sayıdan hangisi büyüktür ?
x=int(input("sayı 1:"))
y=int(input("sayı 2:"))

isBiggest=(x>y)
print(f"{x} {y} den büyüktür:", isBiggest)



# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
a=int(input("sayı giriniz:"))
tekCift=(a%2==0)
print(f"{a} çift sayıdır: {tekCift}")


# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.
b=int(input("sayı giriniz:"))
sonuc=(b>0)
print(f"{b} pozitif sayıdır: {sonuc}")


# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1=float(input("1.vize:"))
vize2=float(input("2.vize:"))
final=float(input("final:"))

ortalama=((((vize1+vize2)/2)*0.6)+(final*0.4))

print(f"ortalama not {ortalama}")


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: info@aysegulturan.com parola:12345)

email="info@aysegulturan.com "
parola="12345"

email_=input("email giriniz=")
parola_=input("parola:")

isEmail=(email_.lower().strip()==email)
isParola=(parola_.strip()==parola)

print(f"email doğru mu {isEmail}, parola doğruluğu {isParola}")
