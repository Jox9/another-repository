def saludar() -> None:
    name = input("Escriba su nombre: ")
    msj = f"Hola {name}, tenga un buen dia.  "
    print(msj)

def ask_plant() -> None:
    msj = "Me gustan las plantas."
    print(msj)
    favorite = input("Cual es tu planta favorito ? ")
    msj = f"El {favorite} !!. Es un bonita planta"
    print(msj)

def ask_plant_name()-> None:
    name = input("Cual es su nombre? ")
    msj = f"""{name}?, que lindo nombre.
    Suena a que nos vamos a llevar bien.""" 
    print(msj)
    
saludar()
ask_plant()
ask_plant_name()