'''
with open("new.txt", "r+", encoding="utf-8") as file:
	file.seek(20)
	print(file.write('deneme'))

with open("new.txt", "r+", encoding="utf-8") as file:
	print(file.read())


with open("new.txt", "a", encoding="utf-8") as file:
	file.write("\nahmet")

with open("new.txt", "r", encoding="utf-8") as file:
	print(file.read())
'''

# ****************** sayfa başında güncelleme ******************

'''
with open("new.txt", "r+", encoding="utf-8") as file:
	content = file.read()
	content = "yasin\n" + content
	file.seek(0)
	file.write(content)
with open("new.txt", "r", encoding="utf-8") as file:
	print(file.read())
'''

# ******************* sayfa ortasında güncelleme *****************

with open("new.txt", "r+", encoding="utf-8") as file:
	liste = file.readlines()
	liste.insert(1, "abdullah\n")
	
	file.seek(0)
	'''
	for i in liste:
		file.write(i)
	'''
	file.writelines('yılmaz aygün')
with open("new.txt", "r", encoding="utf-8") as file:
	print(file.read())