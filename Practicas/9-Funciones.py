def nombreFuncion():
    print("hola mundo");

nombreFuncion();


def funcionConParametros(argumento1, argumento2):
    print(argumento1,argumento2);

funcionConParametros("adios", "mundo");
funcionConParametros("hola", 5);


def argumentosInfinitos(*args):
    print("El argumento 3 es:",args[2])

argumentosInfinitos(1,4,"Adios",40.0)


def numAlCuadrado(numero:int):
    print(numero*numero);

numAlCuadrado(3);


def simpleOperacion(num:int = 0):
    print(num);
    return num//5;

x = simpleOperacion(10);
print(x);
x = simpleOperacion(25);
print(x);
x = simpleOperacion()
print(x);

