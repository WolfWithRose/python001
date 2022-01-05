lista = []
with open("input.txt", "r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))

print("1. Írjuk ki a sorozatban található 17-tel és -17-tel osztható számok harmadát!")
for elem in lista:
    if elem % 17 == 0 or elem % -17 == 0:
        print(elem/3)
print("3. Írjuk ki az első 3-mal vagy 5-tel osztható szám indexét!")
db = 0
for elem in lista:
    if elem % 3 == 0 or elem % 5 == 0:
        print(db)
        break
    else:
        db+=1
print("5. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja nulla?")
nullaszomszed = False
for i in range(len(lista)):
    if i == 0:
        if lista[i+1] == 0:
            nullaszomszed = True
            break
    elif i == len(lista) - 1:
        if lista[i-1] == 0:
            nullaszomszed = True
            break
    else:
        if lista[i+1] == 0 and lista[i-1] == 0:
            nullaszomszed = True
            break
if nullaszomszed == True:
    print("Van")
else:
    print("Nincs")
print(f"7. Hány eleme van a sorozatnak? {len(lista)}")
print("9. Van-e a sorozatban köbszám?")
"""
kobszam = False
for elem in lista:
    if elem**(float(1/3))%1==0:
        kobszam = True
        break
if kobszam == True:
    print("Van")
else:
    print("Nincs")
"""