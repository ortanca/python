#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""
def kelimeGoster(a, b):
	i=0
	b = int(b)
	for i in range(b):
		i+=1
		print(a)
kelimeGoster('ahmet' , 5)
"""
# kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
"""

def limitless(*args):
	b = list(args)

	return b
b = limitless(2,3,4,5,6,8,10,20)
print(b)
"""
# gönderilen 2 sayfa arasındaki tüm asal sayıları bulun.

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