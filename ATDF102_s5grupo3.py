
# /////////////////////// Menu /////////////////////////////
print("====================================================")
print("Bienvenidos al menu de la mejor inmobiliaria de Chile")
print("=====================================================")
print("A continuación se mostraran las alternativas de navegación: ")
print("1. Registrar oficina")
print("2. Registrar inmueble")
print("3. Registrar visita")
print("4. Registrar contrato")
print("5. Solicitar reporte")
print("=====================================================")
opcion = int(input("Seleccione la alternativa que desea: "))
print("************************************************")

# //////////////////////// Registro Oficina /////////////////////////////////////
if opcion == 1:
    #Informacion de la oficina
    print("Registro de información de la oficina")
    print("")
    oficina = input("Introduzca el nombre de oficina: ")
    gerente_oficina = input("Introduzca el nombre del gerente de oficina: ")
    agente_venta =input("Introduzca el nombre del agente de venta: ")
    
    print("===============================================")
    print("Datos registrados: ")
    print()

    print("Oficina registrada")
    print("Oficina: ", oficina)
    print("Gerente de oficina: ", gerente_oficina)
    print("Agente de venta: ", agente_venta)

# ////////////////////// Registro Inmueble /////////////////////////
elif opcion == 2:
    
    #Información específica del inmueble
    print("Registro de información del inmueble")
    print("")
    print("Indica la opción del tipo de inmueble a registrar: ")
    print("")
    print("0: Vivienda")
    print("1: Local comercial")
    print("2: Bodega")
    print("")
    tipo_inmueble = int(input("El tipo de inmueble es: "))
    
    #Información general del inmueble
    print("")
    calle = input("Introduzca la calle del inmueble: ")
    numero = int(input("Introduzca el número del inmueble: "))
    comuna = input("Introduzca la comuna del inmueble:")

    superficie_m2 = int(input("Introduzca la superficie del inmueble (m^2): "))
    valor_tasacion = float(input("Introduzca el valor de tasación del inmueble(UF): "))

    if tipo_inmueble == 0:
        estado_vivienda = input("Indica si la vivienda es 'nueva' o 'usada': ")
        tipo_vivienda = input("Indica si la vivienda es 'casa' o 'departamento': ")
        n_habitaciones = int(input("Indica el número de habitaciones: "))
        n_baños = int(input("Indica el número de baños: "))
        n_cocinas = int(input("Indica el número de cocinas: "))
        red_gas = input("Indique si la propiedad cuenta con red de gas (Si/No): ")
        puerta_blindada = input("Indique si la propiedad cuenta con puerta blindada (Si/No): ")
        tipo_piso = input("Indique el tipo de piso de la propiedad: ")
    else:
        numero_puertas =  int(input("Indica el número de puertas de acceso: "))
        ventanas = input("Indica la presencia de ventanas (Si/No): ")
        estructura = input("Indica si el inmueble esta 'acondicionado' o es 'planta libre': ")

    #Información del propietario que ofrecerá el inmueble
    print("************************************************")
    print("Registro de información del propietario ")
    print("")
    nombre_propietario = input("Introduzca el nombre completo: ")
    rut_propietario = input("Introduzca el RUT: ")
    telefono_propietario1 = input("Introduzca el número de contacto: ")
    telefono_propietario2 = input("Opcionalmente un 2° número de contacto, sino, no escriba nada: ")
    plazo_contrato = input("Introduzca el plazo del contrato, indicando las unidades de tiempo (meses): ")
    
    print("===============================================")
    print("Datos registrados: ")
    print()

    print("Inmueble registrado")
    if tipo_inmueble == 0:
        registro_inmueble = "Vivienda"
    elif tipo_inmueble == 1:
        registro_inmueble = "Local comercial"
    else: 
        registro_inmueble = "Bodega"

    print("Tipo de inmueble: ", registro_inmueble)
    print("Calle: ", calle)
    print("Numero: ", numero)
    print("Comuna: ", comuna)
    print("Superficie m2: ", superficie_m2)
    print("Valor de tasación: ", valor_tasacion)
    
    if tipo_inmueble == 0:
        print("Estado de la vivienda: ", estado_vivienda)
        print("Tipo de vivienda: ", tipo_vivienda)
        print("Numero de habitaciones: ",n_habitaciones)
        print("Numero de baños: ",n_baños)
        print("Numero de cocinas: ",n_cocinas)
        print("Tiene red de gas: ",red_gas)
        print("Tiene puerta blindada: ",puerta_blindada)
        print("El tipo de piso es: ",tipo_piso)
    else: 
        print("Numero de puertas de acceso: ", numero_puertas)
        print("Tiene ventanas: ", ventanas)
        print("Condición: ", estructura)
        print("")
    
    print("")  
    print("Propietario registrado")
    print("Nombre del propietario: ", nombre_propietario)
    print("Rut del propietario: ", rut_propietario)
    print("Telefonos: ", telefono_propietario1, " - ", telefono_propietario2)
    print("Plazo del contrato: ", plazo_contrato)
        
   
