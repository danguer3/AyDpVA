#Este es un programa de ejemplo
def suma(num1,num2):
    sum= num1 + num2
    return sum
def main():
    x= int(input("Dame el primer numero: "))
    y= int(input("Dame el segundo numero: "))
    sumFinal=suma(x,y)
    print("la suma es: " + str(sumFinal))

x = 4
y = 4
if x > y: 
        print("Hello Word")
elif x ==y: 
        print("Bye Bye")
else:
        print("Im happy")
if __name__ == "__main__":
    main()