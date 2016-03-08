from .resources import resources
from .metadata import metadata

try:
    import fmc
except:
    import os
    import sys
    sys.path.append(os.getcwd())
    import fmc

name = "SampleFMCStack"
description = fmc.description("Sample FMC Stack")
