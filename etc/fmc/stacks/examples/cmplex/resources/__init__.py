from . import elasticbeanstalk
from . import iam

resources = elasticbeanstalk.resources + iam.resources
