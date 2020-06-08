liste = ['1','2','5a','10b','abc','10','50']

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

for i in liste:
	try:
		i = int(i)
		print(i)
	except Exception as err:
		print(err)
		continue	


# 2: kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
	
	try:
		x = input('bir sayı giriniz:')
		if x =='q':
			break		
		x = int(x)
	except Exception as err:
		print('sadece rakam girebilirsiniz')
		print(err)

# 3: girilen parola içinde türkçe karakter hatası veriniz.


def check_pw(pw):	
	turkishletters = 'şıİçğüö'
	for i in pw:
		if i in turkishletters:
			raise TypeError('Türkçe karakter hatası alındı')
	print('giriş başarılı')

pw = input('parolanızı giriniz : ')
try:
	check_pw(pw)
except TypeError as err:
	print(err)

# 4: faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verin.

def faktoryel(x):
	if type(x) != int:
		raise TypeError('Yalnızca rakam girebilirsiniz')
	result=1
	for i in range(1,x+1):		
		result *= i
	print(result)		


try:
	
	faktoryel(90)
except TypeError as err:
	print(err)
finally:
	print('işlem tamamlandı')
