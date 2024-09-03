import string
import time

from matplotlib import pyplot as plt
from utils.generateClauses import generate_clauses
from utils.brute_force import is_satisfiable, convert_formula, interpret_solution, variable_map, inverse_variable_map
from utils.DPLL import parse_clauses, dpll

variable_map = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
inverse_variable_map = {v: k for k, v in variable_map.items()}

def convert_formula(formula_with_vars, variable_map):
    cnf_formula = []
    for clause in formula_with_vars:
        numeric_clause = []
        for literal in clause:
            var = literal.strip('¬')
            num = variable_map[var]
            if literal.startswith('¬'):
                numeric_clause.append(-num)
            else:
                numeric_clause.append(num)
        cnf_formula.append(numeric_clause)
    return cnf_formula

def run_tests(num_vars_list, num_trials=100):
    results = []
    for num_vars in num_vars_list:
        num_clauses = num_vars * 3
        times_dpll = []
        times_brute = []
        for _ in range(num_trials):
            clauses = generate_clauses(num_vars, num_clauses)
            numeric_clauses = convert_formula(clauses, variable_map)

            start_time = time.time()
            parsed_clauses, _ = parse_clauses([{str(lit) for lit in clause} for clause in clauses])
            dpll(parsed_clauses, {})
            times_dpll.append(time.time() - start_time)

            start_time = time.time()
            is_satisfiable(numeric_clauses)
            times_brute.append(time.time() - start_time)

        results.append((num_vars, sum(times_dpll) / len(times_dpll), sum(times_brute) / len(times_brute)))
    return results

def plot_results(results):
    vars_plotted, times_dpll_plotted, times_brute_plotted = zip(*results)
    plt.figure(figsize=(10, 5))
    plt.plot(vars_plotted, times_dpll_plotted, label='DPLL', marker='o')
    plt.plot(vars_plotted, times_brute_plotted, label='Brute Force', marker='x')
    plt.xlabel('Number of Variables')
    plt.ylabel('Average Time (seconds)')
    plt.title('Comparación de Tiempos de Ejecución de DPLL vs Brute Force')
    plt.legend()
    plt.grid(True)
    plt.show()

num_vars_list = [2, 4, 6, 8, 10]
results = run_tests(num_vars_list)
plot_results(results)
