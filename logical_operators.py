#girilen bir sayının 0-100 arasında olup olmadığını kontrol edin.

"""print('bilge dede sorar;')
sayi = int(input('kendine bir iyilik yap ve bana bir sayi söyle evlat: '))
result = (sayi > 0 ) and (sayi < 100)
print(f"evladım bana söylediğin sayinin 0-100 arasinda olma durumu : {result}")"""

# girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz. 

"""print('bilge dede sorar;')
sayi = int(input('kendine bir iyilik yap ve bana bir sayi söyle evlat: '))
result = (sayi > 0 ) and (sayi % 2 == 0)
print(f"evladım bana söylediğin sayinin pozitif çif sayı olma durumu : {result}")"""

# email ve parola bilgileri ile giriş kontrolü yapınız

"""database = 'ahmet@email.com', '1234a'

mail = input('mail adresinizi girin : ')
password = input('parolanizi girin : ')

result = (mail.strip() == database[0]) and ( password.strip() == database[1])

print(result)"""

# kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız. 
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırırın 
# a) ortalama 50 olsa bile fina notu en az 50 olmalıdır
# b) finalden 70 aldığında ortalmanın önemi olmasın
"""
birincivize = int(input('birinci vize notunuzu girin : '))
ikincivize = int(input('ikinci vize notunuzu girin : '))
final = int(input('final notunuzu girin : '))

ortalama = (birincivize * 0.6) + (ikincivize * 0.6) + (final * 0.4)

# result = ortalama >= 50 


# a )

result = (ortalama >= 50) and (final >= 50)
#print(result)

# b)

result = (ortalama >= 50) or (final > 70)
print(result)"""


# kişinin ad, kilo ve boy bilgilerini alıp kilo endekslerini hesaplayınız
# formül: (kilo/ boy uzunluğunun karesi)
"""aşağıdaki tabloya göre kişi hangi gruba girmektedir
0-18.4 zayıf
18.4-24.9 normal
25.0-29.9 fazla kilolu
30.0-34.9 şişman"""

name = input('adınız : ')
surname = input('soyadınız : ')
weight = int(input('kilonuz : '))
height = float(input('boyunuz : '))

index = weight / height**2

result = (index <= 18.4)
 
print(true)