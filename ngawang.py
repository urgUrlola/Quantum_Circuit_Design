import qiskit_metal
from qiskit_metal import designs
design = designs.DesignPlanar()

from qiskit_metal import MetalGUI
gui = MetalGUI(design)
gui.show()

from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket

qubit = TransmonPocket(design, 'Q0', options = {'pos_x': '0um', 'pos_y': '0um', 'pad_width': '60um', 'pad_height': '60um'})

gui.rebuild()