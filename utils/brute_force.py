import itertools

# Mapeo de variables a números
# Esto permite convertir nombres de variables (p, q, r) a números (1, 2, 3)
variable_map = {
    'p': 1,
    'q': 2,
    'r': 3
}

# Mapeo inverso para interpretar resultados
# Este diccionario nos permite volver de números a nombres de variables
inverse_variable_map = {v: k for k, v in variable_map.items()}

def convert_formula(formula_with_vars, variable_map):
    """
    Convierte una fórmula booleana dada con nombres de variables
    a una representación numérica utilizando el mapeo de variable_map.
    
    Args:
    formula_with_vars: List[List[str]] - La fórmula en CNF con nombres de variables.
    variable_map: Dict[str, int] - Mapeo de nombres de variables a números.
    
    Returns:
    List[List[int]] - Fórmula en CNF representada con números.
    """
    cnf_formula = []
    for clause in formula_with_vars:
        numeric_clause = []
        for literal in clause:
            var = literal.strip('¬')  # Eliminar la negación si existe
            num = variable_map[var]   # Obtener el número correspondiente a la variable
            if literal.startswith('¬'):
                numeric_clause.append(-num)  # Negar el número si el literal está negado
            else:
                numeric_clause.append(num)
        cnf_formula.append(numeric_clause)
    return cnf_formula

def is_satisfiable(cnf_formula):
    """z
    Verifica si una fórmula en CNF es satisfacible usando fuerza bruta.
    
    Args:
    cnf_formula: List[List[int]] - Fórmula en CNF representada con números.
    
    Returns:
    Tuple[bool, Dict[int, bool]] - Retorna True y la asignación si es satisfacible, 
                                   de lo contrario False y una asignación vacía.
    """
    # Obtener todas las variables involucradas en la fórmula
    variables = {abs(literal) for clause in cnf_formula for literal in clause}
    
    # Generar todas las combinaciones posibles de asignaciones de True/False para las variables
    for assignment in itertools.product([True, False], repeat=len(variables)):
        # Crear un diccionario que asocia cada variable con su valor
        assignment_dict = dict(zip(variables, assignment))
        
        # Evaluar la fórmula con esta asignación
        if evaluate_formula(cnf_formula, assignment_dict):
            return True, assignment_dict
    
    # Si ninguna asignación satisface la fórmula
    return False, {}

def evaluate_formula(cnf_formula, assignment_dict):
    """
    Evalúa una fórmula en CNF bajo una asignación específica de valores de verdad.
    
    Args:
    cnf_formula: List[List[int]] - Fórmula en CNF representada con números.
    assignment_dict: Dict[int, bool] - Asignación de valores a variables.
    
    Returns:
    bool - True si la fórmula es verdadera bajo la asignación dada, False en caso contrario.
    """
    # Iterar sobre cada cláusula en la fórmula
    for clause in cnf_formula:
        clause_satisfied = False
        # Evaluar cada literal en la cláusula
        for literal in clause:
            if literal > 0 and assignment_dict[literal]:  # Literal positivo
                clause_satisfied = True
                break  # La cláusula es verdadera si cualquier literal es verdadero
            elif literal < 0 and not assignment_dict[-literal]:  # Literal negativo
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False  # Si alguna cláusula es falsa, la fórmula es falsa
    return True  # Si todas las cláusulas son verdaderas, la fórmula es verdadera

def interpret_solution(solution_dict, inverse_variable_map):
    """
    Convierte la solución numérica a nombres de variables.
    
    Args:
    solution_dict: Dict[int, bool] - Asignación numérica de valores a variables.
    inverse_variable_map: Dict[int, str] - Mapeo inverso de números a nombres de variables.
    
    Returns:
    Dict[str, bool] - Asignación de valores con nombres de variables.
    """
    interpreted = {}
    for var_num, value in solution_dict.items():
        var_name = inverse_variable_map[var_num]
        interpreted[var_name] = value
    return interpreted

# Definir la fórmula con nombres de variables
# Esta es una fórmula en forma normal conjuntiva (CNF):
# (p ∨ ¬q) ∧ (¬p ∨ r) ∧ (q ∨ r)
formula_with_vars = [
    ['p', '¬q'],
    ['¬p', 'r'],
    ['q', 'r']
]

# Convertir la fórmula a representación numérica
cnf_formula = convert_formula(formula_with_vars, variable_map)
print("Fórmula en CNF numérica:", cnf_formula)

# Verificar si la fórmula es satisfacible
satisfiable, solution_numeric = is_satisfiable(cnf_formula)

if satisfiable:
    solution_interpreted = interpret_solution(solution_numeric, inverse_variable_map)
    print("La fórmula es satisfacible con la siguiente asignación:")
    print(solution_interpreted)
else:
    print("La fórmula es insatisfacible.")
