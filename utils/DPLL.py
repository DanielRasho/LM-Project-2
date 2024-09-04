def parse_clauses(clauses):
    literal_map = {}  # Diccionario para mapear literales a identificadores
    literal_counter = 1  # Contador para asignar identificadores a los literales

    parsed_clauses = []  # Lista para almacenar las cláusulas parseadas
    for clause in clauses:
        parsed_clause = set()  # Conjunto para almacenar los literales de una cláusula parseada
        for literal in clause:
            if literal.startswith('-'):  # Si el literal comienza con '-', es negativo
                var = literal[1:]  # Obtenemos el nombre de la variable sin el '-'
                sign = -1  # Asignamos el signo negativo
            else:
                var = literal
                sign = 1  # Asignamos el signo positivo

            if var not in literal_map:  # Si la variable no está en el mapa de literales
                literal_map[var] = literal_counter  # Asignamos un identificador único a la variable
                literal_counter += 1

            parsed_clause.add(sign * literal_map[var])  # Añadimos el literal parseado al conjunto

        parsed_clauses.append(parsed_clause)  # Añadimos la cláusula parseada a la lista

    return parsed_clauses, literal_map


def dpll(clauses, assignment):
    if not clauses:  # Si no quedan cláusulas, la fórmula es satisfacible
        return True, {var: (val if val else False) for var, val in assignment.items()}

    if any(not clause for clause in clauses):  # Si hay una cláusula vacía, la fórmula es insatisfacible
        return False, None

    unassigned_vars = {literal for clause in clauses for literal in clause if abs(literal) not in assignment}

    if not unassigned_vars:  # Si no quedan variables sin asignar, la fórmula es satisfacible
        return True, {var: (val if val else False) for var, val in assignment.items()}

    literal = next(iter(unassigned_vars))  # Tomamos el primer literal sin asignar

    for boolean in [True, False]:  # Probamos asignar el literal a True y a False
        new_assignment = assignment.copy()  # Creamos una copia de la asignación actual
        new_assignment[abs(literal)] = boolean if literal > 0 else not boolean  # Asignamos el valor correspondiente

        new_clauses = []
        for clause in clauses:
            if literal not in clause and -literal not in clause:  # Si el literal no está en la cláusula
                new_clauses.append(clause)  # Mantenemos la cláusula sin cambios
            elif literal in clause:  # Si el literal está en la cláusula
                continue  # Saltamos a la siguiente cláusula
            else:  # Si el literal negado está en la cláusula
                new_clause = {l for l in clause if l != -literal}  # Eliminamos el literal negado de la cláusula
                if not new_clause:  # Si la cláusula se vuelve vacía, la fórmula es insatisfacible
                    break
                new_clauses.append(new_clause)  # Añadimos la cláusula modificada a la lista de cláusulas

        else:  # Si no se rompe el bucle, llamamos recursivamente a DPLL con las cláusulas modificadas
            result, final_assignment = dpll(new_clauses, new_assignment)
            if result:  # Si la fórmula es satisfacible
                return True, final_assignment

    return False, None  # Si no se encuentra una asignación satisfacible, la fórmula es insatisfacible


def main():
    input_clauses = [{"q", "p", "-p"}, {"-q", "-p", "p"}]
    ## [{"q","p"}]
    parsed_clauses, literal_map = parse_clauses(input_clauses)
    result, assignment = dpll(parsed_clauses, {})

    if result:  # Si la fórmula es satisfacible
        readable_assignment = {var: assignment.get(id, "Indeterminado") for var, id in literal_map.items()}
        print("Satisfacible con la siguiente asignación:", readable_assignment)
    else:  # Si la fórmula es insatisfacible
        print("Insatisfacible.")


main()
