# LM-Project-2

## Descripción

Este proyecto implementa y compara dos algoritmos para resolver problemas de satisfacibilidad booleana (SAT):

1. **Fuerza Bruta**: Un enfoque exhaustivo que prueba todas las posibles asignaciones de verdad para determinar si una fórmula en forma normal conjuntiva (CNF) es satisfacible.
2. **DPLL (Davis-Putnam-Logemann-Loveland)**: Un algoritmo más eficiente que utiliza técnicas de reducción y búsqueda para determinar la satisfacibilidad de una fórmula en CNF.

## Funcionalidades

- **Generación de Cláusulas**: Genera fórmulas aleatorias en CNF con un número especificado de variables y cláusulas.
- **Conversión de Fórmulas**: Convierte fórmulas con nombres de variables a una representación numérica.
- **Verificación de Satisfacibilidad**: Verifica si una fórmula en CNF es satisfacible utilizando fuerza bruta o el algoritmo DPLL.
- **Comparación de Tiempos de Ejecución**: Compara los tiempos de ejecución de los algoritmos de fuerza bruta y DPLL para diferentes tamaños de problemas.
- **Visualización de Resultados**: Genera gráficos que muestran la comparación de tiempos de ejecución entre los dos algoritmos.

## Uso

1. **Generar y Convertir Fórmulas**:

   - Utiliza `generate_clauses` para generar fórmulas aleatorias.
   - Usa `convert_formula` para convertir las fórmulas generadas a una representación numérica.

2. **Verificar Satisfacibilidad**:

   - Usa `is_satisfiable` para verificar la satisfacibilidad de una fórmula utilizando fuerza bruta.
   - Usa `dpll` para verificar la satisfacibilidad de una fórmula utilizando el algoritmo DPLL.

3. **Comparar Tiempos de Ejecución**:

   - Ejecuta `run_tests` para comparar los tiempos de ejecución de los dos algoritmos.
   - Usa `plot_results` para visualizar los resultados de la comparación.

4. **Ejecutar el Programa Principal**:
   - Ejecuta el archivo `main.py` para realizar todas las pruebas y generar los gráficos de comparación.

## Ejemplo de Ejecución

Para ejecutar el programa principal y ver la comparación de tiempos de ejecución, simplemente ejecuta:

```sh
python main.py
```
