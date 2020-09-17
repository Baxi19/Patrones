import cv2
from PIL import Image


def get_rgb(x, y):
    image = cv2.imread("image1.jpg")
    (B, G, R) = image[x, y]
    print("R={}, G={}, B={}".format(R, G, B))
    cv2.imshow("Get RGB(X , Y)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def prepare_data():
    x1 = int(input("Digite un valor de inicio 1: "))
    y1 = int(input("Digite un valor de fin 1 : "))
    x2 = int(input("Digite un valor de inicio 2: "))
    y2 = int(input("Digite un valor de fin 2: "))
    if x1 < x2 and y1 < y2:
        method2(x1, y1, x2, y2)
    else:
        print("\t\n Error, el inicio debe de ser mas pequeno que e fin..!\n")
        prepare_data()

def method2(x1, y1, x2, y2):
    image = cv2.imread("image1.jpg")
    roi = image[x1:y1, x2:y2]
    cv2.imshow("Original ", image)
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize_image(image_name, x,y):
    img = cv2.imread(image_name)
    res = cv2.resize(img, (x, y))
    return res

def method4():
    image = cv2.imread("image1.jpg")
    resized = cv2.resize(image, (200, 200))
    cv2.imshow("Fixed Resizing", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def method5():
    print("Cinco")

def method6():
    print("Seis")


def main():
    print("********************")
    print("*                      MENU                            *")
    print("********************")
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

    if opcion == "1":
        aux_img = cv2.imread("image1.jpg")
        (h, w, d) = aux_img.shape

        x = int(input("Digite un valor de X : "))
        y = int(input("Digite un valor de Y : "))

        if x > h or y > w:
            print("El punto que se desea conocer excede los límites de la imagen:\n"+
                  "\tAltura de imagen: " + str(h) + "\n"+
                  "\tAnchura de imagen: " + str(w))
        else:
            get_rgb(x, y)
        main()

    elif opcion == "2":
        prepare_data()
        main()

    elif opcion == "3":
        x = int(input("Digite la altura : "))
        y = int(input("Digite el ancho : "))
        img = resize_image("image1.jpg",x, y)
        cv2.imshow("Resized" + " ("+ str(x) +", " + str(y) +")", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        main()

    elif opcion == "4":
        method4()
        main()

    elif opcion == "5":
        method5()
        main()

    elif opcion == "6":
        method6()
        main()

    elif opcion == "7":
        print("\n Gracias por utilizar el programa!!")


    else:
        main()

if __name__ == '__main__':
    main()
