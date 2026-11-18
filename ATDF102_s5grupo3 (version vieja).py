# /////////////////////// DATOS PRECARGADOS  /////////////////////////////
# Oficinas
oficina_direccion = ["Estación Central", "El Bosque"]
oficina_gerente = ["Carlos Pachenco", "Nicolas Andaluz"]
oficina_agente = ["Fernando Lopez", "Roberto Paredes"]
total_oficinas = 2

# Inmuebles (datos generales)
inmueble_tipo = ["vivienda", "bodega"]
inmueble_calle = ["Avenida Vitacura", "Calle Alonso de Córdova"]
inmueble_numero = [4380, 5870]
inmueble_comuna = ["Vitacura", "Las Condes"]
inmueble_superficie = [120, 95]
inmueble_tasacion = [540.0, 1770.0]

# Inmuebles (solo viviendas, si no es vivienda queda "" o 0)
inmueble_estado = ["usada", ""]
inmueble_tipo_vivienda = ["departamento", ""]
inmueble_habitaciones = [4, 0]
inmueble_baños = [1, 0]
inmueble_cocinas = [1, 0]
inmueble_caract = ["||", ""]

# Inmuebles (solo locales comerciales y bodegas, si es vivienda queda "" o 0)
inmueble_puertas = [0, 2]
inmueble_ventanas = ["", "si"]
inmueble_estructura = ["", "acondicionado"]
total_inmueble = 2

# Contratos de los propietarios
contrato_nombre = ["Sebastián Ignacio Valdés Rojas", "Rodrigo Esteban Castillo Navarro"]
contrato_rut = ["14903221K", "108563415"]
contrato_telefono = ["|+56223456789|+56221454508|", "|+56227119034|"]
contrato_inmueble = [1, 2]
contrato_fecha = ["15 01 2026", "23 02 2025"]
contrato_plazo = ["12 meses", "indefinido"]
total_contratos = 2

# Visitas de los clientes
cliente_nombre = ["Benjamin Nicolas Castro Rojas", "Sarah Fernanda Flores Valdez"]
cliente_oficina = [1, 2]
cliente_inmueble = [2, 1]
cliente_tipo_contrato = ["Exclusividad", "Sin exclusividad"]
cliente_monto = [8.85, 0]
cliente_operacion = ["Arriendo", "Venta"]
cliente_fecha = ["13 02 2025", "15 11 2025"]
cliente_comentario = ["||", "|La casa debe ser amarilla|"]
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
# /////////////////////// Menu /////////////////////////////
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
    opcion_principal = input("Seleccione la alternativa que desea: ")
    while not opcion_principal.isdigit():
        opcion_principal = input("Debe ingresar un número, intentelo de nuevo: ")
    opcion_principal = int(opcion_principal)
    print("************************************************")

    #consulta de datos
    if opcion_principal == 1:

        while True:
            print("......................................................")
            print("Menu de consulta de datos:")
            print("......................................................")
            print("Escoja una de las siguientes opciones:")
            print("1. Consultar oficinas registrados")
            print("2. Consultar inmuebles registrados")
            print("3. Consultar contratos de propietarios registrados")
            print("4. Consultar la visitas de clientes registrados")
            print("0. Volver al menú principal")

            llave_secundaria = input("Seleccione la opción que desea (para volver al menu ingrese '0'): ")
            while not llave_secundaria.isdigit():
                llave_secundaria = input("Debe ingresar un número, intentelo de nuevo: ")
            llave_secundaria = int(llave_secundaria)

# //////////////////////// Consultar Oficina /////////////////////////////////////
            if llave_secundaria == 1:

                ox = 0
                while ox < total_oficinas:
                    print(str(ox + 1) + ":")
                    print(" Dirección: ", oficina_direccion[ox])
                    print(" Gerente: ", oficina_gerente[ox])
                    print(" Agente de venta: ", oficina_agente[ox])
                    ox = ox + 1

