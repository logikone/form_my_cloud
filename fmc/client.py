import sys
import botocore.session
import botocore.exceptions

from cf.base import Base

class Client(Base):
    def __init__(self):
        session = botocore.session.get_session()
        self.cf_client = session.create_client("cloudformation")

    def _validate_template(self, template):
        try:
            valid = self.cf_client.validate_template(
                    TemplateBody = template
                    )
        except botocore.exceptions.ClientError as e:
            sys.stderr.write("ERROR: {0}".format(str(e)))
            raise
        except Exception as e:
            sys.stderr.write(str(e))
            raise

        return valid

    @classmethod
    def _combine_dicts(Class, configs):
        self = Class()
        combined_dict = {}
        for config in configs:
            self._update_dict(
                    combined_dict,
                    config.representation(),
                    )

        return combined_dict

    @classmethod
    def validate_stack(Class, configs):
        self = Class()
        combined_dict = self._combine_dicts(configs)
        serialized_dict = self.serialize(combined_dict)

        valid = self._validate_template(
                serialized_dict
                )

        return valid

    @classmethod
    def create_stack(Class, configs):
        self = Class()
        combined_dict = self._combine_dicts(configs)

        template_valid = self._validate_template(
                self.serialize(combined_dict)
                )

        print self.serialize(combined_dict)

    @classmethod
    def delete_stack(Class, stack_name):
        self = Class()
        try:
            return self.cf_client.delete_stack(
                    StackName = stack_name
                    )
        except botocore.exceptions.ClientError as e:
            sys.stderr.write("ERROR: {0}".format(str(e)))
            raise
        except Exception as e:
            sys.stderr.write(str(e))
            raise



#! vim: ts=4 sw=4 ft=python expandtab:
