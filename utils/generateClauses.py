import random

def generate_clauses(num_vars, num_clauses):
    clauses = []
    for _ in range(num_clauses):
        clause = {random.choice(['', '¬']) + chr(97 + random.randint(0, num_vars-1)) for _ in range(random.randint(1, 4))}
        clauses.append(list(clause))
    return clauses
