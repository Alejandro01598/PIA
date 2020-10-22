class Nomina:
    def __init__(self,idempleado,nombre,horasn,horasd,sueldoh,):
        self.__idempleado = idempleado
        self.__nombre = nombre
        self.__horasn = horasn
        self.__horasd = horasd
        self.__sueldoh = sueldoh

    def mostrarinfo(self):
        print("---NOMBRE DEL EMPLEADO---\n"+str(self.__nombre))
        print("---ID DEL EMPLEADO--- \n"+str(self.__idempleado))
        print("HORAS DE DIA \n"+str(self.__horasd))
        print("HORAS NOCTURNAS \n"+str(self.__horasn))

    def sueldo(self):
        totalhoras = (self.__horasd + self.__horasn)
        total = (totalhoras * self.__sueldoh)
        if total >= 1200:
            deduccion = (total * 0.07)
        else:
            deduccion =(total* 0.035)

        print("---EL SUELDO NETO ES--- \n"+str(total-deduccion))   
print("-------NOMINA-------")
id_empleado=int(input("Ingresa el id del empleado: \n"))
nombre=input("Ingrese el nombre: \n")
horasd=int(input("Ingresa las horas diurnas: \n"))
horasn=int(input("Ingresa las horas nocturnas:"))
sueldoh=int(input("Ingresa el el sueldo X hra: \n"))
totalhoras=0
total=0
deduccion=0

N=Nomina(id_empleado,nombre,horasd,horasn,sueldoh)
N.mostrarinfo() 
N.sueldo()
 