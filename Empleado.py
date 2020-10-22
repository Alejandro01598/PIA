class Nomina:
    def __init__(self,idempleado,nombre,horas,sueldoh):
        self.__idempleado = idempleado
        self.__nombre = nombre
        self.__horas = horas
        self.__sueldoh = sueldoh

    def mostrarinfo(self):
        print("Nombre del empleado"+str(self.__nombre))
        print("Id del empleado"+str(self.__idempleado))

    def sueldo(self):
        print("Sueldo neto del empleado:"+str(self.__horas * self.__sueldoh))   

id_empleado=int(input("Ingresa el id del empleado: \n"))
nombre=input("Ingrese el nombre: \n")
horas=int(input("Ingresa las horas: \n"))
sueldoh=int(input("Ingresa el sueldo bruto: \n"))

N=Nomina(id_empleado,nombre,horas,sueldoh)
N.mostrarinfo() 
N.sueldo()
 