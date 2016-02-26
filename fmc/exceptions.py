
class MissingArgument(Exception):
    def __init__(self, missing):
        self.missing = missing

    def __str__(self):
        return "The Argument '{0}' Must Be Defined".format(
                self.missing
                )

#! vim: ts=4 sw=4 ft=python expandtab:
