
class MissingArgument(Exception):
    def __init__(self, missing):
        self.missing = missing

    def __str__(self):
        return "The Argument '{0}' Must Be Defined".format(
                self.missing
                )

class MissingOneOf(Exception):
    def __init__(self, missing_one_of, calling_class):
        self.missing_one_of = ", ".join(missing_one_of)
        self.calling_class = calling_class

    def __str__(self):
        return "One of '{0}' Must Be Defined In {1}".format(
                self.missing_one_of,
                self.calling_class,
                )

#! vim: ts=4 sw=4 ft=python expandtab:
