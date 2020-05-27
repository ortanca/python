#kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
"""users = {}
ed_list = ['ilkokul', 'lise', 'üniversite']
username = input('adınızı giriniz : ')
userage = int(input('yaşınızı giriniz : '))
usereducation = input('eğitim durumunuzu girin (ilkokul, lise, üniversite) : ')

users.update({
	'isim' : username,
	'yaş'  : userage,
	'eğitim durumu' : usereducation
})

bd_condition = userage >= 18
edlist_check = usereducation.lower().strip() in ed_list
ed_condition = usereducation == ed_list[1] or usereducation == ed_list[2]

if bd_condition and ed_condition:
	print('ehlitini al ve toz ol')
else :
	print('sana ehliyet mehliyet yok')"""


#bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
"""0-24 = 0
25-44 =1
45-54 =2
55=69 =3
70-84 =4
85-100 = 5
"""

"""ilkyazili = int(input('1.yazılı notunuzu girin: '))
ikinciyazili = int(input('2.yazılı notunuzu girin: '))
sozlu = int(input('sözlü notunuzu girin: '))

ortalama = int((ilkyazili + ikinciyazili + sozlu)/3)

if ortalama >= 0 and ortalama < 25:
	print(f'ortalaman {ortalama} daha çok çalışman lazım.')
elif ortalama >= 25 and ortalama <= 54:
	print(f'ortalaman {ortalama} kıl payı yırttın, daha fazla çalış.')
elif ortalama >= 55 and ortalama <= 69:
	print(f'ortalaman {ortalama} fena değil, idare eder.')
elif ortalama >= 70 and ortalama <= 84:
	print(f'ortalaman {ortalama} güzel.')
else: 
	print(f'ortalaman {ortalama} bu dünyayı sen mi kurtaracaksın, azıcık oyun oyna')"""

#trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
"""1.bakım= 1.yıl
2.bakım= 2.yıl
3.bakım= 3.yıl
4.bakım= 4.yıl
5.bakım= 5.yıl
6.bakım= 6.yıl"""
#süre hesabı alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#date time modülünü kullanmanız gerekiyor.
"""
import datetime

year = int(input('çıkış yılını yazınız : '))
month = int(input('çıkış ayını yazınız : '))
day = int(input('çıkış gününü yazınız : '))

a = datetime.datetime.now()
b = datetime.datetime(year, month, day)

fark = (a - b)
result = fark.days / 365
print(result)

if result > 0 and result < 1 : 
	print('birinci bakım dönemindesiniz')
elif result > 1 and result < 2  :
	print('ikinci bakım dönemindesiniz')
elif result > 2 and result < 3  :
	print('üçüncü bakım dönemindesiniz')
else: 
	print('bakım günü çoktan geçmiş')


"""

#girilen bir sayının 0 ve 100 arasında olup olmadığını kontrol ediniz

"""sayi = int(input('bir sayı giriniz : '))

if sayi > 0 and sayi < 100 :
	print(f'{sayi} sıfır ve yüz arasındadir')
else :
	print(f'{sayi} sıfır ve yüz arasında değildir')"""


# girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
"""
sayi = int(input('bir sayi giriniz : '))

if sayi > 0 : 
	if sayi % 2 == 0 : 
		print('sayi pozitif bir çift sayidir')
	else:
		print('sayi pozitif bir tek sayidir')
elif sayi < 0 and sayi % 2 == 0 :
	print('sayi negatif bir çift sayidir')
else :
	print('sayi negatif bir tek sayidir')"""

# email ve parola bilgileriyle giriş kontrolü yapınız
users = {
	'ortanca' : {
		'email': 'ahmet@email.com',
		'password':'1234abc'
	}	
}

username = input('kullanıcı adınızı giriniz : ')


if username in users :	
	usermail = input(' kullanıcı adı doğru, mail adresinizi giriniz : ')
	if usermail == users['ortanca']['email'] :
		userpw   = input('şifrenizi giriniz : ')
		if userpw == users['ortanca']['password']:
			print('giriş işleminiz başarılı')
		else :
			userpw   = input('yanlış bir şifre girdiniz, yeniden deneyin : ')
	else : 
		usermail = input('yanlış bir mail adresi girdiniz, yeniden deneyin : ')
else :
	username = input('yanlış bir kullancı adı girdiniz, yeniden deneyin : ')
