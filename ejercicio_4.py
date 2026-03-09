def main():
    while True:
        print("bienvenido al programa de desarollo de operaciones ")
        print("1: Ingrese un numero para (determinar si es primo): ")
        print("2: Ingrese un numero para (calcular factorial): ")
        print("3: Ingrese un texto para (contar vocales): ")
        print("0: Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion==1:
            numero=int(input("Ingerese el numero : "))
            if numero<2:
                print("El numero no es primo")  
            else:
                es_primo=True
                for i in range(2, int(numero**0.5)+1):
                    if numero % i == 0:
                        es_primo=False
                        break
                if es_primo:
                    print("El numero es primo")
                else:
                    print("El numero no es primo")
        elif opcion==2:
            numero=int(input("Ingrese el numero para calcular su factorial: "))
            if numero<0:
                print("no se puede obtener el factorial de un numeros negativos")
            elif numero==0 or numero==1:
                print(f"El factorial de {numero} es 1")
            else:
               factorial=1
               for i in range(numero,1,-1):
                   factorial*=i
               print(f"El factorial de {numero} es {factorial}")
        elif opcion==3:
            texto=input("Ingrese un texto para contar las vocales: ")
            vocales="aeiouAEIOU"
            contador=0
            for letra in texto:
                if letra in vocales:
                    contador+=1
            print(f"El numero de vocales en el texto es: {contador}")
        elif opcion==0:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

                
                   



if __name__ == "__main__":
    main()