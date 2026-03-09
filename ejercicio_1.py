def main():
    estudiantes = [
        {
            'nombre': 'Elkin',
            'edad': 19,
            'estado': 'activo',
            'materias': ['Calculo', 'programacion_avanzada', 'Metodo'],
            'notas': {'Calculo': 4.5, 'programacion_avanzada': 3.0, 'Metodo': 2.5}
        },
        {
            'nombre': 'Anyelo',
            'edad': 19,
            'estado': 'activo',
            'materias': ['ecuaciones', 'Física', 'base_dato'],
            'notas': {'ecuaciones': 3.5, 'Física': 4.0, 'base_dato': 4.5}
        },
        {
            'nombre': 'sainner',
            'edad': 20,
            'estado': 'activo',
            'materias': ['arquitectura', 'compiladores', 'analisis'],
            'notas': {'arquitectura': 3.5, 'compiladores': 4.0, 'analisis': 4.5}
        }
    ]
    for estudiante in estudiantes:
        nombre = estudiante['nombre']
        notas = estudiante['notas']
        promedio = sum(notas.values()) / len(notas)
        mejor_materia = max(notas, key=notas.get)
        peor_materia = min(notas, key=notas.get)
        estado_aprobacion = 'aprobado' if promedio >= 3.0 else 'reprobado'
        
        print(f'Estudiante: {nombre}')  
        print(f'Promedio general de notas: {promedio:.2f}')
        print(f'Materia con mejor nota: {mejor_materia} ({notas[mejor_materia]})')
        print(f'Materia con peor nota: {peor_materia} ({notas[ peor_materia]})')
        print(f'Estado: {estado_aprobacion}')
        print('-----------------------------')

if __name__ == "__main__":    
    main()
        
  
