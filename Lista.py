from graphviz import Digraph

class Nodo:
    def __init__(self, No_orden, cliente, nit, precio, ingrediente, tiempo):

        self.NoOrden = No_orden
        self.cliente = cliente
        self.nit = nit
        self.precio = precio
        self.ingediente = ingrediente
        self.tiempo = tiempo
        self.siguiente = None

    def obtenerCliente(self):
        return self.cliente

    def obtenerNO_orden(self):
        return self.NoOrden

    def obtenerNit(self):
        return self.nit

    def obtenerprecio(self):
        return self.precio

    def obteneringrediente(self):
        return self.ingediente

    def obtenertiempo(self):
        return self.tiempo

    def obtenerSiguienteOrden(self):
        return self.siguiente_orden

    def obtenerSiguienteCliente(self):
        return self.siguiente_cliente

    def obtenerSiguienteNit(self):
        return self.siguiente_nit

    def obtenerSiguientePrecio(self):
        return self.siguiente_precio

    def obtenerSiguienteIngrediente(self):
        return self.siguiente_ingrediente

    def obtenerSiguienteTiempo(self):
        return self.siguiente_tiempo

    def asignarDato(self, No_orden, cliente, nit, precio, ingrediente, tiempo):
        self.NoOrden = No_orden
        self.cliente = cliente
        self.nit = nit
        self.precio = precio
        self.ingediente = ingrediente
        self.tiempo = tiempo

    def asignarSiguiente(self, No_orden, cliente, nit, precio, ingrediente, tiempo):
        self.siguiente_orden = No_orden
        self.siguiente_cliente = cliente
        self.siguiente_nit = nit
        self.siguiente_precio = precio
        self.siguiente_ingrediente = ingrediente
        self.siguiente_tiempo = tiempo


class Lista:

    def __init__(self):

        self.head = None

    def Vacia(self):

        return self.head == None

    def agregar(self, No_orden, cliente, nit, precio, ingrediente, tiempo):

        Nod = Nodo(No_orden, cliente, nit, precio, ingrediente, tiempo)
        Nod.asignarSiguiente(self.head, self.head,
                             self.head, self.head, self.head, self.head)
        self.head = Nod

    def Tiempo_espera(self):

        actual = self.head
        contador = 0

        while actual != None:

            contador = contador + float(actual.obtenertiempo())
            actual = actual.obtenerSiguienteOrden()

        if contador > 60:

            i = contador
            j = int(i/60)
            k = i%60

            tiempo = 'Hora: '+str(j) + ' Minutos: ' + str(k)

            print()
            print(tiempo)
            print()

        else:

            tiempo = 'Minutos: '+str(contador) 

            print()
            print(tiempo)
            print()

        

    def Imprimir(self):

        actual = self.head
        while actual != None:
            print('No de orden: #'+ str(actual.obtenerNO_orden())+' - Cliente: '+actual.obtenerCliente()+' - SHUCO: '+ actual.obteneringrediente())
            actual = actual.obtenerSiguienteOrden()

    def buscar(self, No_orden):

        actual = self.head
        encontrado = False

        while actual != None and not encontrado:
            if actual.obtenerNO_orden() == No_orden:
                encontrado = True
            else:
                actual = actual.obtenerSiguienteOrden()

        return encontrado

    def Eliminar(self, No_orden):

        actual = self.head
        previo = None
        encontrado = False

        while not encontrado:
            if actual.obtenerNO_orden() == No_orden:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguienteOrden()

        if previo == None:
            self.head = actual.obtenerSiguienteOrden()
        else:
            previo.asignarSiguiente(actual.obtenerSiguienteOrden(), actual.obtenerSiguienteCliente(), actual.obtenerSiguienteNit(
            ), actual.obtenerSiguientePrecio(), actual.obtenerSiguienteIngrediente(), actual.obtenerSiguienteTiempo())

    def tamano(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguienteCliente()

        return contador

    def Graficar(self):

        dot = Digraph ( 'COLA' , filename = 'COLA.dot' , engine = 'dot' , format = 'svg' )
        dot.attr ( rankdir = "LR" )
        dot.node_attr.update ( shape = "box" )
        dot.node_attr [ 'style' ] = "filled"
        
        contador = 0
        
        actual = self.head
        while actual != None:
            
            contador +=1
            dot.node(str(contador),'ORDEN #'+str(actual.obtenerNO_orden())+' INGREDIENTE:'+actual.obteneringrediente())
            actual = actual.obtenerSiguienteOrden()
        

        for i in range ( 1 , contador ) :
            dot.edge ( str ( i ) , str ( i + 1 ) )
        
        dot.view()

    


