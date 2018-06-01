#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates the solutions of simultaneous non-linear equations using Netwon's Method"""
__author__ = "Deepak Paudel"
__copyright__ = "Copyright 2018"

import math
import logging as log
import sys
import sympy

X, Y = sympy.symbols('x, y', real=True)
ERROR = 1.0e-6


def calculate_jacobian(functions):
    """calcualtes the jacobian matrix of given functions"""
    function = sympy.Matrix(functions)
    return function.jacobian([X, Y])


def get_valued_jacobian(matrix, guess_x, guess_y):
    """returns jacobian matrix with given guesses"""
    return matrix.subs([(X, guess_x), (Y, guess_y)])


def inversed_jacobian(matrix):
    """returns inverse of Jacobian Matrix"""
    try:
        return matrix.inv()
    except ZeroDivisionError as ex:
        log.error("Error! %s", ex)
        sys.exit(1)


def valued_functions(functions, guess_x, guess_y):
    """returns list of functional values of the quesses"""
    array_valued_functions = list()
    for function in functions:
        array_valued_functions.append(function.subs([(X, guess_x), (Y, guess_y)]))
    return array_valued_functions


def netwon_formula(functions, guess_x, guess_y):
    """returns new guesses using Netwon's formula"""
    j_matrix = calculate_jacobian(functions)
    jac_valued = get_valued_jacobian(j_matrix, guess_x, guess_y)
    inverse = inversed_jacobian(jac_valued)
    row_matrix = sympy.Matrix([guess_x, guess_y])
    function_matrix = sympy.Matrix(valued_functions(functions, guess_x, guess_y))
    result = row_matrix - inverse*function_matrix
    return result[0, 0], result[1, 0]


def main():
    """main function to calulate the solutions within a given error range"""
    #Enter functions here
    functions = [X+Y-X*Y+2, X*(math.e)**(-Y)-1]
    first_guess, second_guess = 2, 0
    iteration_counter = 0
    f_value = valued_functions(functions, first_guess, second_guess)
    while abs(f_value[0]) > ERROR and abs(f_value[1]) > ERROR and iteration_counter < 100:
        first_guess, second_guess = netwon_formula(functions, first_guess, second_guess)
        f_value = valued_functions(functions, first_guess, second_guess)
    iteration_counter += 1
    if iteration_counter > 0:    # Solution found
        print "Number of Iterations: %d" % (1 + 2*iteration_counter)
        print "A solution is: %f %f" % (first_guess, second_guess)
    else:
        print "Solution not found!"

if __name__ == '__main__':
    main()
