#Definir el encabezado de la funcion
""""" La funcion se llama areaRectangulo, 
recibe como datos el Largo y el Ancho
y retorna el area del rectangulo"""

def areaRectangulo(lado1, lado2):
    sup=lado1*lado2
    return sup
######Seccion principal######
largo=float(input("Largo de la caja:"))
ancho=float(input("Ancho de la caja:"))
altura=float(input("Altura de la caja:"))
#Invocamos a la funcion areaRectangulo
s1=areaRectangulo(largo, altura)
s3=areaRectangulo(ancho, altura)
s5=areaRectangulo(largo,ancho)
supTotal=2*s1+2*s3+2*s5
print("La suma de superficies es:",supTotal)
#obtener el volumen
volumen=areaRectangulo(largo,areaRectangulo(ancho,altura))
print("El volumen es:",volumen)