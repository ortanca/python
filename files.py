# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu ("w", "a", "x", "r"))
# dosya_erişme_mody => dosyayı hangi amaçla açtığımızı belirtir.

# "w": Write, yazma modu. dosyayı konumda oluşturur. dosyanın içerisinde olan veriyi siler ve yeniden ekleme yapar.

file = open("new.txt", "w", encoding="utf-8") 
file.write('ahmet akif arslan') # açılan dosyanın içine yazdırmak için write kullanılır.
file.close() # açılan dosyayı kapatmak için close kullanılır.

# "a": Append, ekleme modu. dosya konumda yoksa oluşutrur. dosyanın içerisinde olan verinin üzerine ekleme yapar.

file = open("new.txt", "a", encoding="utf-8")
file.write('ahmet akif arslan\n') # append modunda çalıştırıldığı için eski veriyi saklar ve devamına yeni veriyi ekler.
file.close() 

# "x": create, oluşturma modu. dosya zaten varsa hata verir. 

file = open("new.txt", "x", encoding="utf-8") # eğer aynı dizinde, aynı isimde dosya varsa fileexisterror hatası verir.

# "r": read, okuma modu. varsayılan. dosya konumda yoksa hata verir.

try:
	file = open("new.txt", "r", encoding="utf-8") # eğer bir mod parametresi girilmezse varsayılan olaran read modundadır. 
												  #	dosyanın konum bilgisi tutmazsa hata verir.
except FileNotFoundError:
	print('dosya okuma hatası')
finally:
	file.close()
	print('dosya kapatıldı')


file = open("new.txt", "r", encoding="utf-8")

# for döngüsü

for i in file:
	print(i, end="") # print işlemini bitirdikten sonra bir boş satır bırakır. end=""  yöntemi ile sonuna hiç bir şey yapmamasını isteyebiliriz.
file.close()

# ************************* read fonksiyonu **************************

content1 = file.read()
print('içerik 1')
print(conten1) # read bütün içeriği okur ve dosya henüz kapanmadığı için imleç sonda kalır ve ikinci içerik boş görünür.
file = open("new.txt", "r", encoding="utf-8") # bu durumda imleç başa döner içerik 2 de ekrana yazdırılır.
content2 = file.read()
print('içerik 2')
print(content2)

content = file.read(5) # ilk beş karakteri alır. her karakter bir byte'dır.
content = file.read(3) # iilk beş karakteri okuduktan sonra kaldığı yerden ikinci bi okuma yapar ve 3 karakteri okur.
print(content)


file.close()


# *************************************************** readline fonksiyonu

content = file.readline() # herdefasında bir satır okur.
content = file.readline() # herdefasında bir satır okur.
print(content, end="")
file.close()

# ************************************* readlines fonksiyonu

liste = file.readlines() # okuduğu satırları bir dizi elemanı yani liste olarak hafızada tutar.
print(liste)

# ****************************** okuma fonksiyonlarının kullanımı *************

with file = open("new.text", "r", encoding="utf-8") as file: 
# with ile oluşturmuş olduğumuz kod bloğunun sonuna geldiğinde işlem otomatik sonlandıracak ve close() fonksiyonuna gerek kalmayacak.
	content = file.read()
	print(content)
	file.seek(10) # imlecin kaçıncı karakter/byte'dan okumaya başlaycağını söyleriz. örnekte 10. karakterden başlar.
	print(file.(tell)) # imlecin kaçıncı karakter/byte da olduğunu söyler.