# ////////////////////// Consultar Inmueble /////////////////////////
            elif llave_secundaria == 2:

                ix = 0
                while ix < total_inmueble:
                    print(str(ix + 1) + ":")
                    if inmueble_tipo[ix] == "vivienda":
                        print(" Tipo: vivienda " + inmueble_estado[ix] + " (" + inmueble_tipo_vivienda[ix] + ")")
                    else:
                        print(" Tipo: ", inmueble_tipo[ix])
                    print(" Dirección: ", inmueble_calle[ix], inmueble_numero[ix], ",", inmueble_comuna[ix])
                    print(" Superficie: ", inmueble_superficie[ix], "m^2")
                    print(" Tasa de tasación: ", inmueble_tasacion[ix], "UF")
                    if inmueble_tipo[ix] == "vivienda":
                        print(" Número de habitaciones: ", inmueble_habitaciones[ix])
                        print(" Número de baños: ", inmueble_baños[ix])
                        print(" Número de cocinas: ", inmueble_cocinas[ix])
                        print(" Características especificas: ", inmueble_caract[ix])
                    else:
                        print(" Número de puertas de acceso: ", inmueble_puertas[ix])
                        print(" ¿Tiene ventanas?: ", inmueble_ventanas[ix])
                        print(" Estructura: ", inmueble_estructura[ix])
                    ix = ix + 1

# ///////////////////////////// Consultar Contrato //////////////////////
            elif llave_secundaria == 3:

                cx = 0
                while cx < total_contratos:
                    print(str(cx + 1) + ":")
                    print(" Nombre del propietario: ", contrato_nombre[cx])
                    print(" Rut: ", contrato_rut[cx])
                    print(" Número de teléfono: ", contrato_telefono[cx])
                    print(" Número de inmueble: ", contrato_inmueble[cx])
                    print(" Fecha del contrato: ", contrato_fecha[cx])
                    print(" Plazo del contrato: ", contrato_plazo[cx])
                    cx = cx + 1

# ////////////////////////// Consultar Visita //////////////////////////////
            elif llave_secundaria == 4:

                vx = 0
                while vx < total_visitas:
                    print(str(vx + 1) + ":")
                    print(" Nombre del cliente: ", cliente_nombre[vx])
                    print(" Número de oficina: ", cliente_oficina[vx])
                    print(" Número de inmueble: ", cliente_inmueble[vx])
                    print(" Tipo de contrato: ", cliente_tipo_contrato[vx])
                    if cliente_tipo_contrato[vx] == "Exclusividad":
                        print(" Monto 0.5%: ", cliente_monto[vx], "UF")
                    print(" Tipo de operación: ", cliente_operacion[vx])
                    print(" Fecha de visita: ", cliente_fecha[vx])
                    print(" Comentario: ", cliente_comentario[vx])
                    vx = vx + 1

            elif llave_secundaria == 0:

                break
            else:
                print("Opción de consulta no válida.")


    elif opcion_principal == 2:
        while True:
            print("......................................................")
            print("Menu para registrar datos nuevos:")
            print("......................................................")
            print("Escoja una de las siguientes opciones:")
            print("1. Nueva oficina")
            print("2. Nuevo inmueble")
            print("3. Nuevo contrato")
            print("4. Nueva visita")
            print("5. Nueva venta o arriendo")
            print("0. Volver al menú principal")

            llave_secundaria = input("Seleccione la opción que desea (para volver al menu ingrese '0'): ")
            while not llave_secundaria.isdigit():
                llave_secundaria = input("Debe ingresar un número, intentelo de nuevo: ")
            llave_secundaria = int(llave_secundaria)

