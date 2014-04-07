#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from numpy import *
from sympy import Symbol



def montar_matriz(lista_matrices_rigidez):
    """
    Esta función ensambla un Matriz de rigidez K
    a partir de lista_matrices_rigidez ,que contiene
    las matrices de rigidez k de cada   elemento

    

    Example:
    
        In [1]: import numpy as np
                from fem import montar_matriz

        In [2]: a=np.asmatriz((1,-1),(-1,1))

        Out[2]: matrix([[ 1, -1],
                        [-1,  1]])

        In [3]: lista=(a,2*a,3*a,4*a,5*a)
                lista

        Out[3]: (matrix([[ 1, -1],
                        [-1,  1]]),
                 matrix([[ 2, -2],
                        [-2,  2]]),
                 matrix([[ 3, -3],
                        [-3,  3]]),
                 matrix([[ 4, -4],
                        [-4,  4]]),
                 matrix([[ 5, -5],
                        [-5,  5]]))

        In [4]: K=montar_matriz(lista)
                K

        Out[4]: matrix([[ 1., -1.,  0.,  0.,  0.,  0.],
                        [-1.,  3., -2.,  0.,  0.,  0.],
                        [ 0., -2.,  5., -3.,  0.,  0.],
                        [ 0.,  0., -3.,  7., -4.,  0.],
                        [ 0.,  0.,  0., -4.,  9., -5.],
                        [ 0.,  0.,  0.,  0., -5.,  5.]])
    """
    #Aquí se establecen todas las variables
    ################################################
    A=lista_matrices_rigidez 
    num_ele=len(A)
    K=zeros((num_ele+1,num_ele+1))
    n=num_ele
    ################################################

    #Se ensambla la matriz
    ################################################
    for i in range(n):
        j=2
        K[i:i+j,i:i+j]=A[i]
    ################################################


    #Se suman los valores de conectividad 
    ################################################
    for i in range(n):
        for j in range(n):
            if i==j:
                if i!=0:
                    if i!=(n):
                        K[i,j]=A[i-1][1,1]+A[i][0,0]
    ################################################
    return asmatrix(K)