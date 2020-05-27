#1 "Bmw, Mercedes , Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ['Bmw', 'Mercedes','Opel','Mazda']
print(cars)

#2 Liste Kaç elemanlıdır

print(len(cars))

#3  Listenin ilk ve son elemanı nedir?
print(f"listenin ilk elemanı {cars[0]} ve listenin son elemanı {cars[-1]}'dır ")

#4 mazda değerini toyota ile değiştirin.

cars[-1] = 'Toyota'
print(cars)

#5  listenin Mercedes bir elemanı mıdır?

isfound = 'mercedes' in cars
print(isfound)


#6 Listenin -2 indeksindeki değer nedir

print(cars[-2])

#7 listenin ilk üç elemanını alın 

print(cars[0:3])
#del cars[-1]
#print(cars)

#8 Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

cars[-2], cars[-1] = "Toyota", "Renault"
print(cars)

#9 Listenin üzerine "Audi" ve "Nissan" değerleri ekleyin

result = cars + ['Audi', 'Nissan']
print(result)
cars.extend(['Audi', 'Nissan'])
print(cars)

#10 Listenin SOn elemanını silin 

del cars[-1]
print(cars)

 #11 Liste elemanlarını tersten yazdırınız.

print(cars[::-2])

#12 Aşağıdaki verileri bir liste içinde saklayınız

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [90,90,90]]

students = [studentA, studentB[2], studentC[-1][2]]

print(f"{studentA[0]} {studentA[1]} {2019- studentA[2]} yaşındadır ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}'dır.")

