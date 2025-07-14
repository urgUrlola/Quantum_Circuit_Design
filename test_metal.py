from qiskit_metal import designs, MetalGUI
import sys



# To Create a new design
design=designs.DesignPlanar()

# To Launch Metal GUI with this design
gui = MetalGUI(design)

# keeps GUI running un
