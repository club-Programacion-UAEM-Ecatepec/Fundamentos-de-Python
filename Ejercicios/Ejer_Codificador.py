# Ejercicio 3: Codificador/Decodificador
#
# Crea un programa que codifique un texto ingresado para que suelte
# un codigo secreto que puedas guardar y despues reingresar ese mismo codigo
#  para descodificar el codigo y desifrar el texto
# 
# Consejo: utiliza los diccionarios para cambiar los caracteres del texto ingresado
#
#####################################################################################################
#
# Mas abajo esta el ejercicio, trata de hacerlo solo, si no puedes echa un 
# vistazo a la solucion que se muestra mas abajo
#
######################################################################################################
#









codigo = {"a":"7",
        "b":"q",
        "c":"w",
        "d":"e",
        "e":"r",
        "f":"t",
        "g":"y",
        "h":"u",
        "i":"i",
        "j":"o",
        "k":"p",
        "l":"a",
        "n":"s",
        "m":"d",
        "ñ":"f",
        "o":"g",
        "p":"h",
        "q":"j",
        "r":"k",
        "s":"l",
        "t":"ñ",
        "u":"z",
        "v":"x",
        "w":"c",
        "x":"v",
        "y":"b",
        "z":"n",
        " ":"m",
        ",":"+",
        ".":"}",
        "1":"´",
        "2":"{",
        "3":".",
        "4":"_",
        "5":"-",
        "6":"8",
        "7":"1",
        "8":"9",
        "9":"4",
        "0":"*"
}

while(True):
    print("--- CODIFICADOR / DECODIFICADOR ---");
    opc = input("""

        [c]odificar
        [d]ecodificar
        [s]alir

    """);

    if(opc.lower() == "c"):
        texto = input("Ingresa el texto a codificar: \n");
        
        textoRes = "";
        for c in texto:
            textoRes += codigo.get(c,"?");
        
    elif(opc.lower() == "d"):
        texto = input("Ingresa el texto a decodificar: \n");

        textoRes = "";
        for c in texto:
            for k, v in codigo.items():
                
                if(v == c):
                    textoRes += k
    else:
        exit();
    
    

    print("Texto codificado: \n" + textoRes + "\n");


