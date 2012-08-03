while True:
    try:
        peso = float(raw_input("Digite su peso en kilogramos: "))
        if peso > 0:
            break
        else:
            print "Dato invalido, Por favor digite un numero positivo.\n"
    except ValueError:
        print "Dato invalido, Por favor digite un numero positivo.\n"

while True:
    try:
        estatura = float(raw_input("Digite su estatura en metros: "))
        if estatura > 0:
            break
        else:
            print "Dato invalido, Por favor digite un numero positivo.\n"
    except ValueError:
        print "Dato invalido, Por favor digite un numero positivo.\n"

imc = peso / (estatura * estatura)
print "\nSu IMC es de: " + str(imc)

if imc < 16:
    print "Usted tiene delgadez extrema"
elif imc < 17:
    print "Usted tiene delgadez moderada"
elif imc < 18.5:
    print "Usted tiene delgadez aceptable"
elif imc < 25:
    print "Usted tiene un peso adecuado"
elif imc < 30:
    print "Usted tiene sobrepeso"
elif imc < 35:
    print "Usted tiene obesidad tipo I"
elif imc < 40:
    print "Usted tiene obesidad tipo II"
else:
    print "Usted tiene obesidad tipo III"
    
    
    





