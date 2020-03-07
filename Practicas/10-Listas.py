listaPersonas = ["Pedro","Mary", "Luis", "Erick", "Carol"];
listaEdades = [20,31,19,27,22];

def promEdad(listaEdades):
     longitudArray = len(listaEdades);
     totalEdades = 0;

     for edad in listaEdades:
          totalEdades += edad;

     return totalEdades / longitudArray;

print("La edad promedio es de: " + str(promEdad(listaEdades)));

nombre = input("Ingresa el nombre de la persona nueva: ");
#edad = input("Ingresa la edad de la persona nueva: ");

listaPersonas.append(nombre);
# lista1.insert(0,"primer comentario")
#listaEdades.append(int(edad));
print(listaPersonas);

persEliminada = listaPersonas.pop();
print(listaPersonas,"la persona eliminada fue :", persEliminada);

print(listaPersonas,"\nEl primero en llegar fue: -",listaPersonas[0],"y el ultimo fue: -",listaPersonas[len(listaPersonas)-1] )

listaPersonas.sort()
print("Nombres ordenados",listaPersonas);
     
print("Antes de la eliminacion total:  ", listaEdades);
listaEdades.clear();
print("Despues de la elimincacion total:  ",listaEdades);