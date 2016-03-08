try:
    import fmc
except:
    import os
    import sys
    sys.path.append(os.getcwd())
    import fmc

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

resources = [
        eb_app,
        eb_template,
        eb_env
        ]
