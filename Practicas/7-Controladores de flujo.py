edad = input("Ingresa tu edad: ");
edad = int(edad);



# Sentencias de control de flujo
# sentencia if
if(edad > 18):
    print("Eres mayor de edad, ten una cerveza");
    print("estaba rica?");
    print("quieres otra?");

# Setencia if-else
if(edad > 18 and edad < 50):
    print("Eres mayor de edad: puedes pasar");

else:
    print("no eres apto para la entrar, vete" )

# Sentencia swith/elif
if (edad > 50) :
    print("ya eres viejo");
elif (edad >= 30):
    print("eres un señor/señora");
elif (edad >= 18):
    print("Eres joven");
elif (edad >= 13):
    print ("Eres un adolecente");
else:
    print("Eres un niño");

# Sentencias de repeticion
# sentencia while
while(edad < 30):
    print ("Aun eres joven",edad);
    edad += 1;
print("Eres viejo, todo oxidado",edad);

# Sentencia do while... no existe
i = 0;
while(True):
    edad -= 1;
    print("rejuveneces 1 año");
    i+=1;
    if i>5:
        break;

print("Ya tienes",edad,"años");



    

