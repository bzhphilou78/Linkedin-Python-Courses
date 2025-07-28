test_nombre = 23
print("test n°1 = ",test_nombre)
liste = range(20)
liste_1 = []
for x in liste:
    if x % 2 ==0:
        liste_1.append(x)
print("test n°2 = ",liste_1)
liste_2 = [x for x in liste if x % 2 == 0] 
print("test n°3 = ",liste_2)
liste_3 = [str(x) for x in liste_2]
print("test n°3 = ",liste_3)
liste_4 = map(lambda num : num**2, liste_2)
print("test n°4 = ",liste_4)
for item in liste_4:
    print(item)
# Plutôt Compréhension que map
liste_5 = [num**2 for num in liste_2]   
print("test n°5 = ",liste_5)
nombres = range(20)
dict_for = {}
for n in nombres:
    if n%2==0:
        dict_for[n] = n**2
print("test n°6 = ",dict_for)
dict_sans_for = {i:i**2 for i in range(20) if i%2==0}
print("test n°7 = ",dict_sans_for)
