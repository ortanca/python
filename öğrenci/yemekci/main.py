print('bu gün ne pişirsem derdine son!')
print('sakin olun ve hemen elinizdeki malzemeleri bize söyleyin.')
while True:	
	act = input('1- Yemek tarifi eklemek istiyorum\n2- Yemek tarifi almak istiyorum.\n')

	if act == '1':
		yemekAdi = input('eklemek istediğiniz yemeğe bir isim verin :')
		print("tüm malzemeleri eklediğinizden eminseniz yemek tarifini girmek için 'bu kadar' yazabilirsiniz.")
		while True:
			malzeme = input('ekmelek istediğiniz malzemeyi giriniz: ')
			if malzeme == 'bu kadar':
				break
						
	elif act == '2':
		pass
	elif act == 'hadi çıkar beni buradan':
		break
	else:
		print("Yanlış bir komut verdiniz.\nÇıkmak istiyorsanız 'hadi çıkar beni buradan' yazarak proramı sonlandırabilirsiniz")
	