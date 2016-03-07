
class MissingArgument(Exception):
    def __init__(self, missing):
        self.missing = missing

    def __str__(self):
        return "The Argument '{0}' Must Be Defined".format(
                self.missing
                )

class MissingOneOf(Exception):
    def __init__(self, missing_one_of):
        self.missing_one_of = ", ".join(missing_one_of)

    def __str__(self):
        return "One of '{0}' Must Be Defined".format(
                self.missing_one_of
                )

#! vim: ts=4 sw=4 ft=python expandtab:
