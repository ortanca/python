#yöntem 1
"""
import math


value = dir(math)
value = help(math.factorial)


value = math.sqrt(49) # karekök alır
value = math.factorial(5)
value = math.floor(5.9)
value = math.ceil(5.9)
"""
"""

import math as islem / isim verip o isim üzerinden çağırabiliyoruz.

value = islem.ceil(5.9) #sayyıyı büyüğe yuvarlar
value = islem.floor(5.9) #sayıyı küçüğe yuvarlar
print(value)

"""
#yöntem 2

from math import * # factorial, sqrt, floor.... kullanmak istediğim methodları import ediyoruz.

value = factorial(5)
value = sqrt(49)
