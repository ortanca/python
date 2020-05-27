website = "http://www.sadikturan.com"
course = " Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1.soru 

howMany = len(course)
print(howMany)

#2.soru 
print(website[7:10])

#3.soru

print(website[-3:])

#4.soru

print(website[:15], website[15:])

#5.soru
print(course[::-1])

#6.soru
name, surname, age, job = 'ahmet akif', 'arslan', 30, 'yazılımcılık'

print(f'benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.')

#7.soru 

text = 'Hello world'
text = text[0:6] + 'W' + text[-4:]
text.replace(w,'W')

print(text)