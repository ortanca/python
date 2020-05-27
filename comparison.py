#girilen sayıdan hangisi büyüktür
"""print('bilgi dede sorar;')
a = int(input('bir sayı söyle evlat : '))
b = int(input('dur kaçma bir sayı daha söyle evlat : '))
result = a > b
print(result)"""

# kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalam hesaplayınız. eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

"""a = int(input('1. vize notu: '))
b = int(input('2. vize notu: '))
c = int(input('final notu: '))

a = a * 0.6
b = b * 0.6
c = c * 0.4

ortalama = a + b+ c
result = (ortalama >= 50)

print(result)"""

#girilen bir sayının tek mi çift mi olduğunu yazdırın 

""""sayi = int(input('sayi : '))

tek_cift =( sayi% 2 ==*)

print(f'girilen sayının çift olma durumu: {tek_cift}')"""

#girilen bir sayının negatif mi poozitif mi olma durumunu yazdırın 

"""print('bilge dede sorar;')

sayi = int(input('bir sayi söyle evlat: '))
result = (sayi >= 0)
print('bilge dede duurur mu yapıştırmış cevabı.')
print(f"girdiğin sayının poizitif olma durumu : {result}")"""

# parola ve email bilgisini isteyip doğruluğunu kontrol ediniz



mail = input('mail adresinizi girin : ')
password = input('parolanizi girin : ')

database = 'email@ahmet.com', '1234'

isit = mail.lower().strip() == database[0]
isit2 = password.strip() == database[1]

print(f"mail adresinizin doğruluk durumu : {isit} ve parolanizin dogruluk durumu {isit2}")


