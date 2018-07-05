#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates the intergral values of given equations using Romberg Functions"""
__author__ = "Deepak Paudel"
__copyright__ = "Copyright 2018"

import time
import numpy as np
import matplotlib.pyplot as plt

def evaluate_function(x):
    """calculate value of a given function for a point"""
    value = 0.2 + 25 * x - 200 * pow(x, 2) + 675 * pow(x, 3) - 900 * pow(x, 4) + 400 * pow(x, 5)
    return value


def summation(initial_range, final_range, n):
    """returns summantion of evaluated functions for a range of points"""
    _sum = 0
    h = calculate_h(initial_range, final_range, n)
    for i in range(int(n-1)):
        _sum += evaluate_function(initial_range + (i+1)*h)
    return _sum


def calculate_h(initial_range, final_range, n):
    """computes the interval h using starting and ending range with number of steps"""
    return (final_range - initial_range)/n


def trapezoid(initial_range, final_range, n):
    """calculates integral value using trapezoid function"""
    h = calculate_h(initial_range, final_range, n)
    final_value = (h/2) * (evaluate_function(initial_range) + 2 * summation(initial_range, final_range, n) +
                           evaluate_function(final_range))
    return final_value


def romberg(initial_range, final_range, nmax, error):
    """calculates the integral value using Romberg function"""
    Q = np.zeros((nmax, nmax), float)
    converged = 0
    i, k, N = 0, 0, 0
    for i in range(0, int(nmax)):
        N = pow(2, i)
        Q[i, 0] = trapezoid(initial_range, final_range, N)
        for k in range(0, i):
            n = k + 2
            Q[i, k+1] = 1.0/(4 ** (n - 1) - 1) * (4 ** (n - 1) * Q[i, k] - Q[i-1, k])
            if i > 0:
                if abs(Q[i, k+1] - Q[i, k]) < error:
                    converged = 1
                    break
    return Q[i, k + 1], N, converged


def graph(x, y):
    """plots the graph of time vs bisectors of ranges"""
    plt.plot(x, y)
    plt.title('Number of bisectors vs time elapsed graph')
    plt.xlabel('No of bisectors')
    plt.ylabel('Time elapsed')
    plt.show()


def calculate_time_spent(initial_range, final_range, nmax, error):
    """computes the time spent for calculating the intergral value using romberg function"""
    start_time = time.time()
    romberg(initial_range, final_range, nmax, error)
    return time.time() - start_time


def main():
    """main"""
    initial_range, final_range, nmax, error = tuple(float(x) for x in raw_input().split())
    y = list()
    for number in range(2, int(nmax)):
        y.append(calculate_time_spent(initial_range, final_range, number, error))
    graph(np.array(range(2, int(nmax))), np.array(y))


if __name__ == '__main__':
    main()