# ////////////////////////// Registro Visita //////////////////////////////

elif opcion == 3:

    print("Registro de información de visita")
    print("")

    cliente = input("Ingrese nombre del cliente: ")
    propiedad = input("Ingrese propiedad a visitar: ")
    fecha = input("Ingrese fecha de visita: ")
    comentario = input("Ingrese comentario del cliente: ")
    
    print("===============================================")
    print("Datos registrados: ")
    print()

    print("Visita registrada")
    print("Cliente: ", cliente)
    print("Propiedad: ", propiedad)
    print("Fecha: ", fecha)
    print("Comentario: ", comentario)
    
# ///////////////////////////// Registro Contrato //////////////////////
elif opcion == 4:
    
    print("Registro de información del contrato")
    print("")


    nombre = input("Nombre del propietario: ")
    rut = input("RUT del propietario: ")
    telefono = input("Telefono del propietario: ")
    print("")

# Registro del contrato

    inmueble = input("Codigo del inmueble: ")
    tasacion = float(input("Valor de tasacion sin puntos: "))

    if tasacion <= 0:
        print("El valor debe ser mayor que cero.")
    
    else:
        monto = tasacion * 0.5 / 100
        
        print("===============================================")
        print("Datos registrados: ")
        print()
        
        print("\nContrato de exclusividad")
        print("Propietario:", nombre)
        print("Rut: ", rut)
        print("telefono: ", telefono)
        print("Codigo del inmueble:", inmueble)
        print("Monto del 0,5%:", monto)

# ///////////////////////// Solicitar reporte ////////////////////

elif opcion == 5:

    comision_gerente = 0.1
    comision_agente = 0.3
    comision_venta = 0.3

    total_ventas_casas = 300000000
    total_arriendos_casa = 100000000
    total_casa = total_ventas_casas + total_arriendos_casa
    
    total_ventas_depto = 200000000
    total_arriendos_depto = 60000000
    total_depto = total_ventas_depto + total_arriendos_depto
    
    total_ventas_bodega = 500000000
    total_arriendos_bodega = 0
    total_bodega = total_ventas_bodega + total_arriendos_bodega
    
    total_ventas_local = 0
    total_arriendos_local = 600000000
    total_local = total_ventas_local + total_arriendos_local
    
    print("Solicitud de reportabilidad")
    print("")

    print("Seleccione el reporte que desea visualizar: ")
    print("")
    
    print("1. Total de ingresos: ")
    print("2. Total de ingresos por ventas: ")
    print("3. Total de ingresos por arriendo: ")
    print("")
    opcion_reporte = int(input("Alternativa seleccionada: "))
    print("")
    
    if opcion_reporte == 1:
        ingreso = total_casa + total_depto + total_bodega + total_local
    
    elif opcion_reporte == 2:
        print("Seleccione el reporte a visualizar: ")
        print("")
        print("1. Total ventas globales")
        print("2. Total ventas casas")
        print("3. Total ventas departamentos")
        print("4. Total ventas bodegas")
        print("5. Total ventas locales comerciales")
        alternativa_reporte = int(input("Alternativa seleccionada: "))
        
        if alternativa_reporte == 1:
            ingreso = total_ventas_casas + total_ventas_depto + total_ventas_bodega + total_ventas_local
        elif alternativa_reporte == 2:
            ingreso = total_ventas_casas
        elif alternativa_reporte == 3:
            ingreso = total_ventas_depto
        elif alternativa_reporte == 4:
            ingreso = total_ventas_bodega
        elif alternativa_reporte == 5:
            ingreso = total_ventas_local
    
    elif opcion_reporte == 3:
        print("Seleccione el reporte a visualizar: ")
        print("")
        print("1. Total arriendo globales")
        print("2. Total arriendo casas")
        print("3. Total arriendo departamentos")
        print("4. Total arriendo bodegas")
        print("5. Total arriendo locales comerciales")
        alternativa_reporte = int(input("Alternativa seleccionada: "))
        
        if alternativa_reporte == 1:
            ingreso = total_arriendos_casa + total_arriendos_depto + total_arriendos_bodega + total_arriendos_local
        elif alternativa_reporte == 2:
            ingreso = total_arriendos_casa
        elif alternativa_reporte == 3:
            ingreso = total_arriendos_depto
        elif alternativa_reporte == 4:
            ingreso = total_arriendos_bodega
        elif alternativa_reporte == 5:
            ingreso = total_arriendos_local
    
    else:
        print("La opción que ha ingresado no es valida")
            
    
    ingreso_gerente = 0.1 * ingreso
    ingreso_agente = 0.3 * ingreso
    ingreso_comision = 0.3 * ingreso
    
    print("Los ingresos son: ")
    print("Ingresos totales: ", ingreso)
    print("Ingresos por comision de gerente: ", ingreso_gerente)
    print("Ïngreso por comision de agente: ", ingreso_agente)
    print("Ingreso por comision: ", ingreso_comision)

