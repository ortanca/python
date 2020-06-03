#bankamatik uygulaması


accounts = {
	'12345' : {
		'ad' : 'ahmet arslan',
		'bakiye' : 3000,
		'ekhesap' : 2000
	},
	'54321':{
		'ad' : 'yasin arslan',
		'bakiye' : 8000,
		'ekhesap' : 1000
	}
}




hesapno = input('hesap numaranızı giriniz: ').strip()
isfound = str(hesapno) in accounts
bakiye = accounts[hesapno]['bakiye']
ekhesap =  accounts[hesapno]['ekhesap']
def paracek(x):
	if x < bakiye:
		print('işleminiz başarıyla gerçekleştirilmiştir.')
		kalan = bakiye- x
		print(f"kalan bakiyeniz {kalan}TL'dir.")

	elif x > bakiye:
		print('bakiye yetersiz.')
		onay = input('ek hesabı kullanmak ister misiniz? (evet/hayır): ')
		if onay == 'e':
			ekstra = int(input(f"ek hesabınızda {ekhesap}TL bulunmaktadır. lütfen çekmek istediğiniz tutarı yazın."))		
			x += ekstra
			kalan = ekhesap-ekstra 
			print(f"{x}TL hesabınızdan çekilmiştir. ek hesabınızda {kalan}TL kalmıştır.")
		else :
			print('iyi günler dileriz.')
if isfound:
	print('giriş başarılı.')
	print('para çekmek için 1')
	print('bakiye sorgulamak için 2')
	print('hesap bilgilerini görmek için 3')
	islem = int(input('hangi işlemi yapmak istiyorsunuz: '))
	if islem == 1:
		miktar = int(input('çekmek istediğiniz miktarı giriniz: '))
		paracek(miktar)
	elif islem == 2:
		print(f"{hesapno}'lu hesabınızın bakiyesi: {accounts[hesapno]['bakiye']}TL'dir.")
	elif islem == 3:
		print(f"{hesapno}'lu hesabınıza kayıtlı ad/soyad bilgisi: {accounts[hesapno]['ad']},\nbakiyesi : {accounts[hesapno]['bakiye']}TL'dir, \nek hesap limitiniz : {accounts[hesapno]['ekhesap']}TL'dir.")
	else:
		print('yanlış bir giriş yaptınız.')
else:
	print('lütfen girilen hesap numarasını kontrol ediniz.')





