# ALCANCE SCOPE determina en qué partes del código se puede acceder a ella. En Python, existen dos tipos de variables: las globales y las locales. Las variables globales son aquellas que se definen fuera de una función y pueden ser accedidas desde cualquier parte del código

variable=6

def funcion():
    #global variable
    variable=0
    print(variable)
funcion()
print(variable)

