from clase_PlanAhorro import PlanAhorro
from clase_menu import Menu
import csv
if __name__ == "__main__":
    lista = []
    archivo = open("planes.csv")
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        objeto = PlanAhorro(int(fila[0]), fila[1], fila[2], float(fila[3]))
        """
        cantidad = objeto.get_cantidad_licitar()
        if (int(fila[4]) != cantidad):
            objeto.set_cantidad_licitar(int(fila[4]))
        cantidad = objeto.get_cantidad_cuotas()
        if (int(fila[5]) != cantidad):
            objeto.set_cantidad_cuotas(int(fila[5]))
        """
        lista.append(objeto)
    
    archivo.close()
    
    menu1 = Menu(4)
    opciones = ["Actualizar el valor del vehículo de cada plan. ","Cuotas Menores a valor."," Mostrar el monto que se debe haber pagado para licitar el vehículo. ","Modificar la cantidad cuotas que debe tener pagas para licitar."]
    menu1.ingresaOpcion(opciones)
    menu1.muestra()
    opcion = int(input("Ingrese opcion "))
    cantidad = menu1.getCantidad() + 1
    while opcion != cantidad:
        if opcion == 1:
            for objeto in lista:
                objeto.mostrar()
                valor = int(input("Ingrese valor nuevo de vehículo "))
                objeto.set_valor(valor)
                print("Valor modificado con éxito")
        elif opcion == 2:
            valor = float(input("Ingrese valor de la cuota a comparar "))
            for objeto in lista:
                valor_cuota = objeto.importeCuota()
                if (valor_cuota < valor):
                    objeto.mostrar()
        elif opcion == 3:
            for objeto in lista:
                objeto.mostrar()
                print("Monto para licitar el vehículo: ", objeto.importeCuota() * objeto.get_cantidad_licitar())
        elif opcion == 4:
            codigo = int(input("Ingrese codigo plan "))
            bandera = False
            i = 0
            while (bandera == False) and (i < len(lista)):
                if codigo == lista[i].get_codigo():
                    bandera = True
                else: i += 1
            if i < len(lista):
                cantidad_cuotas_licitar = int(input("Se encontró el plan solicitado, Ingrese nueva cantidad de cuotas para licitar "))
                lista[i].set_cantidad_licitar(cantidad_cuotas_licitar)
            else:
                print("No se encontró vehículo solicitado ")
        else:
            print("Ingreso opción incorrecta ")
        menu1.muestra()
        opcion = int(input("Ingrese opcion "))