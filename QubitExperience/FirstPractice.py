from qiskit import QuantumCircuit, assemble, Aer

def firstCircuit():
	qc = QuantumCircuit(2)
	qc.h(0)
	qc.cx(0, 1)
	return qc

def getStateVector(qc: QuantumCircuit):
	svsim = Aer.get_backend('statevector_simulator')
	qobj = assemble(qc)
	return svsim.run(qobj).result().get_statevector()