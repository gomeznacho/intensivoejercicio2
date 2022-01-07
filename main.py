agenda = {}
def añadirContacto(agenda):

    contacto = input("Introduce datos de contacto: ")
    if  not contacto.__contains__(","):
        print("formato erróneo, separa el nombre y el número por una coma")

    else:
        list = contacto.split(",")
        nombre = list[0]
        numero = list[1]
        if list[1] in agenda.values():
            print("telefono ya registrado")

        else:
            agenda[nombre] = numero
            print(agenda)

def buscarPorTelefono():

    numero = input("¿qué teléfono quieres buscar")

    for nombre, telefono in agenda.items():
        if numero == telefono:
            return nombre + telefono

    return "no existe ese número"


def buscarPorNombre():

    busqueda = []
    contacto = input("¿qué nombre quieres buscar")

    for nombre, telefono in agenda.items():
        if nombre.startswith(contacto):
            busqueda.append(nombre + telefono)

    return busqueda

añadirContacto(agenda)
añadirContacto(agenda)

print(buscarPorTelefono())
print(buscarPorNombre())