# //////////////////////// Registro Oficina /////////////////////////////////////
            if llave_secundaria == 1:

                numero_o = total_oficinas + 1

                print("Registro de información de la oficina")
                print("")
                oficina = input("Introduzca la dirección de la sucursal de la oficina: ")
                while oficina == "":
                    oficina = input("No puede quedar vacío, introduzca la dirección: ")
                gerente_oficina = input("Introduzca el nombre del gerente de oficina: ")
                while gerente_oficina == "":
                    gerente_oficina = input("No puede quedar vacío, introduzca el nombre del gerente: ")
                agente_venta =input("Introduzca el nombre del agente de venta: ")
                while agente_venta == "":
                    agente_venta = input("No puede quedar vacío, introduzca el nombre del agente: ")
                print("===============================================")
                print("Datos registrados: ")
                print("===============================================")
                print()

                print("Oficina registrada")
                print("Oficina: ", oficina)
                print("Gerente de oficina: ", gerente_oficina)
                print("Agente de venta: ", agente_venta)

                oficina_direccion.append(oficina)
                oficina_gerente.append(gerente_oficina)
                oficina_agente.append(agente_venta)

                print("Se ha registrado con éxito la oficina " + str(numero_o))
                total_oficinas = total_oficinas +1

# ////////////////////// Registro Inmueble /////////////////////////
            elif llave_secundaria == 2:

                numero_i = total_inmueble + 1

                print("Registro de la información general del inmueble")
                print("")

                calle = input("Introduzca la calle del inmueble: ")
                numero = input("Introduzca el número del inmueble: ")
                while not numero.isdigit():
                    numero = input("Debe ser un número, introduzca el número del inmueble: ")
                numero = int(numero)
                comuna = input("Introduzca la comuna del inmueble:")
                superficie_m2 = input("Introduzca la superficie del inmueble (m^2): ")
                while not superficie_m2.isdigit() or int(superficie_m2) <= 0:
                    superficie_m2 = input("Debe ser un número mayor que cero, introduzca la superficie (m^2): ")
                superficie_m2 = int(superficie_m2)
                valor_tasacion = input("Introduzca el valor de tasación del inmueble(UF): ")
                while not valor_tasacion.replace(".", "", 1).isdigit() or float(valor_tasacion) <= 0:
                    valor_tasacion = input("Debe ser un número mayor que cero (use punto para decimales): ")
                valor_tasacion = float(valor_tasacion)

                print("")
                print("Registro de la información especifica del inmueble")
                print("")
                print("Indica la opción del tipo de inmueble a registrar: ")
                print("0: Vivienda")
                print("1: Local comercial")
                print("2: Bodega")
                tipo_inmueble = input("El tipo de inmueble es: ")
                while tipo_inmueble != "0" and tipo_inmueble != "1" and tipo_inmueble != "2":
                    tipo_inmueble = input("Opción no válida, ingrese 0, 1 o 2: ")
                tipo_inmueble = int(tipo_inmueble)

                if tipo_inmueble == 0:
                    estado_vivienda = input("Indica si la vivienda es 'nueva' o 'usada': ")
                    while estado_vivienda != "nueva" and estado_vivienda != "usada":
                        estado_vivienda = input("Debe escribir 'nueva' o 'usada': ")
                    tipo_vivienda = input("Indica si la vivienda es 'casa' o 'departamento': ")
                    while tipo_vivienda != "casa" and tipo_vivienda != "departamento":
                        tipo_vivienda = input("Debe escribir 'casa' o 'departamento': ")
                    n_habitaciones = input("Indica el número de habitaciones: ")
                    while not n_habitaciones.isdigit():
                        n_habitaciones = input("Debe ser un número, indica el número de habitaciones: ")
                    n_baños = input("Indica el número de baños: ")
                    while not n_baños.isdigit():
                        n_baños = input("Debe ser un número, indica el número de baños: ")
                    n_cocinas = input("Indica el número de cocinas: ")
                    while not n_cocinas.isdigit():
                        n_cocinas = input("Debe ser un número, indica el número de cocinas: ")

                    caract_fica = "|"
                    while True:
                        nueva_caracteristica = input("Opcionalmente, introduzca una caracteristica específica del inmueble, si no quiere agregar más, no escriba nada: ")
                        if nueva_caracteristica == "":
                            break
                        caract_fica = caract_fica + nueva_caracteristica + "|"

                    inmueble_tipo.append("vivienda")
                    inmueble_estado.append(estado_vivienda)
                    inmueble_tipo_vivienda.append(tipo_vivienda)
                    inmueble_habitaciones.append(int(n_habitaciones))
                    inmueble_baños.append(int(n_baños))
                    inmueble_cocinas.append(int(n_cocinas))
                    inmueble_caract.append(caract_fica)
                    inmueble_puertas.append(0)
                    inmueble_ventanas.append("")
                    inmueble_estructura.append("")

                elif tipo_inmueble == 1 or tipo_inmueble == 2:
                    if tipo_inmueble == 1:
                        local_o_comercio = "local comercial"
                    elif tipo_inmueble == 2:
                        local_o_comercio = "bodega"
                    numero_puertas =  input("Indica el número de puertas de acceso: ")
                    while not numero_puertas.isdigit():
                        numero_puertas = input("Debe ser un número, indica el número de puertas de acceso: ")
                    ventanas = input("Indica la presencia de ventanas (si/no): ")
                    while ventanas != "si" and ventanas != "no":
                        ventanas = input("Debe escribir 'si' o 'no': ")
                    estructura = input("Indica si el inmueble esta 'acondicionado' o es 'planta libre': ")
                    while estructura != "acondicionado" and estructura != "planta libre":
                        estructura = input("Debe escribir 'acondicionado' o 'planta libre': ")

                    inmueble_tipo.append(local_o_comercio)
                    inmueble_puertas.append(int(numero_puertas))
                    inmueble_ventanas.append(ventanas)
                    inmueble_estructura.append(estructura)

                    inmueble_estado.append("")
                    inmueble_tipo_vivienda.append("")
                    inmueble_habitaciones.append(0)
                    inmueble_baños.append(0)
                    inmueble_cocinas.append(0)
                    inmueble_caract.append("")

                inmueble_calle.append(calle)
                inmueble_numero.append(numero)
                inmueble_comuna.append(comuna)
                inmueble_superficie.append(superficie_m2)
                inmueble_tasacion.append(valor_tasacion)

                print("Se ha registrado con éxito el inmueble " + str(numero_i))
                total_inmueble = total_inmueble +1

