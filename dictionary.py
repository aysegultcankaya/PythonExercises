# 1- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

urunler = { 
            '100': {'ad': 'IPhone 8', 'fiyat': '5000'}, 
            '101': {'ad': 'IPhone X', 'fiyat': '6000'}, 
            '102': {'ad': 'IPhone XR', 'fiyat': '7000'}
        }



id=input("aramak istediğiniz id bilgisini giriniz:")
urun=urunler[id]
print(f"id:{id} ürün adı: {urun['ad']} ürün fiyatı: {urun[ 'fiyat']} ")