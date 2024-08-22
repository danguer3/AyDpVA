##PRACTICA 1.1 
##Algoritmos y dispositivos de vehiculos antonomos
## CALCULADORA PYTHON 
#EMMANUEL PEREZ RANGEL
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
         print("No es posible la division")
    else:
        divid=num1/num2
    return divid

def potencia(num1,num2):
     pot=num1**num2
     return pot

def modulo(num1,num2):
    mod=num1 % num2 
    return mod  

import math
def raiz(num1):
    if num1<0:
       print("No es posible calcular la raiz de un numero negativo")
    else:
        rz=math.sqrt(num1)
    return rz 

def calculadora ():

    print("Operaciones aritmeticas")
    print("1. suma ")
    print("2. resta ") 
    print("3. multiplicacion ")
    print("4. Division")
    print("5. Modulo")
    print("6. Potencia")
    print("7. Raiz cuadrada")

operator= int(input("Ingrese la operacion que desea realizar: "))
x= float(input("Dame el primer numero: "))
y= float(input("Dame el segundo numero: "))

def operations(operator, x,y):

    if operator==1:
        SumFinal= suma(x,y)
        print("Resultado: " + (SumFinal))
    elif operator==2: 
        ResFinal=resta(x,y)
        print("Resultado: "+ (ResFinal))
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
     

if __name__ == "__main__":
    calculadora()