# ///////////////////////////// Registro Contrato //////////////////////
            elif llave_secundaria == 3:

                numero_c = total_contratos + 1

                print("===============================================")
                print("Registro de información del propietario y de su contrato en el que ingreso su inmueble")
                print("===============================================")
                print()
                nombre_propietario = input("Introduzca el nombre completo: ")
                while nombre_propietario == "":
                    nombre_propietario = input("No puede quedar vacío, introduzca el nombre completo: ")
                rut_propietario = input("Introduzca el RUT sin puntos ni guion: ")
                while len(rut_propietario) < 8 or len(rut_propietario) > 9 or not rut_propietario[:-1].isdigit():
                    rut_propietario = input("RUT no válido, introduzcalo sin puntos ni guion (ejemplo: 14903221K): ")

                cantidad_telefono = 1
                telefono = "|" + input("Introduzca el número de contacto: ") + "|"
                while cantidad_telefono < 3:
                    print ("Opcionalmente introduzca otro número (máximo 3), use una de las siguientes opciones:")
                    print ("1. Introducir otro número")
                    print ("0. No introducir más")
                    respuesta_telefono = input()

                    if respuesta_telefono == "1":
                        teléfono_adicional = input("Introduzca el número de contacto adicional: ")
                        telefono = telefono + teléfono_adicional + "|"

                        cantidad_telefono = cantidad_telefono + 1
                    elif respuesta_telefono == "0":
                        break
                    else:
                        print("Opción no válida")

                inmueble_contrato = input("Introduzca el número del inmueble que se ingresa con este contrato: ")
                while not inmueble_contrato.isdigit() or int(inmueble_contrato) < 1 or int(inmueble_contrato) > total_inmueble:
                    inmueble_contrato = input("No hay un inmueble registrado con ese número, ingrese otro: ")
                inmueble_contrato = int(inmueble_contrato)

                fecha_contrato = input("Introduzca la fecha en que se firmo el contrato, siguiendo el formato 'día-mes-año' (ejemplo: 12 05 2024): ")

                plazo_contrato = input("Introduzca el plazo del contrato, indicando las unidades de tiempo (meses) o, si el plazo no está fijado, escriba 'indefinido': ")

                contrato_nombre.append(nombre_propietario)
                contrato_rut.append(rut_propietario)
                contrato_telefono.append(telefono)
                contrato_inmueble.append(inmueble_contrato)
                contrato_fecha.append(fecha_contrato)
                contrato_plazo.append(plazo_contrato)

                print("Se ha registrado con éxito el contrato " + str(numero_c))
                total_contratos = total_contratos +1

