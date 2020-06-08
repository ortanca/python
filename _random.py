import random

result = dir(random)
result = help(random)

print(result)


result = random.random() #0.0 ile 1.0 arasında rastgele bir sayı üretir
result = random.random() * 100 
result = int(random.uniform(1,10)) # 1 ve 10 arasında rastgele bir sayı üretir ancak sayı float(küsüratlı) olacaktır.
result = random.randint(1,100) # ondalıksız iki sayı arasında random sayılar üretir

greeting = 'hello there'
names = ['ahmet', 'burak', 'yasin', 'asiye']
result = names[random.randint(0, len(names)-1)]

result = random.choice(names) # liste elemanlarından rastgele bir rakamı karşımıza geitrir
result = random.choice(greeting)

liste = list(range(10)) 
random.shuffle(liste) # liste elemanlarını karıştırır.
result = liste


liste = range(100)
result = random.sample(liste, 3) #listenin içinden rastgele üç eleman getir.
print(result)