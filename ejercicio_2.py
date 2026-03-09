def main():
 valor_monetario=float(input("digite valor monetario :"))
 impuesto=valor_monetario*0.16
 if valor_monetario>=200000:
  descuento=valor_monetario*0.10
 else:
    descuento=0 
    total=valor_monetario+impuesto-descuento
    print("el valor del impuesto es:",impuesto)
    print("el valor del descuento es:",descuento)
    print("el valor total a pagar es:",total)
  

if __name__ == "__main__":
    main()