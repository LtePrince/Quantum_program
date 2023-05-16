from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit
import numpy as np

def phase_oracle(n, target, data, name = 'Oracle'):

    # create a quantum circuit on n qubits
    qc = QuantumCircuit(n, name=name)

    # create the identity matrix on n qubits
    oracle_matrix = np.identity(2**n)
    # add the -1 phase to marked elements
    if data !=  ['1001']:
        for i in range(len(data)):
            if target == data[i]:
                oracle_matrix[i,i] = -1
    else :
        oracle_matrix[0,0] = -1
    # convert your matrix (called oracle_matrix) into an operator, and add it to the quantum circuit
    qc.unitary(Operator(oracle_matrix), range(n))

    return qc

def diffuser(n):
    # create a quantum circuit on n qubits
    qc = QuantumCircuit(n, name='Diffuser')

    # apply hadamard gates to all qubits
    qc.h(range(n))
    # call the phase oracle applied to the zero state
    qc.append(phase_oracle(n, '000', ['1001']), range(n))
    # apply hadamard gates to all qubits
    qc.h(range(n))
    

    return qc


def Grover(n, ID_num, token_num, status, target, data):

    # Create a quantum circuit on n qubits
    qc = QuantumCircuit(n+token_num, n+token_num)

    # Determine r
    r = int(np.floor(np.pi/4*np.sqrt(2**n/len(target))))
    print(f'{n} qubits, basis states {target} marked, {r} rounds')

    # step 1: apply Hadamard gates on all qubits
    qc.h(range(n))
    qc.barrier()
    
    # qc.x([3,4,5])
    # qc.cx(0,3)
    # qc.cx(1,4)
    # qc.cx(2,5)
    # qc.barrier()
    
    # step 2: apply r rounds of the phase oracle and the diffuser
    for _ in range(r):
        qc.append(phase_oracle(n, target, data), range(n))
        qc.append(diffuser(n), range(n))
    qc.barrier()

    # step 3: measure all qubits
    qc.measure(range(n), range(n))
    
    
    # qc.measure(range(n+token_num), range(n+token_num))

    return qc

target = '101'
data = ['110', '010', '001', '101', '010']

# 三个qubit用来存储index，三个qubit用来存储ID，三个qubit用来存储token，一个qubit用来存储status
mycircuit = Grover(3,3,3, 1, target, data)
mycircuit.draw(output = 'mpl')


# measure
from qiskit import Aer, execute
simulator = Aer.get_backend('qasm_simulator')
counts = execute(mycircuit, backend=simulator, shots=1000).result().get_counts(mycircuit)
from qiskit.visualization import plot_histogram
plot_histogram(counts)
