#EJERCICIO 1  Escribir un programa que muestre por pantalla la frase ¡Hola mundo!
print("hola mundo")

#EJERCICIO 2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable
MENSAJE= "HOLA MUNDO"
print(MENSAJE)

#EJERCICIO 3 
print("¿Cuál es tu Nombre?")
Nombre= input()
print("Mucho gusto," + Nombre)

#EJERCICIO 4 Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  (3+22⋅5)2
print(((3+2)/(2*5))**2)

#EJERCICIO 5 Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
print("horas de trabajo:")
Horas=float(input())
print("¿Costo por horas de trabajo?")
Costo=float(input())
Paga=Horas*Costo
print("tu paga es:" + str(Paga))   

#EJERCICIO 6 Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma: n(n+1)2
print("Introducir numero entero")
n=int(input())
suma=n(n+1)/2 
print("la suma de los primeros números enteros desde 1 hasta" + str(n) + "es" + str(suma))

#EJERCICIO 7 Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
print("peso en kg:")
Peso=input()
print("estatura en:")
Estatura=input()
imc= Peso/(Estatura**2)
print("tu masa corporal es" + str(imc))  #  PUEDO COLOCARLO ASI O ES OBLIGATORIO QUE SEA: + str(imc)


#EJERCICIO 8 Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
print("dividendo entero:")
a= input()
print("divisor entero:")
b= input()


#EJERCICIO 1 Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
print("¿cual es tu nombre?")
Nombre= input()
print("numero entero")
x=input()
print(Nombre)*x

#EJERCICIO 2 Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera

print("nombre completo")
w=input()
print(w.lower())
print(w.upper())
print(w.title())

#EJERCICIO 3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
print("nombre")
h=input()
print(h.upper() + "tiene" + str(len(h)) + "letras")

#EJERCICIO 4 Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de teléfono sin el prefijo y la extensión
print("numero tlf formato: +58-xxxxxxx-00")
num_tlf=input()
print("El número de teléfono es" + str(num_tlf[4,-3]))


#EJERCICIO 4 Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
email = input("Introduce tu correo electrónico: ") # mirna@gmail.com -> mirna + @ceu.es
print(email[:email.find('@')] + '@ceu.es') #! NO LO HICE !

#EJERCICIO 9 Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año
print("dia",fecha[:2])
print("mes",fecha[3:5])
print("año",fecha[6:])  

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)  #NO ENTENDI

#EJERCICIO 10 Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta
prodcutos_de_cesta=input("productos de una cesta separar con comas:")
print(prodcutos_de_cesta.replace(",","/n"))



#EJERCICIO 11 Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el siguiente formato: <producto>: <unidades> unidades x <precio>€ = <total>€ donde <unidades> es el número de unidades con cinco dígitos, <precio> es el precio unitario con 6 dígitos enteros y 2 decimales y <total> es el coste total con 8 dígitos enteros y 2 decimales.

product=input("nombre del producto:")
precio=float(input("ingresar precio:"))
unidades=int(input("numero de unidades:"))
product:unidades*precio #TODAVIA NO 


#EJERCICIO 1 Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad:input("Cual es tu edad?:")
if edad < 18:
    print("eres menor de edad")
else:
print("eres mayor de edad")

#EJERCICIO 2 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

c="contraseña"
contraseña=input("introduce contraseña")
if c == contraseña.lower():
    print("coincide")
else:
    print("no conincide")


#EJERCICIO 3 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar
num=int(input("introduce numero entero"))
if num/2 == 0
    print("el nmr" + str(num) + "es par")
else:
    print("el nmr" + str(num) + "es impar")








