import matplotlib.pyplot as plt
import BellsState as bs
import QuantumTeleportation as qt
import math
import Utils

from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit import IBMQ, Aer, transpile, assemble

def bellsStateTest():
    qc = bs.getBellsState1([1,0], [1,0])
    stateVector = Utils.getStateVector(qc)
    Utils.printStateVector(stateVector, 4)
    qc.draw(output='mpl')
    plt.show()

def teleportationState():
    qtc = qt.teleportateQuantumState([0.5, math.sqrt(1-0.25)])
    teleportationStateVector = Utils.getStateVector(qtc)
    qtc.draw(output='mpl')
    
    qasm_sim = Aer.get_backend('qasm_simulator')
    qobj = assemble(qtc)
    counts = qasm_sim.run(qobj).result().get_counts()
    plot_histogram(counts)

    plt.show()

teleportationState()