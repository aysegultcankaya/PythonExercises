# 1- Çarpım tablosu hazırlayınız.
# for i in range(1,11):
#     print("********************************")
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")




# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..
#    Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir. 

sayi=int(input("Bir sayı giriniz="))

asalMi=True

if (sayi==1):
    print("Sayı asal değildir.")

for i in range(2,sayi):
    if (sayi%i==0):
        asalMi=False
        break

if asalMi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')


