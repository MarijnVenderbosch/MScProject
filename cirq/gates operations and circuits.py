# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:59:28 2021

@author: marijn
"""


import cirq

#3 by 3 grid of qubits
qubits = [cirq.GridQubit(x,y) for x in range(3) for y in range(3)]

print(qubits)

#Pauli X gate
x_gate = cirq.X

#operation applying X gate on location (0,0)
x_op = x_gate(qubits[0])

print(x_op)

#circuits
cz01 = cirq.CZ(qubits[0] , qubits[1])
x2 = cirq.X(qubits[2])
cz12 = cirq.CZ(qubits[1], qubits[2])

moment0 = cirq.Moment([cz01 , x2])
moment1 = cirq.Moment([cz12])

circuit = cirq.Circuit((moment0,moment1))

print(circuit)