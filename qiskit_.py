from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()
qc.draw(output='mpl')

sim = AerSimulator()
job = sim.run(qc, shots = 1000)
results = job.result()
counts = results.get_counts()
print(counts)
plot_histogram(counts)