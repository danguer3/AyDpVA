##PRACTICA 1.1 
##Algoritmos y dispositivos para Vehiculos Antonomos
## CALCULADORA 
#EMMANUEL PEREZ RANGEL
import math

def suma(num1,num2):
    sum=num1+num2
    return sum

def resta(num1,num2):
    res=num1-num2
    return res

def multiplicacion(num1,num2):
    multi=num1*num2
    return multi

def division(num1,num2):
    if num2==0:
         print("No es posible la division entre 0")
    else:
        divid=num1/num2
    return divid

def potencia(num1,num2):
     pot=num1**num2
     return pot

def modulo(num1,num2):
    mod=num1 % num2 
    return mod  

def raiz(num1):
    if num1<0:
       print("No es posible calcular la raiz de un numero negativo")
    else:
        rz=math.sqrt(num1)
    return rz 

def calculadora ():
    while(True):
        print("Operaciones Disponibles")
        print("1. Suma ")
        print("2. Resta ") 
        print("3. Multiplicacion ")
        print("4. Division")
        print("5. Modulo")
        print("6. Potencia")
        print("7. Raiz cuadrada")
        print("8. Salir")

        operator= int(input("Ingrese la operacion que desea realizar: "))
        x= float(input("Ingrese el primer numero: "))
        y= float(input("Ingrese el segundo numero: "))

        if operator==1:
                SumFinal= suma(x,y)
                print("Resultado: " + str(SumFinal))
        elif operator==2: 
                ResFinal=resta(x,y)
                print("Resultado: "+ str(ResFinal))
        elif operator==3:
            MultiFinal= multiplicacion(x,y)
            print("Resultado:" + str(MultiFinal))
        elif operator==4:
            DivFinal= division(x,y)
            print("Resultado: "+ str(DivFinal))
        elif operator ==5: 
            ModFinal= modulo(x,y)
            print("Modulo: "+ str(ModFinal))
        elif operator ==6:
            PotFinal=potencia(x,y)
            print("Resultado: " + str(PotFinal))
        elif operator==7:
            RaizFinal=raiz(x)
            print("resultado: " + str(RaizFinal))
        else:
            break

     

if __name__ == "__main__":
    calculadora()