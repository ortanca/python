name = input('adınız:')
surname = input('soy adınız:')
day = input('ayın kaçıncı günü doğdunuz:')
month = input('kaçıncı ayda doğdunuz:')
year = input('peki kaç yılında doğdunuz:')
today = 6
thismonth = 5
thisyear = 2020
age = str(thisyear-int(year)) 

print('adınız {} ve soyadınız {}. yaşınız {}'.format(name, surname, age ))
print(f'adınız {name} ve soyadınız {surname}. yaşınız {age}'.format(name, surname, age ))