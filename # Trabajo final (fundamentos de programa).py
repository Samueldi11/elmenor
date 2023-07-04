# Trabajo final (fundamentos de programacion imperativa)
# Samuel Díaz Monedero cod: 2357726
# Felipe Casañas Castro cod: 2357679
# codigo Parqueadero 


def menu():
    factura = 1
    parqueaderos = []
    tarifas = []
    opc = 1
    while opc > 0 and opc < 8:
        print("1. Tarifas")
        print("2. Ingresar vehículo")
        print("3. Buscar vehículo")
        print("4. Mostrar Registros")
        print("5. Salida de vehículo")
        print("6. Buscar Factura")
        print("7. Cuadre de Caja")
        print("8. Salir")
    opc = int(input)("ingrese una opcion: ")


def tarifas(tarifas):
    opc = 1
    while opc > 0 and opc < 5:
        print("1. Ingresar Tarifas")
        print("2. Mostrar Tarifas")
        print("3. Modificar Tarifas")
        print("4. Regresar al Menú principal")

    if opc == 1:
        # Ingresar Tarifas
        opc = 1
        while opc > 0 and opc < 3:
            print("1. Ingresar Tarifa de Automóvil: ")
            print("2. Ingresar Tarifa de Motocicleta: ")
            print("3. Regresar al subMenú Tarifas")
            opc = int(input("ingrese una opcion: "))
            if opc == 1:
                if tarifas[0].len == 0:
                    tarifas = []
                    tAutomovil= int(input("Ingresa el valor a cobrar por minuto para automóviles: "))
                    tarifas.append("Auto")
                    tarifas.append(tAutomovil)


        
        
        
    elif opc == 2:
        # Mostrar Tarifas
        print("valor por minuto", [[0][0]],[[1][0]])
        print("valor por minuto", [[0][1]],[[1][1]])
    
    elif opc == 3:
        #Modificar tarifas
        opc = 1
        while opc > 0 and opc < 3:
            print("1. Modificar Tarifa Automóvil: ")
            print("2. Modificar Tarifa Motocicleta: ")
            print("3. Regresar al subMenú Tarifas")
            opc = int(input("ingrese una opcion: "))
            if opc == 1:
                tarifas[0][1] = int(input("Ingrese la nueva tarifa para Automoviles: "))
                return tarifas
            elif opc == 2:
                tarifas[1][1] = int(input("Ingrese la nueva tarifa para Motocicletas: "))
                return tarifas


        


def crear(parqueaderos,factura,):
    parqueadero = []
    placa = int(input("ingrese la placa del vehiculo: "))
    horah = int(input("ingrese hora de entrada del vehiculo: "))
    tvehiculo = int(input("ingrese tipo de vehiculo"))
    parqueadero.append(factura)
    parqueadero.append(placa)
    parqueadero.append(horah)
    parqueadero.append("horas")
    parqueadero.append("minutos")
    parqueadero.append("preciomin")
    parqueadero.append("pagot")
    parqueadero.append(tvehiculo)
    parqueaderos.append(parqueadero)
    return parqueaderos




