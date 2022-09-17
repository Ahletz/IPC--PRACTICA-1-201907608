
from telnetlib import PRAGMA_HEARTBEAT
from Lista import *

class Principal:

    def __init__(self):
        
        self.Listas = Lista()
        
        print('------BIENVENIDO A SHUCOS TITI !!------')
        print('0000000000000000000000000000000000000000  ---------------')
        print('0000000000++++++++O000000000000000000000 |  +++  ++  ++  |')
        print('000000000++++++++0000++++++++00000000000 |  +  + ++  ++  |')
        print('000000000++++++++000+++++++++00000000000 |  +  + ++  ++  |')
        print('000000000++++++++000+++++++++00000000000 |  +++   ++++   |')
        print('0000000000++++++000000+++++++00000000000 ---  -----------')
        print('000000000000              00000000000000    \ /')
        print('000000000000   ***  ***    0000000000000')
        print('000000000000   ***  ***    0000000000000')
        print('000000000000   ***  ***     000O00000000')
        print('000000000000      000       000000000000')
        print('0000000000000000000000000000000000000000')
        print('0000000000K00000000000000000000000000000')

        self.Menu()


    def Menu(self):

        salida = True
        self.No_orden = 1 #NUMERO DE LAS ORDENES
        self.Numero = 1 #NUMERO DE ORDENES DESPACHADAS

        while salida == True:

            print()
            print('|| SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: ||')
            print('|| 1. Nueva Orden.                            ||')
            print('|| 2. Despachar orden.                        ||')
            print('|| 3. Eliminar Orden.                         ||')
            print('|| 4. Ver ordenes.                            ||')
            print('|| 5. Desarrollador                           ||')
            print('|| 6. Salir                                   ||')
            print()

            opcion = int(input())

            if opcion == 1:
                
                self.Nueva_orden()

            elif opcion == 2:

                self.Despachar()
                

            elif opcion == 3:
                
                self.Eliminar_orden()

            elif opcion == 4:
                
                self.Listas.Graficar()

            elif opcion == 5:
                
                self.Datos_desarollador()

            elif opcion == 6:
                
                salida = False
                print()

                print('||---GRACIAS POR UTILIZAR SHUCOS TITI---||')

                print('0000000000000000000000000000000000000000  -------------------------------------------')
                print('0000000000++++++++O000000000000000000000 |   +++++    +++    +++  ++++++++  +++++++  |')
                print('000000000++++++++0000++++++++00000000000 |  ++   ++    ++    ++   +++  +++  ++    +  |')
                print('000000000++++++++000+++++++++00000000000 | +++++++++    ++++++    ++    ++    ++     |')
                print('000000000++++++++000+++++++++00000000000 | +++   +++      ++      +++  +++  +    ++  |')
                print('0000000000++++++000000+++++++00000000000 | +++   +++      ++      ++++++++  +++++++  |')
                print('000000000000              00000000000000 ---  ---------------------------------------')
                print('000000000000   ***  ***    0000000000000    \ /')
                print('000000000000   ***  ***    0000000000000')
                print('000000000000   ***  ***     000O00000000')
                print('000000000000      000       000000000000')
                print('0000000000000000000000000000000000000000')
                print('0000000000K00000000000000000000000000000')

            else: 

                print('||------NO INGRESO UNA OPCION VALIDA!------||')


    def Nueva_orden(self):

        tiempo = 0 #tiempo de espera

        print()
        print('||INGRESE NOMBRE DEL CLIENTE:                          ||')

        nombre = input()

        print()
        print('||INGRESE NIT DEL CLIENTE:                             ||')

        nit = input()
        
        print()
        print('||INGRESE LA CANTIDAD DE SHUCOS QUE DESEA ORDENAR:     ||')
        print()

        cantidad = int(input())

        for i in range(cantidad):

            print('|| Elija el Ingrediente del shuco No. '+ str(i+1)+' :  ||')
            print()

            #MOSTRAR LOS INGREDIENTES
            
            print('|| 1.SALCHICHA - tiempo de preparacion: 2 minutos    - Precio: Q 5.00  ||')
            print('|| 2.CHORIZO   - tiempo de preparacion: 3 minutos    - Precio: Q 7.00  ||')
            print('|| 3.SALAMI    - tiempo de preparacion: 1.5 minutos  - Precio: Q 7.00  ||')
            print('|| 4.LONGANIZA - tiempo de preparacion: 4 minutos    - Precio: Q 6.00  ||')
            print('|| 5.COSTILLA  - tiempo de preparacion: 6 minutos    - Precio: Q 10.00 ||')
            print()

            salida = True
           
            while salida == True:

                opcion = int(input()) #ingreso de orden

                if opcion == 1:
                    
                    print('||  Su shuco de SALCHICHA se ha agregado a la orde - tiempo de preparacion: 2 minutos ||')
                    self.Listas.agregar(self.No_orden, nombre, nit, '5', 'SALCHICHA', '2')
                    salida = False

                elif opcion == 2:

                    print('||  Su shuco de CHORIZO se ha agregado a la orde - tiempo de preparacion: 3 minutos   ||')
                    self.Listas.agregar(self.No_orden, nombre, nit, '7', 'CHORIZO', '3')
                    salida = False

                elif opcion == 3:

                    print('||  Su shuco de SALAMI se ha agregado a la orde - tiempo de preparacion: 1.5 minutos  ||')
                    self.Listas.agregar(self.No_orden, nombre, nit, '7', 'SALAMI', '1.5')
                    salida = False

                elif opcion == 4:

                    print('||  Su shuco de LONGANIZA se ha agregado a la orde - tiempo de preparacion: 4 minutos ||')
                    self.Listas.agregar(self.No_orden, nombre, nit, '6', 'LONGANIZA', '4')
                    salida = False

                elif opcion == 5:

                    print('||  Su shuco de COSTILLA se ha agregado a la orde - tiempo de preparacion: 6 minutos  ||')
                    self.Listas.agregar(self.No_orden, nombre, nit, '10', 'COSTILLA', '6')
                    salida = False

                else:

                    print('||------NO INGRESO UNA OPCION VALIDA!------||')


        

        print()
        print('|| SU ORDEN ESTARA LISTA EN :   ||')

        self.Listas.Tiempo_espera()
        #MOSTRAR TIEMPO DE SALIDA DE ORDEN

        print('|| ORDENES EN COLA:             ||')   
        print()

        self.Listas.Imprimir()
        print()

        self.No_orden +=1

        

    def Datos_desarollador(self):

        print()
        print('||--------------------------------||')
        print('|| FACULTAD DE INGENIERIA         ||')
        print('|| ESCUELA DE CIENCIAS Y SISTEMAS ||')
        print('|| LUDWING ALEXANDER LÓPEZ ORTIS  ||')
        print('|| 201907608                      ||')
        print('|| ludwingalexander230@gmail.com  ||')
        print('||--------------------------------||')
        print()

    def Despachar(self):

        
        

        while self.Listas.buscar(self.Numero):

            if self.Listas.buscar(self.Numero):

                self.Listas.Eliminar(self.Numero)
        
        if self.Listas.tamano()>1:

            self.Numero += 1

            print()
            print('ORDEN #'+ str(self.Numero) + ' DESPACHADA!!!' )
            print()

            print()
            print('ORDENES EN COLA: ' )
            self.Listas.Imprimir()
            print()


        else:

            print()
            print('|| NO HAY ORDENES EN COLA ||')

    def Eliminar_orden(self):

        tamaño = self.Listas.tamano()

        print()
        print('|| SELECCION LA ORDEN QUE DESEA ELIMINAR:    ||')
        print()

        
        print()
        self.Listas.Imprimir()
        print()
        Numero = int(input())
        print()

        if Numero <= tamaño or Numero >= 1:
            while self.Listas.buscar(Numero):

                if self.Listas.buscar(Numero):

                    self.Listas.Eliminar(Numero)

            print()
            print('|| ORDEN #'+ str(Numero) + ' ELIMINADA!! ||')
            print()

        else:

            print()
            print('|| ORDEN INEXISTENTE                     ||')
            print()

        print('|| ORDENES EN COLA:             ||')   
        print()

        self.Listas.Imprimir()
        print()




        


llamado = Principal()