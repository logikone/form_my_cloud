from .exceptions import (
        MissingArgument,
        MissingOneOf
        )

def RequiredArguments(required_args):
    def check_requirements(func):
        def wrapper(*args, **kwargs):
            for arg in required_args:
                if not arg in kwargs:
                    raise MissingArgument(arg)
            return func(*args, **kwargs)
        return wrapper
    return check_requirements

def RequiresOneOf(required_args):
    def check_requirements(func):
        def wrapper(*args, **kwargs):
            if "Properties" not in kwargs:
                kwargs["Properties"] = {}

            count = 0
            for req in required_args:
                if req in kwargs:
                    kwargs["Properties"][req] = kwargs[req]
                    count += 1

            if count < 1:
                raise MissingOneOf(required_args)
            return func(*args, **kwargs)
        return wrapper
    return check_requirements

def RequiredProperties(required):
    def add_required_props(func):
        def wrapper(*args, **kwargs):
            if "Properties" not in kwargs:
                kwargs["Properties"] = {}

            for opt in required:
                if opt not in kwargs:
                    raise MissingArgument(opt)
                else:
                    kwargs["Properties"][opt] = kwargs[opt]
            return func(*args, **kwargs)
        return wrapper
    return add_required_props

def OptionalProperties(optional):
    def add_optional_props(func):
        def wrapper(*args, **kwargs):
            if "Properties" not in kwargs:
                kwargs["Properties"] = {}

            for opt in optional:
                if opt in kwargs:
                    kwargs["Properties"][opt] = kwargs[opt]
            return func(*args, **kwargs)
        return wrapper
    return add_optional_props
