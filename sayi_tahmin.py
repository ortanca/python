#1-100 arasında rastgele ürtilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# random modülü için python random şeklinde arama yapın
# 100 üzerinden puanlama yapın. her soru 20 puan
# hak bilgisini kuulanıcdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

import random

hotlist= list(range(1,100,1))

print('merhabalar, korkma oyunumuz çok basit.')
print('tek yapman gereken aklımdan tutacağım sayının kaçla kaç arasında olduğunu belirlemek')
print('ve tuttuğum sayıyı yine senin belirleyeceğin sayıda tahminle bulmaya çalışmak.')
print('iyi eğlenceler!')
a = int(input('başlangıç sayısını seçin : '))
b = int(input('bitiş sayısını seçin : '))
sayi = random.randint(a,b)
hak = int(input('kaç hakta bilebilirsin : '))
puanhesap = 100 / hak
can = hak

score = 0

while  hak > 0:
	guess = int(input('tahminleri alalım :'))
	hak -=1
	can = hak
	if guess == sayi :
		score += (can+1) * puanhesap
		hotlist.append(int(score))
		hotlist.sort()
		hotlist.reverse()
		champ = hotlist.index(score)
		print(f'bravo bildiniz. puanınız {score} ve en iyiler sıralamanız {champ}')
		break
	else :
		if guess > sayi:
			print('daha küçük bir sayı giriniz.')
		elif hak == 0:
			print(f'hakkınız bitti. puanunuz {score}')
		else :
			print('daha büyük bir sayı giriniz.')
