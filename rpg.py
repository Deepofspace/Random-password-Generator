import random


def harf():
    harfler = chr(random.randint(65, 90))
    for i in harfler:
        return i


def sayi():
    sayilar = chr(random.randint(48, 57))
    for j in sayilar:
        return j


harf1 = harf()
harf2 = sayi()
harf3 = harf()
harf4 = sayi()
harf5 = harf()
harf6 = sayi()

sifre = harf1+harf2+harf3+harf4+harf5+harf6

print(sifre)
