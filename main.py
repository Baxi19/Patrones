
def method1():
    print()

def method2():
    print()

def method3():
    print()

def method4():
    print()

def method5():
    print()

def method6():
    print()


def main():
    print("********************************************************")
    print("*                      MENU                            *")
    print("********************************************************")
    print("")
    print("\n1) Despliegue el R,G,B de un pixel para un x,y proporcionado por el usuario")
    print("\n2) Extraer una región de una imagen una region (ROI) se deben solicitar los dos pares (x,y)\n"
          " inicio y fin y desplegar la imagen recortada. Muestre primero la imagen original")
    print("\n3) Permita ajustar el tamaño de una imagen solicitando nueva dimensión en pixles y muestrela imagen resultante")
    print("\n4) Redimencione una imagen pero sin alterar el aspecto")
    print("\n5) Rote una imagen la cantidad de grados que el usuario requiera")
    print("\n6) Suavizar una imagen mediante un blur con un kernel Gaussiano")
    print("\n\nSelecione una opcion: ")

    opcion = input("selecione una opcion: ")

    if opcion == "1" :
        method1()
    elif opcion == "2" :
        method2()
    elif opcion == "3" :
        method3()
    elif opcion == "4" :
        method4()
    elif opcion == "5" :
        method5()
    elif opcion == "6" :
        method6()
    else:
        main()


if __name__ == '__main__':
    main()
