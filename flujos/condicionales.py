# Conditionals, branches, if-else
print("Ejercicio de entrada de local")
edad_client = 18
if edad_client < 18:
    print("Fuera de aqui menol")
else:
    print("pase adelante")
# ----------------------------------------------------#
print("Ejercicio de bomba")
# |                 |
# |                 |
# |                 |
# |                 |
# |_________________|

nivel_de_tanque = 0  # hasta 10

if nivel_de_tanque >= 1 and nivel_de_tanque <= 3:
    print("prende una bomba y alarma")
elif nivel_de_tanque > 3 and nivel_de_tanque <= 6:
    print("enciende bomba y apaga alarma")
elif nivel_de_tanque > 6 and nivel_de_tanque <= 9:
    print("enciende bomba y alarma de casi lleno")
elif nivel_de_tanque == 10:
    print("Apaga bomba y enciende indicador de lleno")
elif nivel_de_tanque <= 0 or nivel_de_tanque > 10:
    print("Error en sensor, llamar mantenimiento")
