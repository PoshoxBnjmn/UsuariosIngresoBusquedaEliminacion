Guardado = []

Usuarios = {
    "Eduardo Acevedo":["M","34Ms42fD2"],
    "Jessica Davis":["F","49de54Ke5"],
    "Agustin Morales":["M","5DkdsuCs9"]
}

def ValidarContra(contraseña):
    contNum = 0
    contLetras = 0
    contEsp = 0
    for i in contraseña:
        if i.isnumeric():
            contNum = contNum + 1
        if i.isalpha():
            contLetras = contLetras + 1
        if i == " ":
            contEsp = contEsp + 1
    if len(contraseña) < 8:
        return False
    elif contNum < 1:
        return False
    elif contLetras < 1:
        return False
    elif contEsp > 0:
        return False
    else:
        return True
    
def ValidarNombre(nombre):
    for datos in Usuarios:
        if nombre.lower() == datos.lower():
            print("***Usuario ya existe. Intente otro***")
            return False
        elif nombre == "":
            print("***No se permiten Nombres vacios***")
            return False
        else:
            return True


def IngresoUsuario():
    sexo = ""
    validoNombre = False
    validoContra = False
    while validoNombre == False:
        nombre = input("\nIngrese el nombre del usuario: ")
        if ValidarNombre(nombre):
            validoNombre = True
    while sexo.upper() != "M" and sexo.upper() != "F":
        sexo = input("Ingrese su Sexo (M/F): ")
        if sexo.upper() != "M" and sexo.upper() != "F":
            print("***Ingrese un Sexo valido Masculino (M) o Femenino (F)***")
    while validoContra == False:
        contraseña = input("Ingrese a la contraseña del usuario: ")
        if ValidarContra(contraseña) == False:
            print("\n***Contraseña Invalida***\n")
            validoContra = False
        elif ValidarContra(contraseña) == True:
            print("Contraseña Valida!")
            Usuarios[nombre]=[sexo,contraseña]
            validoContra = True
def BuscarUsuario():
    busqueda = ""
    existe = False
    while busqueda == "":
        busqueda = input("\nIngrese el nombre del Usuario: ")
    for datos in Usuarios.items():
        nombre = datos[0]
        sexoMuestra = datos[1][0]
        contraseñaMuestra = datos [1][1]
        if busqueda.lower() == nombre.lower():
            existe = True
    if existe:
        print(f"\nEl sexo del usuario es: {sexoMuestra.upper()} y la contraseña es: {contraseñaMuestra}")
    elif not existe:
        print("\n***El usuario no se encuentra***")
def EliminarUsuario():
    busqueda = ""
    existe = False
    while busqueda == "":
        busqueda = input("\nIngrese el nombre para eliminar al turista: ")
    for datos in Usuarios:
        if busqueda.lower() == datos.lower():
            existe = True
            break
    if existe:
        del Usuarios[busqueda]
        print(f"\nTurista eliminado con exito!")
    elif not existe:
        print("\n***No se pudo eliminar usuario***")


op = 0
while op != 4:
    op = 0
    print(f"\n{"-"*15}_Menu_{"-"*15}\n1. ingresar usuario\n2. Buscar Usuario\n3. Eliminar Usuario\n4. Salir\n{"-"*36}")
    while op < 1 or op > 4:
        try:
            op = int(input("Ingrese una de las opciones (1-4): "))
            if op < 1 or op > 4:
                print("***Ingrese un opcion del 1 al 4***")
        except:
            print("***Valor Erroneo***")
    match op:
        case 1:
            IngresoUsuario()
        case 2:
            BuscarUsuario()
        case 3:
            EliminarUsuario()
print("\nPrograma terminado...\n")