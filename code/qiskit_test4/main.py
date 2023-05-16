import matplotlib.pyplot as plt
import numpy as np

from qiskit import (
    QuantumCircuit,
    execute,
    Aer)
from qiskit import assemble,transpile

from qiskit.visualization import plot_histogram

qc=QuantumCircuit(3)
qc.cz(0,2)
qc.cz(1,2)
oracle_ex3 = qc.to_gate()

def initialize_s(qc,qubits):
    for q in qubits:
        qc.h(q)
    return qc

def diffuser(nqubits):
    qc = QuantumCircuit(nqubits)
    for qubit in range(nqubits):
        qc.h(qubit)
    for qubit in range(nqubits):
        qc.x(qubit)
    #迭代次数为PI/4*根号下（N/M）
    for i in range(1):
        qc.h(nqubits-1)
        qc.mct(list(range(nqubits-1)),nqubits-1)
        qc.h(nqubits-1)

    for qubit in range(nqubits):
        qc.x(qubit)
    for qubit in range(nqubits):
        qc.h(qubit)
    #qc.draw(output="mpl")
    U_s=qc.to_gate()
    U_s.name="U_s"
    return U_s

n=5
grover_circuit = QuantumCircuit(n)
grover_circuit = initialize_s(grover_circuit,list(range(n)))
#grover_circuit.x(0)
grover_circuit.z([0,1,2])
grover_circuit.cz(0,1)
grover_circuit.ccz(0,1,2)
grover_circuit.cz(1,2)
grover_circuit.cz(0,2)
#grover_circuit.cz(0,1)
#grover_circuit.z(1)
#grover_circuit.cz(0,2)
#grover_circuit.cz(2,3)
#grover_circuit.append(oracle_ex3,[0,1,2])
grover_circuit.append(diffuser(n),list(range(n)))
grover_circuit.measure_all()
grover_circuit.draw(output="mpl")


aer_sim=Aer.get_backend('aer_simulator')
#transpiled_grover_circuit=transpile(grover_circuit,aer_sim)
#qobj = assemble(transpiled_grover_circuit)
result = execute(grover_circuit,aer_sim,shot=1000).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()