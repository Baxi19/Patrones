import cv2
import numpy as numpy
from matplotlib import pyplot as plt
from PIL import Image
from skimage.util import random_noise
from imgaug import augmenters as iaa


def method1():
    print("Uno")

def method2():
    print("Dos")

def resize_image(image_name, x,y):
    img = cv2.imread(image_name)
    res = cv2.resize(img, (x, y))
    return res

def method4():
    print("Cuatro")

def method5():
    print("Cinco")

def method6():
    print("Seis")


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
    print("\n7) Salir")

    opcion = input("selecione una opcion: ")

    if opcion == "1" :
        method1()
        main()

    elif opcion == "2" :
        method2()
        main()

    elif opcion == "3" :
        x = int(input("Digite la altura : "))
        y = int(input("Digite el ancho : "))
        img = resize_image("image1.jpg",x, y)
        cv2.imshow("Resized" + " ("+ str(x) +", " + str(y) +")", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        main()

    elif opcion == "4" :
        method4()
        main()

    elif opcion == "5" :
        method5()
        main()

    elif opcion == "6" :
        method6()
        main()

    elif opcion == "7" :
        print("\n Gracias por utilizar el programa!!")


    else:
        main()


if __name__ == '__main__':
    main()
