import logging as log
import sympy
import math
x,y = sympy.symbols('x,y', real=True)


def calculate_jacobian(functions):
    function = sympy.Matrix(functions)
    return function.jacobian([x, y])

def get_valued_jacobian(matrix, a, b):
    return matrix.subs([(x, a), (y, b)])

def inversed_jacobian(matrix):
   try:
	return matrix.inv()
   except ZeroDivisionError as ex:
	log.error("Error! %s", ex)
        sys.exit(1)

def valued_functions(functions, a, b):
    array_valued_functions = list()
    for function in functions:
	array_valued_functions.append(function.subs([(x, a), (y, b)]))
    return array_valued_functions
    	
def netwon_formula(functions, a, b):
    j_matrix = calculate_jacobian(functions)
    jac_valued = get_valued_jacobian(j_matrix, a, b)
    inverse = inversed_jacobian(jac_valued)
    row_matrix = sympy.Matrix([a, b])
    function_matrix = sympy.Matrix(valued_functions(functions, a, b))
    result = row_matrix - inverse*function_matrix
    return result[0, 0], result[1,0]

def main():
    functions = [x+y-x*y+2, x*(math.e)**(-y)-1]
    a, b = 2, 0
    eps = 1.0e-6
    iteration_counter = 0
    f_value = valued_functions(functions, a, b)
    while abs(f_value[0]) > eps and abs(f_value[1]) > eps and iteration_counter < 100:
    	a, b = netwon_formula(functions, a, b)
    	f_value = valued_functions(functions, a, b)
	iteration_counter += 1
    if iteration_counter > 0:    # Solution found
   	 print "Number of function calls: %d" % (1 + 2*iteration_counter)
   	 print "A solution is: %f %f" % (a, b)
    else:
    	print "Solution not found!"

if __name__ == '__main__':
    main()
