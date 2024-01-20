def saludar() -> None:
    name = input("Escriba su nombre: ")
    msj = f"Hola {name}, tenga un buen dia.  "
    print(msj)

def ask_animal() -> None:
    msj = "Me gustan los animales."
    print(msj)
    favorite = input("Cual es tu animal favorito ? ")
    msj = f"El {favorite} !!. Es un bonito animal"
    print(msj)
    
saludar()
ask_animal()