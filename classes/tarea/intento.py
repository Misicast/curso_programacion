numero = [50, 75, 46, 22, 80, 65, 8]
nummax = max(numero)
nummin = min(numero)
print("numero max es " + str(nummax))
print("numero min es " + str(nummin))


precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print("el max es " + str(max))
print("el min es " + str(min))
