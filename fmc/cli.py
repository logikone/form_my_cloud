import os
import sys
import argparse
try:
    import fmc
except:
    sys.path.append(os.getcwd())
    import fmc

def get_options():
    args = argparse.ArgumentParser()
    args.add_argument("--stack", "-s", type=str,
            help="Full path to Stack to run operations for.")
    args.add_argument("--validate", action="store_true",
            help="Validate Stack.")

    options = args.parse_args()
    if len(sys.argv) < 2:
        args.print_help()
        sys.exit(0)

    return options

def main():
    options = get_options()
    print options

if __name__ == "__main__":
    main()
