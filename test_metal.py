
%load_ext autoreload

%autoreload 2

 

import numpy as np

from collections import OrderedDict

 

from qiskit_metal import designs, draw

from qiskit_metal import MetalGUI, Dict, Headings

 

design = designs.DesignPlanar()

gui = MetalGUI(design)

 

design.overwrite_enabled = True