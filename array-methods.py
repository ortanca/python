names = ['ali', 'yağmur', 'hakan', 'deniz']
years = [1998, 2000, 1998, 1987]

#1 cenk ismini listenin sonuna eklyeniz.

names.append('cenk')
print(names)

# sena değerini listenin başına ekleyiniz.

names.insert(0, 'sena')
names.insert(len(names), 'mehmet')
print(names)

# deniz ismini listeden siliniz

names.remove('deniz')
"""names.pop(index numarası)"""
print(names)

#deniz isminin indexi nedir?
names.insert(-1,'deniz')

print(names.index('deniz'))

# ali listenin bir elemanı mıdır

isfound = 'ali' in names
print(isfound)

# liste elemanlarını ters çeviririn

names.reverse()
print(names)

# years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
print(years)

# str= 'chevrolet dacia' karakter dizisini listeye çeviriniz

text = 'chevrolet dacia' 
newarray = text.split()
print(newarray)

# years dizisinin en büyük elamanı ve en küçük elemanı nedir

print(f'years dizisinin en büyük eleman{max(years)} ve en küçük eleman {min(years)}dir')

#years dizisinde kaç tane 1998 değeri vardır

result= years.count(1998)
print(result)

#years dizisinin tüm elemanlarını siliniz

years.clear()
print(years)

# kullanıcıdan alacağınız üç tane marka bilgisini listede saklayınız
"""
firstdata = input('birinci markayı giriniz : ')
seconddata = input('ikinci markayı giriniz : ')
thirddata= input('üçüncü markayı giriniz : ')

liste = [str(firstdata), str(seconddata), str(thirddata)]
print(liste)"""

markalar=[]

marka = input('marka : ')
markalar.append(marka)

marka = input('marka : ')
markalar.append(marka)

marka = input('marka : ')
markalar.append(marka)

print(markalar)