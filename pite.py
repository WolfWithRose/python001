lista = []

with open("input.txt", "r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))

"""
C#-ban ugyanez:

using (f = StreamReader("input.txt", Encoding.UTF8))
{    

}

"""



db = 0
for elem in lista:
    if elem%9==0 or elem%25==0:
        db=elem

print(f'2. Írjuk ki az utolsó 9-cel vagy 25-tel osztható szám négyzetgyökét! {db**(1/2)}')


def beleesneke(l):
    for elem in lista:
        if elem > 0 and elem < 20:
            return False
    return True

print(f'4. Igaz-e, hogy minden szám (0,20) nyilt intervallumba esik? {"igen" if beleesneke else "nem"}')

db = 0
for elem in lista:
    if elem%18==0 or elem%6==0:
        db+=1

print(f'6. Hány 18-cal vagy 6-tal osztható szám található a sorozatban? {db}')

db=lista[0]
db2=db
for elem in lista:
    if elem>db:
        db=db2
        db=elem

print(f'8. Mennyi a sorozatban található második legnagyobb szám? {db2}')
db=lista[0]
for elem in lista-1:
    
print(f'10. Mennyi a sorozatban található számok szorzatának a fele? {db}')

# nem túl pitonikus
i = 0
while i < len(lista) and not lista[i]<0:
    i+=1
print( 'van' if i<len(lista)  else 'nincs')

# C#,C++,C
# print( i<len(lista) ? 'van' : 'nincs')




print(f'3. Hány páros szám található a sorozatban?{db}')

print(len(list(filter(lambda x : x%2==0, lista))))