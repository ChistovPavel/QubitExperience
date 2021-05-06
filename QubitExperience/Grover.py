from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def getGroverCircuit():
    qA = QuantumRegister(2, name='a')
    qB = QuantumRegister(2, name='b')
    qC = QuantumRegister(3, name='c')
    qS = QuantumRegister(1, name='s')
    output = QuantumRegister(1, name='output')
    cr1 = ClassicalRegister(1)
    cr2 = ClassicalRegister(1)
    grover_circuit = QuantumCircuit(qA, qB, qC, qS, output, cr1, cr2)

    for i in range(0, 2, 1):
        grover_circuit.h(qA[i])

    grover_circuit.barrier()

    grover_circuit.initialize([0, 1], qB[0])
    grover_circuit.initialize([0, 1], qB[1])

    grover_circuit.barrier()

    grover_circuit.cx(qA[0], qC[0])
    grover_circuit.cx(qB[0], qC[0])
    grover_circuit.ccx(qA[0], qB[0], qS[0])
    
    grover_circuit.barrier()
    
    grover_circuit.cx(qA[1], qC[1])
    grover_circuit.cx(qB[1], qC[1])
    grover_circuit.ccx(qA[1], qB[1], qC[2])
    
    grover_circuit.barrier()

    grover_circuit.ccx(qS[0], qC[1], qC[2])
    grover_circuit.cx(qS[0], qC[1])
    grover_circuit.x(qC[1])

    grover_circuit.mct(qC, output)

    grover_circuit.barrier()

    grover_circuit.x(qC[1])
    grover_circuit.cx(qS[0], qC[1])
    grover_circuit.ccx(qS[0], qC[1], qC[2])

    grover_circuit.barrier()

    grover_circuit.ccx(qA[1], qB[1], qC[2])
    grover_circuit.cx(qB[1], qC[1])
    grover_circuit.cx(qA[1], qC[1])

    grover_circuit.barrier()

    grover_circuit.ccx(qA[0], qB[0], qS[0])
    grover_circuit.cx(qB[0], qC[0])
    grover_circuit.cx(qA[0], qC[0])

    grover_circuit.barrier()

    for i in range(0, 2, 1):
        grover_circuit.h(qA[i])
        grover_circuit.z(qA[i])
    
    grover_circuit.cz(qA[0],qA[1])

    for i in range(0, 2, 1):
        grover_circuit.h(qA[i])

    grover_circuit.measure(qA[0], cr1[0])
    grover_circuit.measure(qA[1], cr2[0])

    return grover_circuit;