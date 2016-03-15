import os
import sys
import argparse
import json
import re
import fmc

def get_options(args):
    parent_parser = argparse.ArgumentParser()

    shared_args = argparse.ArgumentParser(add_help=False)
    shared_args.add_argument("stack", type=str,
            help="Path to stack file realive to cwd.")
    shared_args.add_argument("--path", type=str, nargs="?", default="/etc/fmc/stacks",
            help="Path to search for stack, if stack not in default path.")

    subparsers = parent_parser.add_subparsers(dest="operation")

    representation = subparsers.add_parser("representation", parents=[shared_args])
    validate = subparsers.add_parser("validate", parents=[shared_args])
    create = subparsers.add_parser("create", parents=[shared_args])
    delete = subparsers.add_parser("delete", parents=[shared_args])

    options = parent_parser.parse_args(args)

    return options

def _dumps(doc):
    return json.dumps(
            doc,
            indent=4,
            sort_keys=True,
            )

def main():
    client = fmc.client()
    options = get_options(sys.argv[1:])

    r = re.compile("^/")
    if r.match(options.path):
        sys.path.append(options.path)
    else:
        sys.path.append(
                "{0}/{1}".format(
                    os.getcwd(),
                    options.path
                    )
                )

    try:
        name, fromlist = options.stack.split(".", 1)
        stack = __import__(
                options.stack,
                globals(),
                locals(),
                [fromlist]
                )
    except ImportError as e:
        try:
            stack = __import__(
                options.stack
                )
        except ImportError as e:
            sys.exit(e)

    if options.operation == "representation":
        try:
            print _dumps(client.stack_representation(stack))
        except Exception as e:
            sys.exit(e)

    if options.operation == "create":
        try:
            print _dumps(client.create_stack(stack))
        except Exception as e:
            sys.exit(e)

    if options.operation == "validate":
        try:
            print _dumps(client.validate_stack(stack))
        except Exception as e:
            sys.exit(e)

    if options.operation == "delete":
        try:
            print _dumps(client.delete_stack(stack))
        except Exception as e:
            sys.exit(e)

if __name__ == "__main__":
    main()

#! vim: ts=4 sw=4 ft=python expandtab:
