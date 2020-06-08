# error / hata => istenen bilgi integer fakat kullanıcı string bir değer girmişse, ortaya bir hata çıkacaktır. 
# bazı temel hatalar:
# print(a) => NameError
# print('1a2') => ValueError
# print(10/0) => ZeroDvisionError
# print('denem'e) => SyntaxError


# error handling / hata yönetimi => ortaya çıkan bu hatayla karşılaşılması durumunda fonksiyonumuzun ya da kodlarımızın ne tepki vereceğini belirliyoruz.

try: # hata gelebilecek olan kod blokları try içerisinde olmalıdır.
	x = int(input('x : '))
	y = int(input('y : '))
	print(x/y)
except ValueError: # öngördüğümüz hata türünü (bu örnekte : ValueEerror) buraya giriyoruz ve ne tepki vermesi gerektiğini belirtiyoruz.
				  # tüm hata kodları için ayrı except satırları oluşturulabilir.
	print('bir karakter hatası alındı')



try:
	x = int(input('x : '))
	y = int(input('y : '))
	print(x/y)
except (ValueError, SyntaxError ) as e: # hataları parantez içinde virgülle ayırarak gruplandırabiliriz. ve "as" ifadesi ile belirlediğimiz bir obje içine
#alabiliriz. yani gruplananmış hatalardan ayrı olarak hata türünü belirlemek için kullanılır.
	print('bir hata alındı')
	print(e)




while True:
	try:
		x = int(input('x : '))
		y = int(input('y : '))
		print(x/y)
	except Exception as ex: # Exception genel bir hata anlamındadır. yani tüm hataların ana başlığı olduğu için tüm hatalar anlamına gelir.
		print('bir hata alındı', e)
	else: # exceptin elsi durumunda bu bloğu çalıştırır.
		break
	finally: #try ya da except bloğunun çalışmasına bakmaksızın son olarak çalışacak kod bloğunu temsil eder.
	# tanımlanan değişkenlerin içeriklerin sonlandırılması aşamasında kullanılabilir.
		print('try except sonlandı')

# Raising an exception / bir hata fırlatma işlemidir. kendi belirlediğimiz bir şarta verilecek hata tepkisi de denebilir.
# daha spesifik bir hata belirlememizi sağlar.

x = 10

if x > 5:
	raise Exception('x 5den büyük değer alamaz.')


def check_pass(pw):
	import re
	if len(pw) < 8:
		raise Exception('parola en az 7 karakter olmalıdır.')
	elif not re.search("[a-z]", pw):
		raise Exception('parola küçük harf içermelidir.')
	elif not re.search("[A-Z]", pw):
		raise Exception('parola büyük harf içermelidir.')
	elif not re.search("[0-9]", pw):
		raise Exception('parola rakam içermelidir.')
	elif not re.search("[_@$]", pw):
		raise Exception('parola alpha numeric karakter içermelidir.')
	elif not re.search("\s", pw):
		raise Exception('parola boşluk içermemelidir.')
	else:
		print('geçerli parola')

pw = "1234567"

try:
	check_pass(pw)
except Exception as err:
	print(err)
else:
	print('geçerli parola')
finally:
	print('validation tamamlandı') # olumlu ya da olumsuz farketmez programın sonunda çalışır.

class Person:
	def __init__(self, name, year):
		if len(name) > 10:
			raise Exception('name alanı en fazla on karakter içerebilir')
		else:
			self.name = name

p = person('ahmet', 1989)