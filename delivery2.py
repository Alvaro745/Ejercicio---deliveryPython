class persona:
    def __init__(self):
        self.nombre = []
        self.apellido = []
        self.telefono = []
        self.carnet = []

class usuario(persona):
    def __init__(self):
        persona.__init__(self)
        self.email = []
        self.password = []
    
class tipoVehiculo:
    def __init__(self):
        self.tipoVehiculo = []

class marca:
    def __init__(self):
        self.marca = []
        self.procedencia = []

class vehiculo(tipoVehiculo, marca):
    def __init__(self):
        tipoVehiculo.__init__(self)
        marca.__init__(self)
        self.placa = []
        self.cilindrada = []

class conductor(usuario, vehiculo):
    def __init__(self):
        usuario.__init__(self)
        vehiculo.__init__(self)
        self.tipoLicencia = []
        self.estado = []

    def menu(self):
        print("""
           ********MENU DE REGISTRO DE CONDUCTOR*******
           1.-REGISTRAR CONDUCTOR
           2.-MOSTRAR LISTADO DE CONDUCTORES HABILITADOS
           3.-MOSTRAR LISTADO DE CONDUCTORES DESHABILITADOS
           4.-DESHABILITAR CONDUCTOR
           5.-HABILITAR CONDUCTOR
           6.-MODIFICAR CONDUCTOR
           7.-SALIR
        """)

        eleccion = int(input("Seleccione una opcion: \n"))
        if eleccion == 1:
            print(self.registrarConduc())
            self.menu()
        elif eleccion == 2:
            print(self.verConducAlta())
            self.menu()
        elif eleccion == 3:
            print(self.verConducBaja())
            self.menu()
        elif eleccion == 4:
            print(self.deshabilitarConduc())
            self.menu()
        elif eleccion == 5:
            print(self.habilitarConduc())
            self.menu()
        elif eleccion == 6:
            print(self.modificarDatos())
            self.menu()
        elif eleccion == 7:
            print("Gracias por utilizar el sistema")
        else:
            print("Seleccione una opcion valida")
            self.menu()
    
    def registrarConduc(self):
        nombre = input("Nombre del conductor: \n")
        apellido = input("Apellido del conductor: \n")
        telefono = input("Telefono del conductor: \n")
        carnet = input("Carnet del conductor: \n")
        email = input("Email del conductor: \n")
        password = input("Contraseña para el usuario del Conductor: \n")
        tipoVehiculo = input("Tipo de Vehiculo del conductor: \n")
        marca = input("Marca del Vehiculo del conductor: \n")
        procedencia = input("Procedencia del Vehiculo: \n")
        placa = input("Placa del Vehiculo: \n")
        cilindrada = input("Cilindrada del Vehiculo: \n")
        tipoLicencia = input("Tipo de licencia del conductor: \n")
        print(self.guardarConduc(nombre, apellido, telefono, carnet, email, password, tipoVehiculo, marca, procedencia, placa, cilindrada, tipoLicencia))
        agregarOtro=input("Desea agregar mas registros? s/n \n")
        if agregarOtro == 's' or agregarOtro =='S':
            self.registrarConduc()
        return 'Conductores registrados correctamente.!'
    
    def guardarConduc(self, nombre, apellido, telefono, carnet, email, password, tipoVehiculo, marca, procedencia, placa, cilindrada, tipoLicencia):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.telefono.append(telefono)
        self.carnet.append(carnet)
        self.email.append(email)
        self.password.append(password)
        self.tipoVehiculo.append(tipoVehiculo)
        self.marca.append(marca)
        self.procedencia.append(procedencia)
        self.placa.append(placa)
        self.cilindrada.append(cilindrada)
        self.tipoLicencia.append(tipoLicencia)
        self.estado.append(1)
        return 'El conductor {} fue registrado exitosamente..!!'.format(nombre)

    def buscarConduc(self, estado):
        print(self.BaseDatosConduc(estado))
        eleccion = input("Digite el nombre del Conductor: \n")
        posicion = self.nombre.index(eleccion)
        self.BaseDatosConduc(posicion)
        return posicion

    def deshabilitarConduc(self):
        print("*****DESHABILITAR CONDUCTOR*******")
        posicion = self.buscarConduc(1)
        return self.darBaja(posicion)
    
    def darBaja(self, posicion):
        self.estado[posicion] = 0
        return "El Conductor {} esta Deshabilitado..!!".format(self.nombre[posicion])
    
    def habilitarConduc(self):
        print("*****HABILITAR CONDUCTOR*******")
        posicion = self.buscarConduc(0)
        return self.darAlta(posicion)
    
    def darAlta(self, posicion):
        self.estado[posicion] = 1
        return "El Conductor {} esta Habilitado..!!".format(self.nombre[posicion])

    def verConducAlta(self):
        return self.BaseDatosConduc(1)

    def verConducBaja(self):
        return self.BaseDatosConduc(0)

    def BaseDatosConduc(self, estado):
        if(self.nombre):
            for i in range(len(self.nombre)):
                self.detalleConduc(i, estado)
            return "Base de datos Cargado Correctamente"
        else:
            return "TODAVIA NO SE AGREGARON REGISTROS A LA BASE DE DATOS"

    def detalleConduc(self, posicion, estado):
        if(self.estado[posicion] == estado):
            print("NOMBRE: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
            print("TELEFONO: {}".format(self.telefono[posicion]))
            print("CARNET: {}".format(self.carnet[posicion]))
            print("EMAIL: {}".format(self.email[posicion]))
            print("TIPO DE VEHICULO: {}".format(self.tipoVehiculo[posicion]))
            print("MARCA: {}".format(self.marca[posicion]))
            print("TIPO DE LICENCIA: {}".format(self.tipoLicencia[posicion]))
            print("ESTADO: {}".format(self.estado[posicion]))
            print("*****************************************")
            pass

    def buscarConductor(self):
        self.BaseDatosConduc(1)
        print("-------------------------------")
        editar = input("Digite el nombre del conductor a modificar: \n")
        posicion = self.nombre.index(editar)
        self.BaseDatosConduc(posicion)
        return posicion

    def modificarDatos(self):
        posicion = self.buscarConductor()
        dato = input("Desea modificar el Nombre?: s/n \n")
        datoActual = self.nombre[posicion]
        nombre = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el Apellido?: s/n \n")
        datoActual = self.apellido[posicion]
        apellido = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el Telefono?: s/n \n")
        datoActual = self.telefono[posicion]
        telefono = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el Carnet?: s/n \n")
        datoActual = self.carnet[posicion]
        carnet = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el Correo Electronico?: s/n \n")
        datoActual = self.email[posicion]
        email = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar la Contraseña de Usuario?: s/n \n")
        datoActual = self.password[posicion]
        password = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el Tipo de Vehiculo?: s/n \n")
        datoActual = self.tipoVehiculo[posicion]
        tipoVehiculo = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar la Marca?: s/n \n")
        datoActual = self.marca[posicion]
        marca = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar la Procedencia?: s/n \n")
        datoActual = self.procedencia[posicion]
        procedencia = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar la Placa?: s/n \n")
        datoActual = self.placa[posicion]
        placa = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar Cilindrada?: s/n \n")
        datoActual = self.cilindrada[posicion]
        cilindrada = self.confirmarEditarStr(dato,datoActual)
        dato = input("Desea modificar el Tipo de Licencia?: s/n \n")
        datoActual = self.tipoLicencia[posicion]
        tipoLicencia = self.confirmarEditarStr(dato,datoActual)
        self.guardarModificacion(posicion,nombre,apellido,telefono,carnet,email,password,tipoVehiculo,marca,procedencia,placa,cilindrada,tipoLicencia)
        self.otros()

    def confirmarEditarStr(self,dato,datoActual):
        if(dato == 's' or dato == 'S'):
            nuevo = input("Ingrese el nuevo dato: \n")
            return nuevo
        elif(dato == 'n' or dato == 'N'):
            actual = datoActual
            return actual
        else:
            print("** Seleccion erronea.!!! Regresando al menu Modificar Conductor")
            self.menu()
    
    def guardarModificacion(self, posicion, nombre, apellido, telefono, carnet, email, password, tipoVehiculo, marca, procedencia, placa, cilindrada, tipolicencia):
        self.nombre[posicion] = nombre
        self.apellido[posicion] = apellido
        self.telefono[posicion] = telefono
        self.carnet[posicion] = carnet
        self.email[posicion] = email
        self.password[posicion] = password
        self.tipoVehiculo[posicion] = tipoVehiculo
        self.marca[posicion] = marca
        self.procedencia[posicion] = procedencia
        self.placa[posicion] = placa
        self.cilindrada[posicion] = cilindrada
        self.tipoLicencia[posicion] = tipolicencia
        return "** Actualizado correctamente.!!! **"
    
    def otros(self):
        otro = input("Desea modificar los datos de otro Conductor? s/n \n")
        if (otro == "s" or otro == "S"):
            self.editar()
        if (otro == "n" or otro == "N"):
            return self.menu()

conductores = conductor()
conductores.menu()
