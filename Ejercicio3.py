print("Este programa determina si dos numeros son iguales o diferentes ")

a=int(input("Escriba el primer numero :"))
b=int(input("Escriba el segundo numero : "))

if a == b :
    x=" es completamente igual a"
else :
    x= "No es igual a "
print("{0} {1} {2} ".format(a,x,b))
