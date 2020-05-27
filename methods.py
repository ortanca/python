website = "http://www.sadikturan.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 'Hello World' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

text = ' Hello World '
print(text.strip())

#.lstrip('w') solundaki w karakterleri siler.
#.rstrip('w') sağındaki w karakterleri siler.
#.strip('w') tüm dizideki w karakterleri arasında belirtilenleri siler.

#2 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki karakteri silin.

array = website.split('.')
text = array[1]
print(text)

#3 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

print(course.lower())

#4 'website' içinde kaç tane a karakteri vardır ? (count('a'))

print(website.count('a'))

#5 'website'  www ile başlayıp com ile bitiyor mu?

isStart = website.startswith('www')
isEnd = website.endswith('com')
print(isStart, isEnd)

#6 'website' içinde '.com' ifadesi var mı?

isFound = website.find('.com')
print(isFound)

#7 'course' içindeki karakterlerin hepsi alfabetik mi?  (isalpha, isdigit)

isalphabetic = course.isalpha()
print(isalphabetic)

# 8'Contents ' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

text = 'Contents'
print(text.center(50, '*'))

#9 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

print(course.replace(' ', '-'))

#10 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

text = 'Hello World'
print(text.replace('World', 'There'))

#11 'course' karakter dizisini boşluk karakterlerinden ayırın.

print(course.split(' '))



