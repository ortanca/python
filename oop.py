# object orented programming (oop)

# class

class Person: #class ismi adettendir büyük harfle başlar.
	# pass #yer tutucu
	#class attributes
	adress = 'no information'
	#constructor (yapıcı method)
	def __init__(self, name, y):

		#object attributes
		self.name = name
		self.y = y

 	#instance methods
	def intro(self):
 		print('hello '+ self.name)
	# instance (object)
	def calcAge(self):
		return 2020 - self.y
#obje ismi küçük harfle başlar, değişken tanımlarken kullanılan kurallara yakındır.
p1 = Person('ahmet', 1989) 
p2 = Person('yasin', 1993)

#update 
p1.name ='hüsnü'
p1.adres = 'yes information'

p1.intro()
print(p2.calcAge())