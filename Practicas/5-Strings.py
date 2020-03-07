miCadena = "Hola mundo";
miCadena2= 'otra cadena';
otraCadena = """
    xD
        ;D
                    :(
"""

print(miCadena); # Hola mundo
print(miCadena2); # otra cadena
print(otraCadena); #    xD
                   #        ;D
                   #                :(


print(miCadena.upper()); # HOLA MUNDO
print(miCadena.lower()); # hola mundo
print(miCadena.title()); # Hola Mundo
print(miCadena.swapcase()); # hOLA MUNDO
print(miCadena.capitalize()); # Hola mundo
print(miCadena.replace("Hola", "bye")); # bye mundo
print(miCadena.count(' ')); # 1

print(miCadena.startswith('la')); # True
# print(miCadena.endswith("do"));

print(miCadena.split("o")); # [H, la mund]
print(miCadena.find("un"));

print(len(miCadena));
print(miCadena.index('a'));

print(miCadena.isnumeric()); # False
print(miCadena.isalpha()); # False 

print(miCadena[5]); # m
print(miCadena[-1]); # o


# imprimir en pantalla
nombre = "jesus"

print("mi nombre es " + nombre)
print("mi nombre es", nombre)
print("mi nombre es {1} y tengo {0}, {1}".format( nombre,52))
