diccionario = {"valor1" : "hola mundo",
                2 : 20};

print(diccionario);
print(diccionario[2]);
unaString = "valor1";
print(diccionario[unaString]);

diccionario = {"Tamal": "platillo mexicano hecho de masa de maiz, salsa verde y pollo",
                "Botanear": "verbo de comer alguna golocina",
                "Escuencle": "Persona que está en el período de la niñez"};

diccionario.update({"Salsa":"Condimento proveniente de mexico hecho de chile con especias de sabor picoso "});

print(diccionario,"\n");


print(diccionario.copy())
print(diccionario.fromkeys(range(5)))
print(diccionario.get("tamal", "no encontrado"))
print(diccionario.items())
print(diccionario.keys())
print(diccionario.pop(0,"no encontrado"))
print(diccionario.popitem())
print(diccionario.setdefault("default", "no encontrado"))
print(diccionario.update({"Tamal": "platillo mexicano hecho de masa de maiz, salsa verde y pollo"}))
print(diccionario.values())
print(diccionario.clear(),"\n")
print(diccionario
