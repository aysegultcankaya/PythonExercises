# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 

ad=input("ad:")
yas=int(input("yas:"))
egitim=input("egitim durumu:")

if (yas>=18):
    if(egitim=="lise") or (egitim=="üniversite") :
        print(f" {ad} Ehliyet alabilirsiniz")
    else:
        print(f" {ad} ehliyet almak için eğitiminiz yeteli değil") 
else:
    print(f"{ad} yaşınız küçük")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yazili1=int(input("1.yazılı notu= "))
yazili2=int(input("2.yazılı notu= "))
sozlu=int(input("sözlü notu= "))
ortalamaNot=((yazili1+yazili2+sozlu)/3)

if (ortalamaNot>0 and ortalamaNot<=24):
    print(f"ortlamanız{ortalamaNot}, notunuz=0dır")
elif (ortalamaNot>25 and ortalamaNot<=44):
    print(f"ortlamanız{ortalamaNot}, notunuz=1dır")
elif (ortalamaNot>=45 and ortalamaNot<=54):
    print(f"ortlamanız{ortalamaNot}, notunuz=2dır")
elif (ortalamaNot>=55 and ortalamaNot<=69):
    print(f"ortlamanız{ortalamaNot}, notunuz=3dır")
elif (ortalamaNot>=70 and ortalamaNot<=84):
    print(f"ortlamanız{ortalamaNot}, notunuz=4dır")
elif (ortalamaNot>=85 and ortalamaNot<=100):
    print(f"ortlamanız{ortalamaNot}, notunuz=5dır")



# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih=input("Araç trafiğe çıkış tarihi(yıl/ay/gün)=")
tarih=tarih.split("/")

simdi=datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<= 365):
    print('1.servis bakımı.')
elif (gun>365) and (gun<=365*2):
    print('2.servis bakımı')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis bakımı')
else:
    print('hatalı bilgi girdiniz.')