# ////////////////////////// Registro Visita //////////////////////////////
            elif llave_secundaria == 4:

                numero_v = total_visitas + 1
                print("===============================================")
                print("Registro de información de visita")
                print("===============================================")
                print()

                nombre_cliente = input("Ingrese nombre completo del cliente: ")
                while nombre_cliente == "":
                    nombre_cliente = input("No puede quedar vacío, ingrese nombre completo del cliente: ")

                while True:
                    oficina_visitar = input("Ingrese el número de la oficina a visitar: ")
                    if not oficina_visitar.isdigit() or int(oficina_visitar) < 1 or int(oficina_visitar) > total_oficinas:
                        print("No hay una oficina registrada con ese número, ingrese otro")
                    else:
                        oficina_visitar = int(oficina_visitar)
                        break

                while True:
                    inmueble_interes = input("Ingrese el número del inmueble para comprar o arrendar: ")
                    if not inmueble_interes.isdigit() or int(inmueble_interes) < 1 or int(inmueble_interes) > total_inmueble:
                        print("No hay un inmueble registrado con ese número, ingrese otro")
                    else:
                        inmueble_interes = int(inmueble_interes)
                        break

                fecha = input("Ingrese fecha de visita, siguiendo el formato 'día-mes-año' (ejemplo: 12 05 2024): ")

                print("Escoja la opción para indicar el tipo de operación: ")
                print("1. Venta")
                print("2. Arriendo")
                opcion_operación = input("Escoja la opción para indicar el tipo de operación: ")
                while opcion_operación != "1" and opcion_operación != "2":
                    opcion_operación = input("Opción no válida, ingrese 1 o 2: ")

                tipo_operación = ""
                if opcion_operación == "1":
                    tipo_operación = "Venta"
                elif opcion_operación == "2":
                    tipo_operación = "Arriendo"

                comentario = "|"

                print("Si quiere poner uno o más comentarios, escoja las siguientes opciones: ")
                print("1. Poner un comentario")
                print("0. No poner comentarios")

                llave_comentario = input()

                if llave_comentario == "1":
                    while True:
                        comentario_nuevo = input("Ingrese el comentario del cliente (si no quiere agregar más, no escriba nada): ")
                        if comentario_nuevo == "":
                            break
                        comentario = comentario + comentario_nuevo + "|"

                if comentario == "|":
                    comentario = "||"


                print("Antes de terminar, escoja la opción del tipo de contrato comercial a realizar:")
                print("0. Exclusividad (Escoger esta opción hará que el cliente deba cancelar un monto del 0.5 % del valor de tasación del inmueble )")
                print("1. Sin exclusividad")

                opcion_tcontrato = input()
                while opcion_tcontrato != "0" and opcion_tcontrato != "1":
                    opcion_tcontrato = input("Opción no válida, ingrese 0 o 1: ")

                if opcion_tcontrato == "0":
                    tipo_contrato = "Exclusividad"

                    tasacion = inmueble_tasacion[inmueble_interes - 1]
                    monto = tasacion * 0.5 / 100
                    print("El cliente debe cancelar: ", monto, "UF")

                elif opcion_tcontrato == "1":
                    tipo_contrato = "Sin exclusividad"
                    monto = 0

                cliente_nombre.append(nombre_cliente)
                cliente_oficina.append(oficina_visitar)
                cliente_inmueble.append(inmueble_interes)
                cliente_tipo_contrato.append(tipo_contrato)
                cliente_monto.append(monto)
                cliente_operacion.append(tipo_operación)
                cliente_fecha.append(fecha)
                cliente_comentario.append(comentario)

                print("Se ha registrado con éxito la visita del cliente " + str(numero_v))
                total_visitas = total_visitas +1