#------------------
#Proyecto 3 en construcción
#------------------
    # Variables iniciales
oficina1 = "Dirección: Estación Central \n Gerente: Carlos Pachenco \n Agente de venta: Fernando Lopez"
oficina2 = "Dirección: El bosque \n Gerente: Nicolas Andaluz \n Agente de venta: Roberto Paredes"
oficina3 = "" #Espacio vacío para nueva oficina
total_oficinas = 2

inmueble1 = "Tipo: vivienda usada (departamento) \n Dirección: Avenida Vitacura 4380,Vitacura \n Superficie: 120 m^2 \n Tasa de tasación: 540 UF\n Número de habitaciones: 4 \n Número de baños: 1 \n Número de cocinas: 1 \n Características especificas: ||"
inmueble2 = "Tipo: bodega \n Dirección: Calle Alonso de Córdova 5870,Las Condes \n Superficie: 95 m^2 \n Tasa de tasación: 1770 UF \n Número de puertas de acceso: 2 \n ¿Tiene ventanas?: si \n Estructura: acondicionado"
inmueble3 = "" #Espacio vacío para agregar nuevo inmueble
total_inmueble = 2

contrato1 = "Nombre del propietario: Sebastián Ignacio Valdés Rojas \n Rut: 14903221K \n Número de teléfono: |+56223456789|+56221454508| \n Fecha del contrato: 15 01 2026 \n Plazo del contrato: 12 meses"
contrato2 = "Nombre del propietario: Rodrigo Esteban Castillo Navarro \n Rut: 108563415 \n Número de teléfono: +56227119034| \n Fecha del contrato: 23 02 2025 \n Plazo del contrato: indefinido"
contrato3 = "" #Espacio vacío para agregar nuevo contrato del propietario
total_contratos = 2

cliente1 = "Nombre del cliente: Benjamin Nicolas Castro Rojas \n Número de oficina: 1 \n Fecha de visita: 13 02 2025 \n Comentario: ||"
cliente2 = "Nombre del cliente: Sarah Fernanda Flores Valdez \n Número de oficina: 2 \n Fecha de visita: 15 11 2025 \n Comentario: |La casa debe ser amarilla|"
cliente3 = "" #Espacio vacío para agregar nuevo cliente
total_visitas = 2

# --- Acumuladores financieros precargados (en pesos) ---
total_ventas_casas = 300000000
total_arriendos_casa = 100000000

total_ventas_depto = 200000000
total_arriendos_depto = 60000000

total_ventas_bodega = 500000000
total_arriendos_bodega = 0

total_ventas_local = 0
total_arriendos_local = 600000000

