print("---------- Palindromo ----------");
cadena = input("Ingresa una palabra para ver si es un palindromo: ");

cadenaAlReves = "";

for i in cadena:
    cadenaAlReves = i + cadenaAlReves;
print("la cadena al reves es: {0}".format(cadenaAlReves))

if(cadena == cadenaAlReves):
   print("{0} si es un palindromo".format(cadena));
else:
    print("{0} no es un palindromo".format(cadena));

# cadenaAlReves = cadena[:: -1];
# print("la cadena al reves es: {0}".format(cadenaAlReves));
# if (cadenaAlReves == cadena):
#     print("{0} si es un palindromo".format(cadena));
# else:
#     print("{0} no es un palindromo".format(cadena));


    

