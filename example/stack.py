import os
import sys
try:
    import fmc
except:
    sys.path.append(os.getcwd())
    import fmc

description = fmc.description("Sample FMC Stack")
metadata = fmc.metadata(
        Instances = {
            "Description": "Description of Instances",
            },
        Databases = {
            "Description": "Description of Databases",
            },
        )

eb = fmc.resource("ElasticBeanstalk")
eb_app = eb.Application(
        LogicalID = "test-app",
        ApplicationName = "Test Application",
        Description = "A Test Application",
        )

eb_env = eb.Environment(
        LogicalID = "dev-eb-env",
        ApplicationName = eb_app.LogicalID,
        )

stack = [
        description,
        metadata,
        eb_app,
        eb_env,
        ]

if __name__ == "__main__":
    for s in stack:
        print s
        print s.representation()
