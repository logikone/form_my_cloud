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
            count = 0
            if [k for k in required_args if k in kwargs]: 
                count += 1
            if count < 1:
                raise MissingOneOf(required_args)
            return func(*args, **kwargs)
        return wrapper
    return check_requirements
