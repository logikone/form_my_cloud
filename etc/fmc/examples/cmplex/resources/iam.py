try:
    import fmc
except:
    import os
    import sys
    sys.path.append(os.getcwd())
    import fmc

iam = fmc.resource("IAM")

iam_role = iam.Role(
        LogicalID = "TestIAMRole",
        AssumeRolePolicyDocument = {
            "Statement": {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "ec2.amazonaws.com",
                        ],
                    },
                "Action": [
                    "sts:AssumeRole",
                    ],
                },
            },
        Path = "/test/",
        )

iam_instance_profile = iam.InstanceProfile(
        LogicalID = "TestIAMInstanceProfile",
        Path = "/test/",
        Roles = [
            {
                "Ref": iam_role.LogicalID,
                },
            ],
        )

iam_policy = iam.Policy(
        LogicalID = "TestIAMPolicy",
        PolicyDocument = {
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "*",
                        ],
                    "Resource": [
                        "*",
                        ],
                    },
                ],
            },
        PolicyName = "TestIAMPolicy",
        Roles = [
            {
                "Ref": iam_role.LogicalID
                }
            ]
        )

resources = [
        iam_role,
        iam_instance_profile,
        iam_policy
        ]
