print("ingresa tu nombre, apellidos, año de nac y Carrera con semestre");
nombre = input("Ingresa tu nombre: ");
apellidos = input("Ingresa tus apellidos: ");
nac = input("Ingresa tu año de nacimiento: ")
carrera = input("Ingresa tu carrera: ")

nombre = nombre.capitalize();
apePat = apellidos.split(" ")[0].capitalize();
apeMat = apellidos.split(" ")[1].capitalize();
edad = 2020 - int(nac);
carrera = carrera.upper();

print(
"""
    nombre completo: {0} {1} {2}
    edad: {3}
    carrera: {4}

       ds
""".format(nombre, apePat, apeMat, edad, carrera))
