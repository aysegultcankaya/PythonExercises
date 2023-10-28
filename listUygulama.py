# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
list=["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
print(list)

# 2-  Liste Kaç elemanlıdır ?
print(len(list))

# 3-  Listenin ilk ve son elemanı nedir ?
print(list[0],list[-1])

# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
list[0]="Samsung S9"
print(list)

# 5-  "Samsung S6" listenin bir elemanı mıdır ?
text2=list.index("Samsung S6")
print(text2)


# 6-  Listenin -3 indeksindeki değer nedir ?
print(list[-3])

# 7-  Listenin ilk 2 elemanını alın.
print(list[:2])


# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
list[2:]=["Samsung S9" , "Samsung S10" ]
print(list) 


# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
x=("IPhone X", "IPhone XR" )
list.extend(x)
print(list)

# 10- Listenin son elemanını silin.
list.pop()
print(list)


# 11- Liste elemanlarını tersten yazdırınız.
print(list[::-1])


# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
      # kullaniciB: Sena Turan  1999, (80,80,70)
      # kullaniciC: Ahmet Turan 1998, (80,70,90)


kullaniciA=["Yiğit", "Bilgi",2010, [70,60,70]]
kullaniciB=["Sena" ,"Turan" , 1999, [80,80,70]]
kullaniciC=["Ahmet", "Turan", 1998, [80,70,90]]

kullanıcılar=[kullaniciA,kullaniciB,kullaniciC]
print (kullanıcılar)
# for x in kullanıcılar:
#     print(x)



# 13- Liste elemanlarını ekrana yazdırınız.
for a in list:
   print(a)

