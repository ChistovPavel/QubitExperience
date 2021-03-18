import matplotlib.pyplot as plt
import FirstPractice as fp

qc = fp.firstCircuit();
stateVector = fp.getStateVector(qc)

for i in range(0, len(stateVector), 1):
	print(round(stateVector[i], 2))

	
qc.draw(output='mpl')
plt.show()