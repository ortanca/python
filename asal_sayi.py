# girilen bir sayının asal olup olmadığını bulun.
# asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

sayi = int(input('bir sayı giriniz : '))
isAsal = True

if sayi == 1:

	print('bir sayısı bu kuralın dışındadır.')

for i in range(2, sayi):
	if sayi % i == 0 :
		isAsal = False
		break

if isAsal :
	print('sayi asaldir.')
else:
	print('sayi asal değildir.')