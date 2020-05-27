sayilar = [1,3,5,7,9,12,19,21]

# sayilar listesindeki hangi sayilar 3ün katidir
"""

ucunkatisayilar = []
for x in sayilar :
	if x %3 ==0 :
		ucunkatisayilar.append(x)
		print(f'{x} üçün katidir.')
	else:
		print(f'{x} üçün kati değildir.')
print(f"sayilar listesindeki üçün katı olan sayılar {len(ucunkatisayilar)}")
print(f"sayilar listesindeki üçün katı olmayan sayılar {len(sayilar) - len(ucunkatisayilar)}")
"""

# sayilar listesinde sayilarin toplamı kaçtir
"""
for x in sayilar  :
	print('a')

for x in sayilar:
	(2x-1) % 2 > 0
"""
# sayilar listesindeki tek sayilarin karesini yaziniz.
"""
for x in sayilar:
	if x % 2 != 0:
		print(x**2)
	else:
		print(f'{x} - bu sayi çift bir sayidir')
"""

# şehirlerden hangileri en fazla 5 karakterlidir?
"""
sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

for x in sehirler:
	if len(x) <= 5 :
		print(f"{x} bu kurala uygun.")
	else:
		print(f"{x} şu andan itaberen ocak dışı.")
"""

urunler = [
	{'name' : 'samsung s6', 'price' : '3000'},
	{'name' : 'samsung s7', 'price' : '4000'},
	{'name' : 'samsung s8', 'price' : '5000'},
	{'name' : 'samsung s9', 'price' : '6000'},
	{'name' : 'samsung s10', 'price' : '7000'}
]
#ürünlerin fiyatları toplamı nedir?
prices=[]
for x in urunler: 
	prices.append(int(x['price']))
	print(prices)
result = prices[0] + prices[1] + prices[2] + prices[3] + prices[4]
print(result)
	

#ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.


