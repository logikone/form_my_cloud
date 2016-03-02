import os
import sys
import argparse
import imp
import json

try:
    import fmc
except:
    sys.path.append(os.getcwd())
    import fmc

client = fmc.client()

def get_options():
    parent_parser = argparse.ArgumentParser()

    shared_args = argparse.ArgumentParser(add_help=False)
    shared_args.add_argument("--stack", "-s", type=str, required=True,
            help="Path to stack file realive to cwd.")

    subparsers = parent_parser.add_subparsers(dest="operation")

    representation = subparsers.add_parser("representation", parents=[shared_args])
    validate = subparsers.add_parser("validate", parents=[shared_args])
    create = subparsers.add_parser("create", parents=[shared_args])

    options = parent_parser.parse_args()

    return options

def _dumps(doc):
    return json.dumps(
            doc,
            indent=4,
            sort_keys=True,
            )

def main():
    options = get_options()

    try:
        stack = imp.load_source("stack", options.stack)
    except Exception as e:
        print str(e)
        sys.exit()

    if options.operation == "representation":
        print _dumps(client.stack_representation(stack))

    if options.operation == "create":
        print _dumps(client.create_stack(stack))

    if options.operation == "validate":
        print _dumps(client.validate_stack(stack))

if __name__ == "__main__":
    main()
