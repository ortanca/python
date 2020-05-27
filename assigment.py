x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6

# kullanıcıdan aldığınız 2 sayının çarpımı ili xyz toplamının farkı nedir

"""firstnumber = input('birinci sayıyı giriniz : ')
secondnumber = input('ikinci sayıyı giriniz : ')

result = int(firstnumber) * int(secondnumber) - ( x + y + z )

print(f"girdiğiniz sayıların çarpımı ile x,y,z sayılarının toplamının farkı {result}'dır")"""


# y'nin x'e kalansız bölümünü hesaplayınız

#x,y,z toplamının modu kaçtır

total  = x + y + z

result = total%3

print(result)  

# ynin x. kuvvetini hesaplayınız

y **= x

print(y)

# x,*y, z = numbers işlemine göre z'nin küpü kaçtır

x, *y, z = numbers 
z **= 3
print(z)

# x, *y, z = numbers işlemine göre ynin değerleri toplamı kaçtır

x, *y, z = numbers 

result= y[0]+y[1]+y[2]
print(result)