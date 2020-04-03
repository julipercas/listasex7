#La Junta de Castilla y León nos ha mandado realizar una aplicación para almacenar información sobre los infectados por el COVID-19. Los datos ha día de hoy son los siguientes (sacados hoy lunes de la página de datos abiertos de la junta)
#Para realizar la aplicación el jefe de proyecto nos insta a que utilicemos listas como forma  para almacenar la información.
#Además nos ha pedido que la aplicación debe tener un menú para modificar, dar de alta, y visualizar los datos por provincias, así como dar el total de toda la comunidad. El menú podría ser algo parecido a esto:
#Partir del siguiente código.
import time
import os
try:
    def altaprovincia(provincias):
        provincia=input("Introduzca el nombre de la provincia: ")
        provincias.append(provincia)
        return provincias
    def altacomunidad(comunidades):
        comunidad=input("Introduzca el nombre de la comunidad: ")
        comunidades.append(comunidad)
        return comunidades
    def altaconfirmado(confirmados):
        confirmado=int(input("Indique la cantidad de casos confirmados: "))
        confirmados.append(confirmado)
        return confirmados
    def altapositivo(nuevospositivos):
        positivo=int(input("Indique la cantidad de nuevos casos positivos: "))
        nuevospositivos.append(positivo)
        return nuevospositivos
    def modificarconfirmados(confirmados,nuevoscasos):
        confirmados[indice]+=nuevoscasos
        return confirmados
    def modificarnuevos(nuevospositivos,nuevoscasos):
        nuevospositivos[indice]=nuevoscasos
        return nuevospositivos
    def getIndexPositions(comunidades, comunidad):
        IndicePosicion = []
        indices = 0
        while True:
            try:
                indices = comunidades.index(comunidad, indices)
                IndicePosicion.append(indices)
                indices += 1
            except ValueError:
                break
        return IndicePosicion

    def calcularnuevosporcomunidades():
        n_elementos_lista=len(provincias)
        totalnuev=0
        for indiceposicion in range (0,n_elementos_lista):
            totalnuev+=nuevospositivos[indiceposicion]
        return totalnuev
        
    def calcularconfirmadosporcomunidades():
        n_elementos_lista=len(provincias)
        totalconf=0
        for indiceposicion in range (0,n_elementos_lista):
            totalconf+=confirmados[indiceposicion]
        return totalconf

    def mostrardatosporcomunidades(comunidades,confirmados,nuevospositivos):
        print("En la comunidad de",comunidad,"hay un total de...")
        print(totalconf,"casos confirmados.")
        print(totalnuev,"casos nuevos")
        input("\nPulse una tecla para continuar ....")
        
    def mostrardatosporprovincias(provincias,confirmados,nuevospositivos):
        n_elementos_lista=len(provincias)
        print("El número de elementos de la lista", n_elementos_lista)
        print("LISTADO DE PROVINCIAS, COMUNIDADES AUTONOMAS, Y CASOS CONFIRMADOS")
        print("--------------------------------")
        for indice in range(0,n_elementos_lista):
            print(provincias[indice],"\t\t",confirmados[indice],"\t",nuevospositivos[indice])
        input("\nPulse una tecla para continuar ....")


    provincias=["Avila","Burgos","Leon","Palencia","Salamanca","Segovia","Soria","Valladolid","Zamora"]
    comunidades=["Castilla y leon","Castilla y leon","Castilla y leon","Castilla y leon","Castilla y leon","Castilla y leon","Castilla y leon","Castilla y leon","Castilla y leon"]
    confirmados=[414,719,821,262,1030,567,523,886,192]
    nuevospositivos=[33,46,95,42,148,64,92,79,24]
    opcion=1
    while opcion!=5:
        os.system ("cls")  
        print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
        print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        print("\t1.- Dar de alta  Provincia y datos (confirmados y nuevos)")
        print("\t2.- Introduce una provincia para modificar sus datos(confirmados y nuevos) " )
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la Comunidad ")
        print("\t4.- Listado de la situacion  general por provincias(confirmados y nuevos)")
        print("\t5.-Salir")
        opcion=int(input("Que desea hacer?: "))
        if opcion==1:
            provincias=altaprovincia(provincias)
            comunidades=altacomunidad(comunidades)
            confirmados=altaconfirmado(confirmados)
            nuevospositivos=altapositivo(nuevospositivos)
        elif opcion==2:
            provincia=input("Introduzca el nombre de la provincia cuyos datos quiera modificar: ")
            indice=provincias.index(provincia)
            nuevoscasos=int(input("Introduzca la cantidad de casos nuevos que quieres agregar a los datos actuales: "))
            confirmados=modificarconfirmados(confirmados,nuevoscasos)
            nuevospositivos=modificarnuevos(nuevoscasos,nuevospositivos)
        elif opcion==3:
            comunidad=input("Que Comunidad desea consultar?")
            indiceposicion=getIndexPositions(comunidades,comunidad)
            totalconf=calcularconfirmadosporcomunidades()
            totalnuev=calcularnuevosporcomunidades()
            mostrardatosporcomunidades(comunidades,confirmados,nuevospositivos)
        elif opcion==4:
            mostrardatosporprovincias(provincias,confirmados,nuevospositivos)
        elif opcion==5:
            print("terminar")
        else:
            print("Por favor, seleccione una opcion valida.")
except ValueError:
    print("No pude convertir el dato a un entero.")
except Exception as e: 
    print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )

