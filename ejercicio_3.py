def main():
   
    inicio = int(input("Ingrese el primer número entero (inicio de la serie): "))
    interacion = int(input("Ingrese el segundo número entero (número de iteraciones): "))

    if interacion < 0:
        print("Error: El número de iteraciones no puede ser negativo.")
        return

    serie_fibonacci = []
    a, b = inicio, inicio
    for _ in range(interacion):
        serie_fibonacci.append(a)
        siguiente = a + b
        a=b
        b=siguiente

    print(f"Serie Fibonacci generada: {serie_fibonacci}")
    print(f"Número de términos generados: {len(serie_fibonacci)}")
    print(f"Último valor incluido: {serie_fibonacci[-1]}")

if __name__ == "__main__":
    main()