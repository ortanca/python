numbers = [1,3,5,7,9,12,19,21]

#1 sayilar listesini while ile ekrana yazdırın.
x=0
while x < 7:
	x=x+1
	print(numbers[x])

#2  başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
"""
a = int(input('başlangıç için bir sayı girin : '))
b = int(input('bitiş için bir sayı daha girin : '))

while a < b :
	a=a+1
	if a % 2 != 0 :
		print(f"{a} tek bir sayıdır.")
	else :
		print(f"{a} çift bir sayıdır.") 
"""
#3 1-100 arasındaki sayıları azalan şekilde yazdırın.
x=0 
sayilar=[]
while x < 100 : 
	x=x+1
	sayilar.append(x)
sayilar.reverse()

#4 kullancıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.

"""
b = int(input('bir sayı girin : '))
c = int(input('bir sayı girin : '))
d = int(input('bir sayı girin : '))
e = int(input('bir sayı girin : '))

sayi=[a,b,c,d,e]
sayi.sort()
print(sayi)
"""
#5 kullancıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
# ürün sayısını kullanıcıya sorun 
# dictionary listesi yapısı name,price şeklinde olsun 
# ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

a = int(input('kaç tane ürün girecüü : '))
productlist={}
x=0 
while x < a:
	x=x+1
	itemcode= input('ürün kodunu giriniz: ')
	itemname= input('ürün adını giriniz: ')
	itemprice= input('ürün fiyatını giriniz: ')
	productlist.update({
			itemcode : {
				'name' : itemname,
				'price': itemprice
			}
		})

print(productlist)
 	