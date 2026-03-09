def main():
    '''Crea una función que reciba: nombre, edad y correo. El programa debe hacer
las siguientes validaciones:
• Nombre mínimo 3 caracteres
• Edad (entre 0 y 120)
• Correo debe contener @, .com, edu.co,
Si algún dato es inválido, debe generar un mensaje claro y volver a pedir el dato.
Posteriormente almacene dicha información en una lista.'''
    datos_usuario = []
    
    while True:
        nombre = input("Ingrese su nombre (mínimo 3 caracteres): ")
        if len(nombre) < 3:
            print("Error: El nombre debe tener al menos 3 caracteres.")
            continue
        
        try:
            edad = int(input("Ingrese su edad (entre 0 y 120): "))
            if edad < 0 or edad > 120:
                print("Error: La edad debe estar entre 0 y 120.")
                continue
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            continue
        
        correo = input("Ingrese su correo electrónico (debe contener @, .com, edu.co): ")
        if '@' not in correo or ('.com' not in correo and '.edu.co' not in correo):
            print("Error: El correo debe contener '@' y terminar con '.com' o '.edu.co'.")
            continue
        
        datos_usuario.append({'nombre': nombre, 'edad': edad, 'correo': correo})
        print("Datos almacenados correctamente.")
        break

    print("Información del usuario:", datos_usuario)

if __name__ == "__main__":
    main()