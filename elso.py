import random

szamok=[]

#100 elemu lista feltoltése 1-99 kozotti veletlenszamokkal

for i in range(100):
    #szam generalas

    rszam=random.randint(1,100)

    #szam elhelyezese a listaban

    szamok.append(rszam)

#ellenorzes
print(szamok)


#egyszamjatek
jatek_szam=0
nem_talaltDB=0

#kitalalando szam beallitasa
kitalalando_szam=