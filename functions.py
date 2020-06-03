#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""
def kelimeGoster(a, b):
	i=0
	b = int(b)
	for i in range(b):
		i+=1
		print(a)
kelimeGoster('ahmet' , 5)
def yazdir(kelime, adet):
	print(kelime * adet )

yazdir('merhaba\n', 10 )
"""


# kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
"""

def limitless(*args):
	b = list(args)

	return b
b = limitless(2,3,4,5,6,8,10,20)
print(b)

def listeyeCevir(*params):
	liste=[]

	for param in params:
		liste.append(param)

	return liste

result = listeyeCevir(10,20,30,'merhaba')
print(result)
"""

# gönderilen 2 sayfa arasındaki tüm asal sayıları bulun.
"""
def asalx(a,b):
	aralik = []
	for i in range(a,b):
		i+=1
		aralik.append(i)
	return aralik
aralik = asalx(2,22)

last = aralik[-1]
first = aralik[0]
asalmi = True 

i=first
for i in aralik:
	i += 1
	print(i)

sayi1 = int(input('sayi 1: '))
sayi2 = int(input('sayi 2:'))

def asalSayilariBul(sayi1, sayi2):
	for sayi in range(sayi1, sayi2+1):
		if sayi > 1:
			for i in range(2, sayi):
				if (sayi % i == 0):
					break
			else:
				print(sayi)

asalSayilariBul(sayi1,sayi2)
"""
# kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde yazdirin

def tambolenleribul(sayi):
	tambolenler = []

	for i in range(2, sayi):
		if sayi % i == 0:
			tambolenler.append(i)
	return tambolenler

print(tambolenleribul(22))