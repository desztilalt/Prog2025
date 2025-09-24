import random

szamok=[]

#100 elemu lista feltoltése 1-99 kozotti veletlenszamokkal

for i in range(100):
    #szam generalas

    rszam=random.randint(1,100)

    #szam elhelyezese a listaban

    szamok.append(rszam)

#ellenorzes
'''print(szamok)'''

#kitalalando szam beallitasa
kitalalando_szam=random.randint(0,len(szamok))

tipp=input("Kérek egy egész számot [1-100]: ")

while(not tipp.isdecimal()):
    print("Egész számmal játsz!")
    tipp=input("Kérek egy egész számot [1-100]: ")

tipp=int(tipp)
    
if (tipp<kitalalando_szam):
    print("A kitalálandó szám nagyobb.")
elif (tipp>kitalalando_szam):
    print("A kitalálandó szám kisebb.")

while (tipp!=kitalalando_szam):
    tipp=input("Kérek egy egész számot [1-100]: ")
    
    while(not tipp.isdecimal()):
        print("Egész számmal játsz!")
        tipp=input("Kérek egy egész számot [1-100]: ")

    tipp=int(tipp)
    
    if (tipp<kitalalando_szam):
            print("A kitalálandó szám nagyobb.")
    elif (tipp>kitalalando_szam):
            print("A kitalálandó szám kisebb.")
        
print("Gratulálok, eltaláltad a számot!")