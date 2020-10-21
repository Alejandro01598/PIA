class Nomina:
    def __init__(self,idEmpleado,Nombre,Sueldoh,Horasd,Horasn,Horase):
        self.__idEmpleado = idEmpleado
        self.__Nombre = Nombre
        self.__Sueldoh = Sueldoh 
        self.__Horasd = Horasd
        self.__Horasn = Horasn
        self.__Horase = Horase

    @property
    def idEmpleado (self):
        return self.__idEmpleado
    
    @idEmpleado.setter
    def idEmpleado(self,valor):
        self.__idEmpleado=valor
   
    @property
    def Nombre (self):
        return self.__Nombre
    
    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre=valor

    @property
    def Sueldoh (self):
        return self.__Sueldoh
    
    @Sueldoh.setter
    def Direccion(self,valor):
        self.__Sueldoh=valor

    @property
    def Horasd (self):
        return self.__Horasd
    
    @Horasd.setter
    def Direccion(self,valor):
        self.__Horasd=valor

    @property
    def Horasn (self):
        return self.__Horasn
    
    @Horasn.setter
    def Horasn(self,valor):
        self.__Horasn=valor

    @property
    def __Horase (self):
        return self.__Horase
    
    @Horase.setter
    def Horase(self,valor):
        self.__Horase=valor


    def Sueldo(self):
       Sueldo
    

    