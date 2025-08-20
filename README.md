7-Transmon Quantum Chip Simulation

Project Description
Simulation and design of a superconducting quantum chip composed of seven transmon qubits, including six fixed-frequency qubits and one central flux-tunable qubit. The project models qubit-resonator interactions, multi-qubit dynamics, and key quantum properties like T1 relaxation times, using Qiskit Metal, QuTiP, and electromagnetic simulations.

Motivation
Superconducting qubits are a leading platform for scalable quantum computing. Understanding qubit-resonator interactions, energy spectra, and coherence times is essential for designing high-fidelity quantum hardware. This project bridges theoretical quantum mechanics with practical device design.

Key Results

Designed and visualized the 7-qubit chip layout using Qiskit Metal.

Extracted qubit and resonator parameters using Gmsh and Elmer FEM simulations.

Modeled qubit-resonator interactions with Jaynes-Cummings and Tavis-Cummings Hamiltonians using QuTiP.

Simulated T1 relaxation times for all qubits; values ranged 18–35 µs, consistent with expected transmon behavior.

Developed an end-to-end simulation pipeline from chip design to quantum dynamics analysis.

Tools & Technologies

Qiskit Metal – Chip layout and design

QuTiP – Quantum simulations

Elmer FEM / Gmsh – Electromagnetic simulations

Python / NumPy / Matplotlib – Data analysis and visualization

LaTeX – Full technical report

How to Run / Reproduce

Code for simulation and visualization is included in this repository.

Dependencies: Qiskit, QuTiP, NumPy, Matplotlib, Elmer FEM (optional for EM simulations).

Instructions for running each module are documented in the notebook files.

Visuals / Results

Qubit frequencies, resonator detunings, and layout schematics included in figures/.

T1 relaxation curves for all seven qubits included.

Next Steps / Future Work

Expand simulations to include realistic noise and decoherence models (Lindblad, thermal noise, non-Markovian effects).

Compare simulated results with experimental data from published superconducting qubit systems.

Scale up for multi-qubit gate analysis and entanglement studies in a circuit QED setup.

Full Paper
For a detailed technical report, see