# ////////////////////////// Registro Venta o Arriendo //////////////////////////////
            elif llave_secundaria == 5:

                print("===============================================")
                print("Registro de venta o arriendo")
                print("===============================================")
                print()
                print("Indica el tipo de inmueble: ")
                print("1. Casa")
                print("2. Departamento")
                print("3. Bodega")
                print("4. Local comercial")
                tipo_venta = input("El tipo de inmueble es: ")
                while tipo_venta != "1" and tipo_venta != "2" and tipo_venta != "3" and tipo_venta != "4":
                    tipo_venta = input("Opción no válida, ingrese un número del 1 al 4: ")

                print("Indica el tipo de operación: ")
                print("1. Venta")
                print("2. Arriendo")
                operacion = input("La operación es: ")
                while operacion != "1" and operacion != "2":
                    operacion = input("Opción no válida, ingrese 1 o 2: ")

                monto_operacion = input("Introduzca el monto en pesos (sin puntos): ")
                while not monto_operacion.isdigit() or int(monto_operacion) <= 0:
                    monto_operacion = input("Debe ser un número mayor que cero, sin puntos: ")
                monto_operacion = int(monto_operacion)

                if tipo_venta == "1" and operacion == "1":
                    total_ventas_casas = total_ventas_casas + monto_operacion
                elif tipo_venta == "1" and operacion == "2":
                    total_arriendos_casa = total_arriendos_casa + monto_operacion
                elif tipo_venta == "2" and operacion == "1":
                    total_ventas_depto = total_ventas_depto + monto_operacion
                elif tipo_venta == "2" and operacion == "2":
                    total_arriendos_depto = total_arriendos_depto + monto_operacion
                elif tipo_venta == "3" and operacion == "1":
                    total_ventas_bodega = total_ventas_bodega + monto_operacion
                elif tipo_venta == "3" and operacion == "2":
                    total_arriendos_bodega = total_arriendos_bodega + monto_operacion
                elif tipo_venta == "4" and operacion == "1":
                    total_ventas_local = total_ventas_local + monto_operacion
                elif tipo_venta == "4" and operacion == "2":
                    total_arriendos_local = total_arriendos_local + monto_operacion

                print("Se ha registrado con éxito la operación por $", monto_operacion)

            elif llave_secundaria == 0:
                print("Volviendo al menu principal")
                break
            else:
                print("Opción de registro no válida.")


