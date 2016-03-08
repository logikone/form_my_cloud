try:
    import fmc
except:
    import os
    import sys
    sys.path.append(os.getcwd())
    import fmc

metadata = fmc.metadata(
        Instances = {
            "Description": "Description of Instances",
            },
        Databases = {
            "Description": "Description of Databases",
            },
        )
