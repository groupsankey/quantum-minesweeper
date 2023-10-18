# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:50:14 2022
"""

import pygame
import time
import random
import json
import math

"""
Qiskit
"""
import numpy as np
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, execute, transpile, QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
    
def rastgele():

    # Loading your IBM Quantum account(s)
    print('Libraries imported successfully!')
    
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.x(0)
    qc.measure(0,0)
    print(qc)
    backend = Aer.get_backend('qasm_simulator') # Choosing the simulator we want to use
    job = execute(qc, backend, shots = 1024) # Running the simulator - specifying the circuit we want to simulate and the number of times we want to simulate it (shots)
    result = job.result()
    counts = result.get_counts() # Getting the counts of 0 and 1 from the result
    plot_histogram(counts)
    print(counts)
    
    coundDeger = str(counts)
    coundDeger = coundDeger.replace("'", " ")
    coundDeger = coundDeger.replace(",", " ")
    coundDeger = coundDeger.replace("}", " ")
    first_word = coundDeger.split()[1]
    print("Deger: ", first_word)
    print(coundDeger)
    xDeger = coundDeger.split()[3]
    yDeger = coundDeger.split()[6]
    xDegerXE = int(xDeger)
    yDegerYE = int(yDeger)
    
    
    valueX = random.randint(0, 512)
    
    while True:
        if valueX%32 != 0:
            valueX= valueX+1
        else:
            break
    
    valueY = random.randint(0, 512)
    
    while True:
        if valueY%32 != 0:
            valueY= valueY+1
        else:
            break
    
    xDegerX = valueX
    yDegerY = valueY
    
    Test = 54
    while True:
        if Test%32 != 0:
            Test= Test+1
        else:
            break
        
    print(Test)
    print("DegerX: ", xDegerX)
    print("DegerY: ", yDegerY)
    type(qc)
     
    """
    Qiskit Bitti / JSON
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('\nGrovers Algorithm')
    print('------------------\n')
    
    
    grid_konumu = 0
    
    
    
    brid=[[0]*16]*16
    y = xDegerX
    x = yDegerY
    #mayin = T[x][y]
    a = f"{x//4}"
    b = f"{y//4}"
    
    a_int = int(a)
    b_int = int(b)
    
    z = a_int*4 +b_int
    grid_konumu = z
    
    print(grid_konumu)
            
    pi = math.pi
    q = QuantumRegister(4,'q')
    c = ClassicalRegister(4,'c')
    qc = QuantumCircuit(q,c)
    
    print('\nInitialising Circuit...\n')
    
    ### Initialisation ###
    
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.h(q[3])
    
    print('\nPreparing Oracle circuit....\n')
    
    ### 0000 Oracle ###
    
    if(grid_konumu == 0):
        qc.x(q[0])
        qc.x(q[1])
        qc.x(q[2])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
    
        qc.x(q[0])
        qc.x(q[1])
        qc.x(q[2])
        qc.x(q[3])
    
    ### 0001 Oracle ###
    
        
    if(grid_konumu == 1):
    
        qc.x(q[1])
        qc.x(q[2])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[1])
        qc.x(q[2])
        qc.x(q[3])
    
    
    
    ### 0010 Oracle ###
    if(grid_konumu == 2):
        qc.x(q[0])
        qc.x(q[2])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
        qc.x(q[2])
        qc.x(q[3])
    
    
    
    ### 0011 Oracle ###
    if(grid_konumu == 3):
        qc.x(q[2])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[2])
        qc.x(q[3])
    
    
    
    ### 0100 Oracle ###
    if(grid_konumu == 4):
        qc.x(q[0])
        qc.x(q[1])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
        qc.x(q[1])
        qc.x(q[3])
    
    
    
    ### 0101 Oracle ###
    if(grid_konumu == 5):
        qc.x(q[1])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[1])
        qc.x(q[3])
    
    
    
    ### 0110 Oracle ###
    if(grid_konumu == 6):
        qc.x(q[0])
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
        qc.x(q[3])
    
    
    
    ### 0111 Oracle ###
    if(grid_konumu == 7):
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[3])
    
    
    ### 1000 Oracle ###
    if(grid_konumu == 8):
        qc.x(q[0])
        qc.x(q[1])
        qc.x(q[2])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
        qc.x(q[1])
        qc.x(q[2])
    
    
    
    ### 1001 Oracle ###
    if(grid_konumu == 9):
        qc.x(q[1])
        qc.x(q[2])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[1])
        qc.x(q[2])
    
    
    
    ### 1010 Oracle ###
    if(grid_konumu == 10):
        qc.x(q[0])
        qc.x(q[2])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
        qc.x(q[2])
    
    
    
    ### 1011 Oracle ###
    if(grid_konumu == 11):
        qc.x(q[3])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[3])
    
    
    
    ### 1100 Oracle ###
    if(grid_konumu == 12):
        qc.x(q[0])
        qc.x(q[1])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
        qc.x(q[1])
    
    
    ### 1101 Oracle ###
    if(grid_konumu == 13):
        qc.x(q[1])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[1])
        print("aaaaaaaaaaaaaaaa")
    
    
    ### 1110 Oracle ###
    if(grid_konumu == 14):
        qc.x(q[0])
    
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
        qc.x(q[0])
    
    
    
    ###1111 Oracle###
    if(grid_konumu == 15):
        qc.cp(pi/4, q[0], q[3])
        qc.cx(q[0], q[1])
        qc.cp(-pi/4, q[1], q[3])
        qc.cx(q[0], q[1])
        qc.cp(pi/4, q[1], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
        qc.cx(q[1], q[2])
        qc.cp(-pi/4, q[2], q[3])
        qc.cx(q[0], q[2])
        qc.cp(pi/4, q[2], q[3])
    
    
    print('\nPreparing Amplification circuit....\n')
    #### Amplification ####
    
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.h(q[3])
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.x(q[3])
    
    qc.cp(pi/4, q[0], q[3])
    qc.cx(q[0], q[1])
    qc.cp(-pi/4, q[1], q[3])
    qc.cx(q[0], q[1])
    qc.cp(pi/4, q[1], q[3])
    qc.cx(q[1], q[2])
    qc.cp(-pi/4, q[2], q[3])
    qc.cx(q[0], q[2])
    qc.cp(pi/4, q[2], q[3])
    qc.cx(q[1], q[2])
    
    qc.cp(-pi/4, q[2], q[3])
    qc.cx(q[0], q[2])
    qc.cp(pi/4, q[2], q[3])
    
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.x(q[3])
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.h(q[3])
    
    ### Measurment ###
    qc.barrier(q)
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    qc.measure(q[2], c[2])
    qc.measure(q[3], c[3])
    
    backend = Aer.get_backend('qasm_simulator')
    print('\nExecuting job....\n')
    job = execute(qc, backend, shots=250)
    
    result = job.result()
    counts = result.get_counts(qc)
    
    coundDeger = str(counts)
    coundDeger = coundDeger.replace("'", " ")
    coundDeger = coundDeger.replace("{", " ")
    coundDeger = coundDeger.replace(":", " ")
    
    
    coundDeger = coundDeger.replace(",", " ")
    coundDeger = coundDeger.replace("}", " ")
    print(coundDeger)
    
            
            
    grids = ["0000","0001","0010","0100","1000","0011","0101","1001","0110","1010","1100","0111","1011","1101","1110","1111"]
    grids_count = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
    
    
    
    
    # Bubble sort in Python
    
    
    ali=max(counts,key=lambda x:counts[x])
    print(20*"-")
    print(int(ali,2))
    print(20*"-")
    print(max(counts,key=lambda x:counts[x]))
    print(20*"-")
    print('RESULT: ',counts,'\n')
    print('Press any key to close')
    
    
    buyuk_x = x%4 
    buyuk_y = y%4 
    
    q1 = QuantumRegister(4,'q')
    c1 = ClassicalRegister(4,'c')
    qc1 = QuantumCircuit(q1,c1)
    
    
    z = (buyuk_x)*4 + buyuk_y
    grid_konumu = z
    
    
    print(grid_konumu)
    
    qc1.h(q1[0])
    qc1.h(q1[1])
    qc1.h(q1[2])
    qc1.h(q1[3])
    
    
    if(grid_konumu == 0):
        qc1.x(q1[0])
        qc1.x(q1[1])
        qc1.x(q1[2])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
    
        qc1.x(q1[0])
        qc1.x(q1[1])
        qc1.x(q1[2])
        qc1.x(q1[3])
    
    ### 0001 Oracle ###
    
        
    if(grid_konumu == 1):
    
        qc1.x(q1[1])
        qc1.x(q1[2])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[1])
        qc1.x(q1[2])
        qc1.x(q1[3])
    
    
    
    ### 0010 Oracle ###
    if(grid_konumu == 2):
        print("AAAAAAAAAAAAAAAAAAAAA")
        qc1.x(q1[0])
        qc1.x(q1[2])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
        qc1.x(q1[2])
        qc1.x(q1[3])
    
    
    
    ### 0011 Oracle ###
    if(grid_konumu == 3):
        qc1.x(q1[2])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[2])
        qc1.x(q1[3])
    
    
    
    ### 0100 Oracle ###
    if(grid_konumu == 4):
        qc1.x(q1[0])
        qc1.x(q1[1])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
        qc1.x(q1[1])
        qc1.x(q1[3])
    
    
    
    ### 0101 Oracle ###
    if(grid_konumu == 5):
        qc1.x(q1[1])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[1])
        qc1.x(q1[3])
    
    
    
    ### 0110 Oracle ###
    if(grid_konumu == 6):
        qc1.x(q1[0])
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
        qc1.x(q1[3])
    
    
    
    ### 0111 Oracle ###
    if(grid_konumu == 7):
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[3])
    
    
    ### 1000 Oracle ###
    if(grid_konumu == 8):
        qc1.x(q1[0])
        qc1.x(q1[1])
        qc1.x(q1[2])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
        qc1.x(q1[1])
        qc1.x(q1[2])
    
    
    
    ### 1001 Oracle ###
    if(grid_konumu == 9):
        qc1.x(q1[1])
        qc1.x(q1[2])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[1])
        qc1.x(q1[2])
    
    
    
    ### 1010 Oracle ###
    if(grid_konumu == 10):
        qc1.x(q1[0])
        qc1.x(q1[2])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
        qc1.x(q1[2])
    
    
    
    ### 1011 Oracle ###
    if(grid_konumu == 11):
        qc1.x(q1[3])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[3])
    
    
    
    ### 1100 Oracle ###
    if(grid_konumu == 12):
        qc1.x(q1[0])
        qc1.x(q1[1])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
        qc1.x(q1[1])
    
    
    ### 1101 Oracle ###
    if(grid_konumu == 13):
        qc1.x(q1[1])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[1])
        print("aaaaaaaaaaaaaaaa")
    
    
    ### 1110 Oracle ###
    if(grid_konumu == 14):
        qc1.x(q1[0])
    
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
        qc1.x(q1[0])
    
    
    
    ###1111 Oracle###
    if(grid_konumu == 15):
        qc1.cp(pi/4, q1[0], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(-pi/4, q1[1], q1[3])
        qc1.cx(q1[0], q1[1])
        qc1.cp(pi/4, q1[1], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
        qc1.cx(q1[1], q1[2])
        qc1.cp(-pi/4, q1[2], q1[3])
        qc1.cx(q1[0], q1[2])
        qc1.cp(pi/4, q1[2], q1[3])
    
    
    print('\nPreparing Amplification circuit....\n')
    #### Amplification ####
    
    qc1.h(q1[0])
    qc1.h(q1[1])
    qc1.h(q1[2])
    qc1.h(q1[3])
    qc1.x(q1[0])
    qc1.x(q1[1])
    qc1.x(q1[2])
    qc1.x(q1[3])
    
    qc1.cp(pi/4, q1[0], q1[3])
    qc1.cx(q1[0], q1[1])
    qc1.cp(-pi/4, q1[1], q1[3])
    qc1.cx(q1[0], q1[1])
    qc1.cp(pi/4, q1[1], q1[3])
    qc1.cx(q1[1], q1[2])
    qc1.cp(-pi/4, q1[2], q1[3])
    qc1.cx(q1[0], q1[2])
    qc1.cp(pi/4, q1[2], q1[3])
    qc1.cx(q1[1], q1[2])
    
    qc1.cp(-pi/4, q1[2], q1[3])
    qc1.cx(q1[0], q1[2])
    qc1.cp(pi/4, q1[2], q1[3])
    
    qc1.x(q1[0])
    qc1.x(q1[1])
    qc1.x(q1[2])
    qc1.x(q1[3])
    qc1.h(q1[0])
    qc1.h(q1[1])
    qc1.h(q1[2])
    qc1.h(q1[3])
    
    ### Measurment ###
    qc1.barrier(q)
    qc1.measure(q1[0], c[0])
    qc1.measure(q1[1], c[1])
    qc1.measure(q1[2], c[2])
    qc1.measure(q1[3], c[3])
    
    
    backend = Aer.get_backend('qasm_simulator')
    print('\nExecuting job....\n')
    job = execute(qc1, backend, shots=250)
    
    result = job.result()
    counts = result.get_counts(qc1)
    
    mustafa=max(counts,key=lambda x:counts[x])
    print(20*"-")
    print(int(mustafa,2))
    print(20*"-")
    
    gercek_konumy = a_int*4 + buyuk_x
    gercek_konumx = b_int*4 + buyuk_y
    
    print("b_int",b_int)
    print("a_int",a_int)
    print("buyuk_x",buyuk_x)
    print("buyuky",buyuk_y)
    print(gercek_konumx)
    print(gercek_konumy)
    print('RESULT: ',counts,'\n')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    dictionary = {
        "minescanner": "mineware",
        "degerx": xDegerX,
        "degery": yDegerY,
        "phonenumber": "9976770500"
    }
    
    json_object = json.dumps(dictionary, indent=4)
    
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    
    """
    JSON Bitti
    """
    
    pygame.init()
    
    img = pygame.image.load('sankey.jpg')
    pygame.display.set_icon(img)
    
    white = (255, 255, 255)
    gray = (208, 209, 217)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
     
    dis_width = 512
    dis_height = 512
    
    rows = 16
    w = 512
    
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Quantum Minesweeper')
     
    clock = pygame.time.Clock()
    
    pygame.init()
        
    dis = pygame.display.set_mode((dis_width, dis_height))
    snake_block = 32
    snake_speed = 10
     
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
    
    
    
    def Your_score(score):
        valuex = score_font.render("DegerX: " +str(xDegerX), True, white)
        valuey = score_font.render("DegerY: " +str(yDegerY), True, white)
        dis.blit(valuex, [300, 0])
        dis.blit(valuey, [300, 32])
    
     
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
     
     
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [10, dis_height / 16])
              
     
    def gameLoop():
        game_over = False
        game_close = False
     
        x1 = dis_width / 2
        y1 = 128
     
        x1_change = 0
        y1_change = 0
     
        xgit = gercek_konumx/32
        print(xgit)
        
        snake_List = []
        Length_of_snake = 1
     
        foodx = round((xDegerX - snake_block) / 160.0) * 160.0
        foody = round((yDegerY - snake_block) / 160.0) * 160.0
        
        foodx1 = round((xDegerX - snake_block) / 160.0) * 160.0
        foody1 = round((yDegerY - snake_block) / 160.0) * 160.0
     
                
        while not game_over:
    
            while game_close == True:
                message("Mission Completed!", red)
                #Your_score(Length_of_snake - 1)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_r:
                            rastgele()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
    
                
                
            #if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
             #   game_close = True
            x1 = x1+x1_change
            y1 = y1+y1_change
            arac = 0
            
            if gercek_konumx < x1 and arac == 0:
                x1_change = -snake_block
                print("SOL")
            elif gercek_konumx > x1 and arac == 0:
                x1_change = snake_block
                print("SAĞ")
            else:
                arac = 1
  
            if gercek_konumy < y1 and arac == 1:
                y1_change = -snake_block
                print("AŞAĞI")
            elif gercek_konumy > y1 and arac == 1:
                y1_change = snake_block
                print("YUKARI")

                
                
                
            print("XXXX", x1)
            print("YYYY", y1)
            print("GERÇEK-X", gercek_konumx)
            print("GERÇEK-Y", gercek_konumy)
    
            dis.fill(black)
            sizeBtwn = w // rows
            sizeBtwna = w // rows * 4
    
            x = 0
            y = 0
            xa = 0
            ya = 0
            for l in range(rows-1):
                pygame.draw.rect(dis,red,(1,0,1,512))
                pygame.draw.rect(dis,red,(128,0,1,512))
                pygame.draw.rect(dis,red,(256,0,1,512))
                pygame.draw.rect(dis,red,(384,0,1,512))
                pygame.draw.rect(dis,red,(511,0,1,512))
                pygame.draw.rect(dis,red,(0,1,512,1))
                pygame.draw.rect(dis,red,(0,128,512,1))
                pygame.draw.rect(dis,red,(0,256,512,1))
                pygame.draw.rect(dis,red,(0,384,512,1))
                pygame.draw.rect(dis,red,(0,511,512,1))
                
                x = x + sizeBtwn
                y = y + sizeBtwn
    
                xa = xa + sizeBtwna
                ya = ya + sizeBtwna
    
                pygame.draw.line(dis, (gray), (x,0),(x,w))
                pygame.draw.line(dis, (gray), (0,y),(w,y))
                
                pygame.draw.line(dis, (213, 50, 80), (xa,0),(xa,w))
                pygame.draw.line(dis, (213, 50, 80), (0,ya),(w,ya))  
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round((xDegerX - snake_block) / 160.0) * 160.0
                foody = round((yDegerY - snake_block) / 160.0) * 160.0
                Length_of_snake += 1
                pygame.draw.rect(dis, blue, [foodx1, foody1, snake_block, snake_block])
     
            xgel = foodx + 100
            if pygame.key.get_pressed()[pygame.K_a]:
                x1_change = -xgit
                y1_change = 0
            if pygame.key.get_pressed()[pygame.K_s]:
                y1_change = xgit
                x1_change = 0
                
    
            if pygame.key.get_pressed()[pygame.K_w]:
                y1_change = -xgit
                x1_change = 0
    
                
            if x1==foodx:
                print("X")
                x1_change = 0
            if y1==foody:
                print("Y")
                y1_change = 0
            clock.tick(snake_speed)
     
        pygame.quit()
        quit()
     
    
    gameLoop()
rastgele()