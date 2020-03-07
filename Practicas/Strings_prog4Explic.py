miCadena = "hola mundo";
otraCadena = """
    xD
        ;D
                    :(
"""

print(miCadena);

print(miCadena.upper());
# print(miCadena.lower());
print(miCadena.title()); # transforma a mayuscula la primera letra de cada palabra
print(miCadena.swapcase()); # intercambia mayuscula por minus y minus por mayus
print(miCadena.capitalize()); # transforma a mayuscula la primera letra
print(miCadena.replace("Hola", "bye")); # remplaza el primer str con el 2do
print(miCadena.count(' ')); # cuenta cuantas veces aparece la palabra especificada

print(miCadena.startswith('Ho')); # devuelve true si el str comienza con la palbra indicada
# print(miCadena.endswith("do"));

print(miCadena.split("o")); # crea una lista con las palabras separadas por la letra/s especificada
print(miCadena.find("un")); # encuentra la posicion de cierta frase en el str

print(len(miCadena));   # longitud del str 
print(miCadena.index('a'));

print(miCadena.isnumeric());
print(miCadena.isalpha()); # es alfanumerico (puras letras)?

print(miCadena[5]);
print(miCadena[-1]);


# imprimir en pantalla
nombre = "jesus"

print("mi nombre es " + nombre)
print("mi nombre es", nombre)
print("mi nombre es {0} y tengo {1}".format( nombre,52))
