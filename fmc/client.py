import sys
import botocore.session
import botocore.exceptions

from fmc.base import Base

class Client(Base):
    def __init__(self):
        session = botocore.session.get_session()
        self.cf_client = session.create_client("cloudformation")

    def _validate_template(self, template):
        valid = self.cf_client.validate_template(
                TemplateBody = template
                )

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
    def validate_stack(Class, stack):
        self = Class()
        combined_dict = self._combine_dicts(stack.stack)
        serialized_dict = self.serialize(combined_dict)

        valid = self._validate_template(
                serialized_dict
                )

        return valid

    @classmethod
    def create_stack(Class, stack):
        self = Class()
        combined_dict = self._combine_dicts(stack.stack)

        template_valid = self._validate_template(
                self.serialize(combined_dict)
                )

        if template_valid:
            response = self.cf_client.create_stack(
                    StackName = stack.name,
                    TemplateBody = self.serialize(combined_dict),
                    )

        return response

    @classmethod
    def delete_stack(Class, stack):
        self = Class()
        return self.cf_client.delete_stack(
                StackName = stack.name
                )

    @classmethod
    def stack_representation(Class, stack):
        self = Class()
        return self._combine_dicts(stack.stack)

#! vim: ts=4 sw=4 ft=python expandtab:
