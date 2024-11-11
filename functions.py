# Se importan todas las funciones y tablas necesarias.
from databases import libros
# Se declara la variable salir con valor inicial False para así ejecutar el bucle hasta que el usuario salga.
salir = False

'''
Se declara la función ver_catalogo, donde se inicia un bucle for para recorrer
el listado de libros mostrando por pantalla su título y su autor
'''
def ver_catalogo():
    for i in libros:
         print("")
         print(f"{libros[i]["autor"]} | {libros[i]["titulo"]}")
         print("")

'''
Se declara la función consultar_disponibilidad, donde se inicia una variable
"check" con valor 0, posteriormente se inicia un bucle que recorre el diccionario
"libros", si encuentra una entrada en la que el título coincida y la disponibilidad
sea True entonces muestra que está disponible, si no está disponible entonoces devuelve
que no lo está y si no encuentra una entrada que coincida con el título del usuario añade 1
al contador, posteriormente se comprueba si este equivale al total de entradas en el
diccionario y si es así le indica al usuario que ha escrito mal el título o que este no se ha encontrado.
'''
def consultar_disponibilidad(a):
     check = 0
     for i in libros:
        if libros[i]["titulo"] == a and libros[i]["disp"] == True:
            print("\nEl libro está disponible.\n")
        elif libros[i]["titulo"] == a and libros[i]["disp"] == False:
            print("\nEl libro no está disponible.\n")
        else:
             check = check + 1

        if check == len(libros):
             print("\nLibro no encontrado, ¿lo has escrito correctamente?\n")


'''
Se declara la función reserva y se inicia un contador llamdo check, 
luego se recorre libros com un bucle for y si encuentra que el libro
solicitado está disponible, le cambia el valor a False y le indica al
usuario que se ha reservado, si encuentra el libro con el valor False
indica que no está disponible y si no lo encuentra suma 1 al contador.
Al final si el contador es igual a la longitud del diccionario le hace
saber al usuario que no se ha encontrado el libro.
'''
def reserva(a):
    check = 0
    for i in libros:
         if libros[i]["titulo"] == a:
            if libros[i]["disp"]  == True:
                 libros[i]["disp"] = False
                 print(f"\nSe ha reservado el libro {libros[i]["titulo"]}\n")
            else:
                 print(f"\nEl libro {libros[i]["titulo"]} ya está reservado.\n")
         else:
              check = check + 1
         if check == len(libros):
              print("\nLibro no encontrado, ¿lo has escrito correctamente?\n")
         


# Muestra un mensaje de ayuda
def help():
     print("\nVER - MUESTRA EL CATÁLOGO DE LIBROS\nCONSULTAR - CONSULTA LA DISPONIBILIDAD DE UN LIBRO\nRESERVA - RESERVA UN LIBRO SI ESTE ESTÁ DISPONIBLE\nSALIR - CIERRA EL PROGRAMA\nAYUDA - MUESTRA ESTE MENSAJE")


# La función muestra un menú con todas las opciones posibles y ejecuta la función asignada a la opción elegida.
def menu():
        global salir
        while salir != True:
            print("===========================================================")
            print("Opciones:                                                 |")
            print("(V) Ver catálogo de libros                                |")
            print("(C) Consultar disponibilidad de un libro                  |")
            print("(R) Reservar un libro                                     |")
            print("(S) Salir de la aplicación                                |")
            print("(H) Muestra ayuda sobre el programa                       |")
            print("===========================================================")
            user_input = input("Seleccione una opción: ")

            match user_input:
                case "V" | "v":
                      ver_catalogo() 
                case "C" | "c":
                      consultar_disponibilidad(input("¿Qué libro desea consultar?: "))
                case "R" | "r":
                      reserva(input("¿Qué libro desea reservar?: "))
                case "H" | "h":
                      help()
                case "S" | "s":
                      salir = True
                case _: print("\nOpción no válida\n")

