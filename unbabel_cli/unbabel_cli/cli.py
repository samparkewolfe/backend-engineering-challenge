import argparse

from . import command

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", dest="input_file", required=True, help="input file", metavar="FILE")
    return parser.parse_args()


def dispatch(args):
    if args.input_file:
        command.handle_input_file(args.input_file)


def main():
    args = parse_arguments()
    dispatch(args)
