opcP = 0
opcS = 0
totP = 0
totI = 0
totB = 0
subT = 0
selD = 0
descuento = 0
descuentoA = 0
descuentoB = 0
valido = False
bien = False
 
 
 
 
print("Bienvenid@ a El Diente de Oro")
 
 
while opcP != 3:
    opcS = 0
    bien = False
    print("1- Mostrar Tratamientos")
    print("2.-Renunciar: Limpiar cotización")
    print("3.-Salir")
    while True:
        try:
            opcP = int(input("Elección: "))
            if opcP >= 1 and opcP <= 3:
                valido == True
            break
        except:  
            print("Opción mal seleccionada")
        finally: 
 
 
         if opcP == 1:
            while bien == False:
                print("Qué tipo de cliente es ustéd?")
                print("1.-Trabajador Auxiliar")
                print("2.-Trabajador Administrativo")
                print("3.-Trabajador Docente")
                print("4.-No trabajo en Duoc")
                try:
                    selD = int(input("Elección: "))
                    if selD >= 1 and selD <= 4:
                        if selD == 1:
                            descuento = 15
                            descuentoA = 0.85
                            print("Su descuento es de 15%")
                            bien = True
                        if selD == 2:
                            descuento = 10
                            descuentoA = 0.90
                            print("Su descuento es de 10%")
                            bien = True
                        if selD == 3:
                            descuento = 5
                            descuentoA = 0.95
                            print("Su descuento es de 5%")
                            bien = True
                        if selD == 4:
                            print("Felices compras :]]]")
                            bien = True
                except:
                 print("Seleccione alguna, propiamente")
 
 
            while opcS != 4:
                                print("Tratamientos:")
                                print("-----------------")
                                print("1.- Carillas Porcelana por $250.000")
                                print("2.- Implantes Dentales por $475.000")
                                print("3.- Ortodoncia Brackets por $800.000")
                                print("4.- Volver")
                                try:
                                    opcS = int(input("Selección: "))
                                except:
                                    print("Seleccione propiamente")
                                finally:
                                        if opcS == 1:
                                            totP = totP + 250000
                                            subT = subT + 250000
                                            print("Su orden se añadió correctamente")
                                        else:
                                            if opcS == 2:
                                                totI = totI + 475000
                                                subT = subT + 475000
                                                print("Su orden se añadió correctamente")
                                            else: 
                                                if opcS == 3:
                                                    totB = totB + 800000
                                                    subT = subT + 800000
                                                    print("Su orden se añadió correctamente")
                                                else:
                                                    if opcP == 2:
                                                        subT = subT - subT
                                                        totP = totP - totP
                                                        totI = totI - totI
                                                        totB = totB - totB
                                                        print("Cotización limpiada correctamente")
total = subT * descuentoA
#Ayuda no me acuerdo de cómo hacer el descuento aaaaaaa
descuentoB = subT * descuentoA
descuentoC = subT - descuentoB
print("-----------------------------------------")
print("                Cotización               ")
print("-----------------------------------------")
if totP > 0:
    print("--> Tratamiento(s) Carilla Porcelana\t$", totP)
if totI > 0:
        print("--> Tratamiento(s) Implantes Dentales\t$", totI)
if totB > 0: 
            print("--> Tratamiento(s) Ortodoncia Brackets\t$", totB)
print("-----------------------------------------")
print("Subtotal\t$", subT)
if descuento != 0:
    print("Descuento", descuento, "%\t$", descuentoC)
    print("-----------------------------------------")
    print("Total\t$", total)
    print("-----------------------------------------")
    print(f"Son 12 cuotas de:\t$", round(total/12), "\n")
    print("Sonria bonito!!")
else:
    print("-----------------------------------------")
    print(f"Total\t$", round(total))
    print("-----------------------------------------")
    print(f"Son 12 cuotas de:\t$", round(total/12), "\n")
    print("Sonria bonito!!")
 