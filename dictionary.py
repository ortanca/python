students = {
	'120' : {
		'ad' : 'ali',
		'soyad' : 'yılmaz',
		'gsm' : '530 000 00 00'
	},
	'121' : {
		'ad' : 'can',
		'soyad' : 'korkmaz',
		'gsm' : '530 111 11 11'
	},
	'122' : {
		'ad' : 'volkan',
		'soyad' : 'yükselen',
		'gsm' : '530 222 22 22'
	}
}

#1 Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

studentno = input('öğrenci numarasını giriniz : ')
studentname = input('öğrencinin adını giriniz : ')
studentlastname = input('öğrencinin soyadını giriniz : ')
studentsgsm = input('öğrenci gsm numarasını giriniz : ')
"""students[studentno] = { 
							'ad' : studentname,
							'soyad' : studentlastname,
							'gsm' : studentsgsm
							}
"""
students.update({
		studentno: {
			'ad' : studentname,
			'soyad' : studentlastname,
			'gsm' : studentsgsm
		}
	})
print(students)
#2 Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

wichstudent = input('bilgilerini istediğiniz öğrenci numarasını giriniz : ')

print(f"bilgisini istediğiniz öğrencinin adı {students[wichstudent]['ad']}, soyadı {students[wichstudent]['soyad']}'dır. ve sisteme kayıtlı gsm numarası:{students[wichstudent]['gsm']}' ")