comision_gerente = 0.1
comision_agente = 0.3
comision_venta = 0.3
#--------------
#Menu principal
#--------------
while True:
    print("====================================================")
    print("Bienvenidos al menu de la mejor inmobiliaria de Chile")
    print("=====================================================")
    print("A continuación se mostraran las alternativas de navegación: ")
    print("1. Solicitar datos")
    print("2. Registrar nuevos datos")
    print("3. Solicitar reporte de venta o arriendo")
    print("0. Salir del sistema")
    print("=====================================================")
    opcion_principal = int(input("Seleccione la alternativa que desea: "))
    print("************************************************")

    #consulta de datos
    if opcion_principal == 1:

        while True:
            print("......................................................")
            print("Menu de consulta de datos:")
            print("......................................................")
            print("Escoja una de las siguientes opsiones:")
            print("1. Consultar oficinas registrados")
            print("2. Consultar inmuebles registrados")
            print("3. Consultar contratos de propietarios registrados")
            print("4. Consultar la visitas de clientes registrados")
            print("0. Volver al menú principal")

            llave_secundaria = int(input("Seleccione la opción que desea (para volver al menu ingrese '0'): "))

            if llave_secundaria == 1:
            #Consultar la oficina
                ox = 0
                while ox <= total_oficinas:
                    if ox == 1:
                        print("1:\n",oficina1)
                    elif ox == 2:
                        print("2:\n",oficina2)
                    ox = ox + 1

            elif llave_secundaria == 2:
            #Consultar inmueble
                ix = 0
                while ix <= total_inmueble:
                    if ix == 1:
                        print("1:\n",inmueble1)
                    elif ix == 2:
                        print("2:\n",inmueble2)
                    ix = ix + 1

            elif llave_secundaria == 3:
            #Consultar contrato del propietario del inmueble
                cx = 0
                while cx <= total_contratos:
                    if cx == 1:
                        print("1:\n",contrato1)
                    elif cx == 2:
                        print("2:\n",contrato2)
                    cx = cx + 1

            elif llave_secundaria == 4:
            #Consultar la visita del cliente
                vx = 0
                while vx <= total_visitas:
                    if vx == 1:
                        print("1:\n",cliente1)
                    elif vx == 2:
                        print("2:\n",cliente2)
                    vx = vx + 1

            elif llave_secundaria == 0:
            #Volver al menu principal
                break
            else:
                print("Opción de consulta no válida.")

    #registrar nuevos datos
    elif opcion_principal == 2:
        while True:
            print("......................................................")
            print("Menu para registrar datos nuevos:")
            print("......................................................")
            print("Escoja una de las siguientes opsiones:")
            print("1. Nueva oficina")
            print("2. Nuevo inmueble")
            print("3. Nuevo contrato")
            print("4. Nueva visita")
            print("0. Volver al menú principal")

            llave_secundaria = int(input("Seleccione la opción que desea (para volver al menu ingrese '0'): "))

            if llave_secundaria == 1:
                #Nueva oficina
                numero_o = 0
                while numero_o <=total_oficinas:
                    numero_o = numero_o + 1

                print("Registro de información de la oficina")
                print("")
                oficina = input("Introduzca la dirección de la sucursal de la oficina: ")
                gerente_oficina = input("Introduzca el nombre del gerente de oficina: ")
                agente_venta =input("Introduzca el nombre del agente de venta: ")
                print("===============================================")
                print("Datos registrados: ")
                print("===============================================")
                print()

                print("Oficina registrada")
                print("Oficina: ", oficina)
                print("Gerente de oficina: ", gerente_oficina)
                print("Agente de venta: ", agente_venta)

                oficina3 = "Dirección: " + oficina + " \n " + "Gerente: " +  gerente_oficina + " \n " + "Agente de venta: " + agente_venta

                print("Se ha registrado con éxito la oficina " + str(numero_o))
                total_oficinas = total_oficinas +1

            elif llave_secundaria == 2:
                #Nuevo inmueble
                numero_i = 0
                while numero_i <=total_inmueble:
                    numero_i = numero_i + 1

                print("Registro de la información general del inmueble")
                print("")
                
                calle = input("Introduzca la calle del inmueble: ")
                numero = int(input("Introduzca el número del inmueble: "))
                comuna = input("Introduzca la comuna del inmueble:")
                superficie_m2 = int(input("Introduzca la superficie del inmueble (m^2): "))
                valor_tasacion = float(input("Introduzca el valor de tasación del inmueble(UF): "))

                print("")
                print("Registro de la información especifica del inmueble")
                print("")
                print("Indica la opción del tipo de inmueble a registrar: ")
                print("0: Vivienda")
                print("1: Local comercial")
                print("2: Bodega")
                tipo_inmueble = int(input("El tipo de inmueble es: "))

                if tipo_inmueble == 0:
                    estado_vivienda = input("Indica si la vivienda es 'nueva' o 'usada': ")
                    tipo_vivienda = input("Indica si la vivienda es 'casa' o 'departamento': ")
                    n_habitaciones = int(input("Indica el número de habitaciones: "))
                    n_baños = int(input("Indica el número de baños: "))
                    n_cocinas = int(input("Indica el número de cocinas: "))

                    caract_fica = "|"
                    while True:
                        nueva_caracteristica = input("Opcionalmente, introdusca al menos 1 caracteristica específica del inmueble, en caso contrario o ya introdujo suficientes caracteristicas, no escriba nada")
                        caract_fica = caract_fica + nueva_caracteristica + "|"
                        if nueva_caracteristica == "":
                            break
                    inmueble3 = "Tipo: " + "vivienda " + estado_vivienda + "(" + tipo_vivienda + ")" + "\n" + "Dirección: " + calle + str(numero) + comuna + "\n" + "Superficie: " + str(superficie_m2) + " m^2" + "\n" + "Tasa de tasación: " + str(valor_tasacion) + " UF" + "\n" + "Número de habitaciones: " + str(n_habitaciones) + "\n" + "Número de baños: " + str(n_baños) + "\n" + "Número de cocinas: " + str(n_cocinas) + "\n" + "Características especificas: " + caract_fica

                elif tipo_inmueble == 1 or tipo_inmueble == 2:
                    if tipo_inmueble == 1:
                        local_o_comercio = "Local comercial"
                    elif tipo_inmueble == 2:
                        local_o_comercio = "Bodega"
                    numero_puertas =  int(input("Indica el número de puertas de acceso: "))
                    ventanas = input("Indica la presencia de ventanas (Si/No): ")
                    estructura = input("Indica si el inmueble esta 'acondicionado' o es 'planta libre': ")

                    inmueble3 = "Tipo: " + local_o_comercio + "\n" + "Dirección: " + calle + str(numero) + comuna + "\n" + "Superficie: " + str(superficie_m2) + " m^2" + "\n" + "Tasa de tasación: " + str(valor_tasacion) + " UF" + "\n" + "Número de puertas de acceso: " + str(numero_puertas) + "\n" + "¿Tiene ventanas?: " + ventanas + "\n" + "Estructura: " + estructura
                
                print("Se ha registrado con éxito el inmueble " + str(numero_i))
                total_inmueble = total_inmueble +1
            elif llave_secundaria == 3:
                #Nuevo contrato
                numero_c = 0
                while numero_c <=total_contratos:
                    numero_c = numero_c + 1
                #Información del propietario que ofrecerá el inmueble
                print("===============================================")
                print("Registro de información del propietario ")
                print("===============================================")
                print()
                nombre_propietario = input("Introduzca el nombre completo: ")
                rut_propietario = input("Introduzca el RUT: ")

                cantidad_telefono = 1
                telefono = "|" + input("Introduzca el número de contacto: ") + "|"
                while cantidad_telefono <= 3:
                    respuesta_telefono = int(input("Opsionalmente introduzca otro número (máximo 3), use una de las siguientes opciones:"))
                    print ("1. Introducir otro número")
                    print ("0. No introducir más")

                    if respuesta_telefono == 1:
                        teléfono_adicional = input("Introduzca el número de contacto adicional: ")
                        telefono = telefono + teléfono_adicional + "|"
                        
                        cantidad_telefono = cantidad_telefono + 1
                    elif respuesta_telefono == 0:

                        cantidad_telefono = cantidad_telefono + 3

                fecha_contrato = input("Introduzca la fecha en que se firmo el contrato, siguiendo el formato 'día-mes-año' (ejemplo: 12 05 2024)")

                plazo_contrato = input("Introduzca el plazo del contrato, indicando las unidades de tiempo (meses) o, si el plazo no está fijado, escriba 'indefinido': ")

                contrato3 = "Nombre del propietario: " + nombre_propietario + "\n" + "Rut: " + str(rut_propietario) + "\n" + "Número de teléfono: " + telefono + "\n" + "Fecha del contrato: " + fecha_contrato + "\n" + "Plazo del contrato: " + plazo_contrato

                print("Se ha registrado con éxito el contrato " + str(numero_c))
                total_contratos = total_contratos +1

            elif llave_secundaria == 4:
                #Nueva visita
                numero_v = 0
                while numero_v <= total_visitas:
                    numero_v = numero_v + 1
                print("===============================================")
                print("Registro de información de visita")
                print("===============================================")
                print()

                nombre_cliente = input("Ingrese nombre completo del cliente: ")
                oficina_visitar = (input("Ingrese el número de la oficina a visitar: "))
                fecha = input("Ingrese fecha de visita, siguiendo el formato 'día-mes-año' (ejemplo: 12 05 2024): ")

                comentario = "|"

                print("Si quiere poner uno o más comentarios, escoja las siguientes opsiones: ")
                print("1. Poner un comentario")
                print("0. No poner comentarios")

                llave_comentario = int(input())

                if llave_comentario == 1:
                    while True:
                        hacer_comentarios = int(input("Con '1' ponga un comentario, con '0' se deja de poner comentarios"))
                        if hacer_comentarios == 1:
                            comentario_nuevo = input("Ingrese el comentario del cliente: ")
                            comentario = comentario + comentario_nuevo + "|"
                        elif hacer_comentarios == 0:
                            break

                elif llave_comentario == 0:
                    break
                
                #Información del cliente y su visita que comprará o arrenderá el inmueble
    
                cliente3= "Nombre del cliente: " + nombre_cliente + "\n" + "Número de oficina: " + oficina_visitar + "\n" + "Fecha de visita:" + fecha + "\n" + "Comentario: " + comentario
                print("Se ha registrado con éxito la visita del cliente " + str(numero_v))
                total_visitas = total_visitas +1

            elif llave_secundaria == 0:
                print("Volviendo al menu principal")
                break


    #registrar Solicitar reporte de venta o arriendo
    elif opcion_principal == 3:

        while True:

            total_casa = total_ventas_casas + total_arriendos_casa
            
            total_depto = total_ventas_depto + total_arriendos_depto
            
            total_bodega = total_ventas_bodega + total_arriendos_bodega
            
            total_local = total_ventas_local + total_arriendos_local
            
            print("Solicitud de reportabilidad")
            print("")

            print("Seleccione el reporte que desea visualizar: ")
            print("")
            
            print("1. Total de ingresos: ")
            print("2. Total de ingresos por ventas: ")
            print("3. Total de ingresos por arriendo: ")
            print("4. Ingresos de la oficina: ")
            print("0. Total de ingresos por arriendo: ")
            print("")
            opcion_reporte = int(input("Alternativa seleccionada: "))
            print("")
            
            if opcion_reporte == 1:
                ingreso = total_casa + total_depto + total_bodega + total_local
            
            elif opcion_reporte == 2:
                print("Seleccione el reporte a visualizar: ")
                print("")
                print("1. Total ventas globales")
                print("2. Total ventas casas")
                print("3. Total ventas departamentos")
                print("4. Total ventas bodegas")
                print("5. Total ventas locales comerciales")
                alternativa_reporte = int(input("Alternativa seleccionada: "))
                
                if alternativa_reporte == 1:
                    ingreso = total_ventas_casas + total_ventas_depto + total_ventas_bodega + total_ventas_local
                elif alternativa_reporte == 2:
                    ingreso = total_ventas_casas
                elif alternativa_reporte == 3:
                    ingreso = total_ventas_depto
                elif alternativa_reporte == 4:
                    ingreso = total_ventas_bodega
                elif alternativa_reporte == 5:
                    ingreso = total_ventas_local
            
            elif opcion_reporte == 3:
                print("Seleccione el reporte a visualizar: ")
                print("")
                print("1. Total arriendo globales")
                print("2. Total arriendo casas")
                print("3. Total arriendo departamentos")
                print("4. Total arriendo bodegas")
                print("5. Total arriendo locales comerciales")
                alternativa_reporte = int(input("Alternativa seleccionada: "))
                
                if alternativa_reporte == 1:
                    ingreso = total_arriendos_casa + total_arriendos_depto + total_arriendos_bodega + total_arriendos_local
                elif alternativa_reporte == 2:
                    ingreso = total_arriendos_casa
                elif alternativa_reporte == 3:
                    ingreso = total_arriendos_depto
                elif alternativa_reporte == 4:
                    ingreso = total_arriendos_bodega
                elif alternativa_reporte == 5:
                    ingreso = total_arriendos_local

            elif opcion_reporte == 4:
                ingreso_gerente = 0.1 * ingreso
                ingreso_agente = 0.3 * ingreso
                ingreso_comision = 0.3 * ingreso
            
                print("Los ingresos son: ")
                print("Ingresos totales: ", ingreso)
                print("Ingresos por comision de gerente: ", ingreso_gerente)
                print("Ïngreso por comision de agente: ", ingreso_agente)
                print("Ingreso por comision: ", ingreso_comision)

            elif opcion_reporte == 0:
                print("Volviendo al menu principal")
                break
            
            else:
                print("La opción que ha ingresado no es valida")
    #apagar
    elif opcion_principal ==0:
        print("Adiós")
        break
    else:
        print("La opsión ingresada es inválida, intentelo de nuevo")