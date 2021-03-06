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

    def _combine_dicts(self, stack):
        combined_dict = {}

        # Add Template Version
        try:
            version = stack.version
        except:
            from fmc.format import Version
            version = Version()
        finally:
            self._update_dict(
                    combined_dict,
                    version.representation()
                    )

        # Add Description
        try:
            self._update_dict(
                    combined_dict,
                    stack.description.representation()
                    )
        except:
            pass

        # Add MetaData
        try:
            self._update_dict(
                    combined_dict,
                    stack.metadata.representation()
                    )
        except:
            pass

        # Add Parameters
        try:
            for parameter in stack.parameters:
                self._update_dict(
                        combined_dict,
                        parameter.representation()
                        )
        except:
            pass

        # Add Mappings
        try:
            for mapping in stack.mappings:
                self._update_dict(
                        combined_dict,
                        mapping.representation()
                        )
        except:
            pass

        # Add Conditions
        try:
            for condition in stack.conditions:
                self._update_dict(
                        combined_dict,
                        condition.representation()
                        )
        except:
            pass

        # Add Resources
        try:
            for resource in stack.resources:
                self._update_dict(
                        combined_dict,
                        resource.representation(),
                        )
        except:
            pass

        # Add Outputs
        try:
            for output in stack.outputs:
                self._update_dict(
                        combined_dict,
                        output.representation()
                        )
        except:
            pass

        return combined_dict

    def validate_stack(self, stack):
        combined_dict = self._combine_dicts(stack)
        serialized_dict = self.serialize(combined_dict)

        valid = self._validate_template(
                serialized_dict
                )

        return valid

    def create_stack(self, stack, validate=True):
        combined_dict = self._combine_dicts(stack)
        Capabilities = []

        for resource in stack.resources:
            try:
                Capabilities.append(resource.Capabilities)
            except:
                pass

        if validate:
            template_valid = self._validate_template(
                    self.serialize(combined_dict)
                    )
        else:
            template_valid = True

        if template_valid:
            response = self.cf_client.create_stack(
                    StackName = stack.name,
                    TemplateBody = self.serialize(combined_dict),
                    Capabilities = Capabilities,
                    )

        return response

    def delete_stack(self, stack):
        return self.cf_client.delete_stack(
                StackName = stack.name
                )

    def stack_representation(self, stack):
        return self._combine_dicts(stack)

#! vim: ts=4 sw=4 ft=python expandtab:
