# Funciones:
# Funcion de la recta => f(x) = m*x+ b
# Reproducir la funcion de la recta
from math import ceil, floor


def ecuacion_de_la_recta(x):
    return 2 * x + 6


# y
# |
# |_________
# |__________x
def ecuacion_constante():
    return 5


# | x | f(x) |
# | 0 | f(0)=6 |
# | 2 | f(2)=10 |
# | 4 | f(4)=14 |
# | 6 | f(6)=18 |

f0 = ecuacion_de_la_recta(0)
f2 = ecuacion_de_la_recta(2)
f4 = ecuacion_de_la_recta(4)
f6 = ecuacion_de_la_recta(6)
print(f0, f2, f4, f6)
# Funciones que posee python por defecto
print(56)
# Otras funciones
print("sum", sum([1, 15, 12, 15]))
print("abs", abs(-15))
print("len", len([-15, 15, 62]))
print("round", round(9.8))
print("ceil", ceil(1.1))
print("floor", floor(9.9))
# ------------------------------------ #
print("Funcion de llenado de tanque")


def llenado_tanque(nivel_de_tanque):
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


niveles = range(0, 11)
for nivel in niveles:
    print("nivel: ", nivel)
    llenado_tanque(nivel)
