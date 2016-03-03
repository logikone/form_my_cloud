import os
import sys
try:
    import fmc
except:
    sys.path.append(os.getcwd())
    import fmc

name = "SampleFMCStack"

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
        LogicalID = "testapp",
        ApplicationName = "Test Application",
        Description = "A Test Application",
        )

eb_template = eb.ConfigurationTemplate(
        LogicalID = "testebtemplate",
        ApplicationName = {
            "Ref": eb_app.LogicalID,
            },
        SolutionStackName = "64bit Amazon Linux 2015.09 v2.0.8 running Docker 1.9.1",
        DependsOn = [
            eb_app.LogicalID,
            ],
        )

eb_env = eb.Environment(
        LogicalID = "devebenv",
        Description = "Test Environment",
        EnvironmentName = "TestEnvironment",
        ApplicationName = {
            "Ref": eb_app.LogicalID,
            },
        DependsOn = [
            eb_app.LogicalID,
            eb_template.LogicalID,
            ],
        TemplateName = {
            "Ref": eb_template.LogicalID,
            },
        OptionSettings = [
            {
                "Namespace": "aws:autoscaling:launchconfiguration",
                "OptionName": "InstanceType",
                "Value": "t2.nano",
                },
            {
                "Namespace": "aws:elasticbeanstalk:environment",
                "OptionName": "EnvironmentType",
                "Value": "SingleInstance",
                },
            ]
        )

stack = [
        description,
        metadata,
        eb_env,
        eb_app,
        eb_template,
        ]

if __name__ == "__main__":
    for s in stack:
        print s
        print s.representation()
