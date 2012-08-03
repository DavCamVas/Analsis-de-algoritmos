def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print a
        temp = b
        b = a + b
        a = temp
        
while True:
    try:
        n = int(raw_input("Digite la cantidad de numeros que desea ver de la sucesion de fibonacci: "))
        if n > 0:
            break
        else:
            print "Dato invalido, Por favor digite un numero entero positivo.\n"
    except ValueError:
        print "Dato invalido, Por favor digite un numero entero positivo.\n"
        
print "\nLa sucesion es: "
fibonacci(n)

        

