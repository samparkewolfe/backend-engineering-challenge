import argparse

from . import command

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", dest="filename", required=True, help="input file", metavar="FILE")
    return parser.parse_args()


def dispatch(args):
    command.handle_filename(args.filename)


def main():
    args = parse_arguments()
    dispatch(args)
