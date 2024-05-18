# Ciclo For: funciona dentro de un intervalo de datos cerrado, con
# inicio y fin definidos
lista_nombres = ["Bea", "Gabriel", "Mirnita", "Yannet", "Cruz"]
for nombre in lista_nombres:
    print("Hola", nombre)
# Imprimir numeros de 1 a 1000
for number in range(1, 1001):
    print(number)
# Ciclos While: este ciclo depende de una condicion

nivel_tanque = 5

while nivel_tanque < 10:
    print("Llenando tanque", nivel_tanque)
    nivel_tanque = nivel_tanque + 0.5
# Interrupciones de ciclo
print("Interrupciones break y continue")
# Break: salir del ciclo
print("Interrupciones break con for")
for name in lista_nombres:
    if name == "Gabriel":
        break
    print("Hola", name)
print("Interrupciones continue con for")
for name in lista_nombres:
    if name == "Gabriel":
        continue
    print("Hola", name)
# Continue: brincar
print("Interrupciones break while")
nivel_tanque_2 = 5
while nivel_tanque_2 < 10:
    if nivel_tanque_2 >= 9.0:
        break
    print("Llenando tanque", nivel_tanque_2)
    nivel_tanque_2 = nivel_tanque_2 + 0.5

print("Interrupciones continue while")
while nivel_tanque_2 > 0:
    nivel_tanque_2 = nivel_tanque_2 - 0.5
    if nivel_tanque_2 <= 1:
        continue
    print("Llenando tanque", nivel_tanque_2)
