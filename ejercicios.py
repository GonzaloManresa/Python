#Escribe un programa que imprima los números del 1 al 100. Pero para los múltiplos de 3, imprime la palabra "Fizz" en lugar del número, y para los múltiplos de 5, imprime "Buzz". Para los números que son múltiplos de tanto 3 como 5, imprime "FizzBuzz".

for i in range(1,100+1):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif (i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)
        

#Haz un programa que solicite número al usuario hasta que el usuario ingrese 0, en ese caso el programa tiene que calcular la suma de los números ingresados anteriormente y el promedio

suma = 0
contador = 0

while True:
    numero = float(input("Ingresa un número (o 0 para finalizar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"La suma de los números ingresados es: {suma}")
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron números.")