# ///////////////////////// Solicitar reporte ////////////////////
    elif opcion_principal == 3:

        ingreso = total_ventas_casas + total_arriendos_casa + total_ventas_depto + total_arriendos_depto + total_ventas_bodega + total_arriendos_bodega + total_ventas_local + total_arriendos_local
        fuente_ingresos = "todos los inmuebles"

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
            print("0. Volver al menú principal")
            print("")
            opcion_reporte = input("Alternativa seleccionada: ")
            while not opcion_reporte.isdigit():
                opcion_reporte = input("Debe ingresar un número, intentelo de nuevo: ")
            opcion_reporte = int(opcion_reporte)
            print("")

            if opcion_reporte == 1:
                ingreso = total_casa + total_depto + total_bodega + total_local
                fuente_ingresos = "todos los inmuebles"
                print("Los ingresos totales son: ",ingreso)

            elif opcion_reporte == 2:
                print("Seleccione el reporte a visualizar: ")
                print("")
                print("1. Total ventas globales")
                print("2. Total ventas casas")
                print("3. Total ventas departamentos")
                print("4. Total ventas bodegas")
                print("5. Total ventas locales comerciales")
                alternativa_reporte = input("Alternativa seleccionada: ")
                while alternativa_reporte != "1" and alternativa_reporte != "2" and alternativa_reporte != "3" and alternativa_reporte != "4" and alternativa_reporte != "5":
                    alternativa_reporte = input("Opción no válida, ingrese un número del 1 al 5: ")
                alternativa_reporte = int(alternativa_reporte)

                if alternativa_reporte == 1:
                    ingreso = total_ventas_casas + total_ventas_depto + total_ventas_bodega + total_ventas_local
                    fuente_ingresos = "todos los inmuebles vendidos"

                    print("Ingresos totales en ventas: ",ingreso)

                elif alternativa_reporte == 2:
                    ingreso = total_ventas_casas
                    fuente_ingresos = "las ventas de casas"
                    print("Ingresos totales en ventas de casas: ",ingreso)

                elif alternativa_reporte == 3:
                    ingreso = total_ventas_depto
                    fuente_ingresos = "las ventas de departamentos"
                    print("Ingresos totales en ventas de departamento: ",ingreso)

                elif alternativa_reporte == 4:
                    ingreso = total_ventas_bodega
                    fuente_ingresos = "las ventas de bodegas"
                    print("Ingresos totales en ventas de bodegas: ",ingreso)

                elif alternativa_reporte == 5:
                    ingreso = total_ventas_local
                    fuente_ingresos = "las ventas de locales comerciales"
                    print("Ingresos totales en ventas de locales comerciales: ",ingreso)

            elif opcion_reporte == 3:
                print("Seleccione el reporte a visualizar: ")
                print("")
                print("1. Total arriendo globales")
                print("2. Total arriendo casas")
                print("3. Total arriendo departamentos")
                print("4. Total arriendo bodegas")
                print("5. Total arriendo locales comerciales")
                alternativa_reporte = input("Alternativa seleccionada: ")
                while alternativa_reporte != "1" and alternativa_reporte != "2" and alternativa_reporte != "3" and alternativa_reporte != "4" and alternativa_reporte != "5":
                    alternativa_reporte = input("Opción no válida, ingrese un número del 1 al 5: ")
                alternativa_reporte = int(alternativa_reporte)

                if alternativa_reporte == 1:
                    ingreso = total_arriendos_casa + total_arriendos_depto + total_arriendos_bodega + total_arriendos_local
                    fuente_ingresos = "los arriendos de todos los inmuebles"
                    print("Ingresos totales en arriendos: ",ingreso)
                elif alternativa_reporte == 2:
                    ingreso = total_arriendos_casa
                    fuente_ingresos = "los arriendos de casas"
                    print("Ingresos totales en arriendos de casas: ",ingreso)
                elif alternativa_reporte == 3:
                    ingreso = total_arriendos_depto
                    fuente_ingresos = "los arriendos de departamentos"
                    print("Ingresos totales en arriendos de departamentos: ",ingreso)
                elif alternativa_reporte == 4:
                    ingreso = total_arriendos_bodega
                    fuente_ingresos = "los arriendos de las bodegas"
                    print("Ingresos totales en arriendos de bodegas: ",ingreso)
                elif alternativa_reporte == 5:
                    ingreso = total_arriendos_local
                    fuente_ingresos = "los arriendos de los locales comerciales"
                    print("Ingresos totales en arriendos de locales comerciales: ",ingreso)

            elif opcion_reporte == 4:
                ingreso_gerente = comision_gerente * ingreso
                ingreso_agente = comision_agente * ingreso
                ingreso_comision = comision_venta * ingreso

                print("Los ingresos de la oficina, según los ingresos de " + fuente_ingresos + " son: ")
                print("Ingresos totales: ", ingreso)
                print("Ingresos por comision de gerente: ", ingreso_gerente)
                print("Ingreso por comision de agente: ", ingreso_agente)
                print("Ingreso por comision: ", ingreso_comision)

            elif opcion_reporte == 0:
                print("Volviendo al menu principal")
                break

            else:
                print("La opción que ha ingresado no es valida")

    elif opcion_principal ==0:
        print("Adiós")
        break
    else:
        print("La opción ingresada es inválida, intentelo de nuevo")
