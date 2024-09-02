def parse_clauses(clauses):
    literal_map = {}
    literal_counter = 1

    parsed_clauses = []
    for clause in clauses:
        parsed_clause = set()
        for literal in clause:
            if literal.startswith('-'):
                var = literal[1:]
                sign = -1
            else:
                var = literal
                sign = 1

            if var not in literal_map:
                literal_map[var] = literal_counter
                literal_counter += 1

            parsed_clause.add(sign * literal_map[var])

        parsed_clauses.append(parsed_clause)

    return parsed_clauses, literal_map

def dpll(clauses, assignment):
    if not clauses:
        return True, {var: (val if val else False) for var, val in assignment.items()}
    
    if any(not clause for clause in clauses):
        return False, None

    unassigned_vars = {literal for clause in clauses for literal in clause if abs(literal) not in assignment}

    if not unassigned_vars:
        return True, {var: (val if val else False) for var, val in assignment.items()}

    literal = next(iter(unassigned_vars))

    for boolean in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[abs(literal)] = boolean if literal > 0 else not boolean

        new_clauses = []
        for clause in clauses:
            if literal not in clause and -literal not in clause:
                new_clauses.append(clause)
            elif literal in clause:
                continue
            else:
                new_clause = {l for l in clause if l != -literal}
                if not new_clause:
                    break
                new_clauses.append(new_clause)
        else:
            result, final_assignment = dpll(new_clauses, new_assignment)
            if result:
                return True, final_assignment

    return False, None

def main():
    input_clauses = [{"q","p", "-p"}]
    ## [{"q","p"}]
    parsed_clauses, literal_map = parse_clauses(input_clauses)
    result, assignment = dpll(parsed_clauses, {})

    if result:
        readable_assignment = {var: assignment.get(id, "undetermined") for var, id in literal_map.items()}
        print("Satisfiable with assignment:", readable_assignment)
    else:
        print("Unsatisfiable")
