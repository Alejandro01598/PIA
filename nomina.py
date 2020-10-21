class Nomina_e:
    def __init__(self,idEmpleado,Nombre,Sueldoh,Horas):
        self.__idEmpleado = idEmpleado
        self.__Nombre = Nombre
        self.__Sueldoh = Sueldoh 
        self.__Horas = Horas

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
    def Sueldoh(self,valor):
        self.__Sueldoh=valor

    @property
    def Horas (self):
        return self.__Horas

    @Horas.setter
    def Horas(self,valor):
        self.__Horas=valor

    def total(self):
        Deduccion =0
        sueldo=(self.__Horas * self.__Sueldoh)
        Horasextra= (self.__Horas-8)
        sueldo1=((Horasextras*self.__Sueldoh)* 2
        sueldototal = sueldo + sueldo1
        if (sueldototal >= 3000):
            Deduccion = (sueldototal * .07)
        else:
            Deduccion = (sueldototal * .035)
        return sueldototal

    def sueldoneto(self):
        print("Sueldo Total =" +sueldototal)
        print("Sueldo neto ="(Sueldototal - Deduccion))




print ("-------DATOS DE EMPLEADOS------")
idEmpleado=input("Ingresa el ID del empleado\n")
Nombre =input("Ingresa el nombre del empleado\n")
Sueldoxh= input("Ingresa el sueldo por horas\n")
Horas=input("Ingresa las horas\n")
print ("----Resultados----\n" )



r=Nomina_e(idEmpleado,Nombre,Sueldoxh,Horas)
r.sueldoneto()