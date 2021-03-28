from qiskit import QuantumCircuit, assemble, Aer

def printStateVector(stateVector, binNumberLength):
    for i in range(0, len(stateVector), 1): 
        print('{} : {}'.format(bin(i).replace('b', '').zfill(binNumberLength), round(stateVector[i], 2)))

def getStateVector(qc: QuantumCircuit):
	svsim = Aer.get_backend('statevector_simulator')
	qobj = assemble(qc)
	return svsim.run(qobj).result().get_statevector()