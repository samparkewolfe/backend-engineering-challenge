import sys
import argparse

from . import command

def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", dest="input_file", required=True, help="input file", metavar="FILE")
    parser.add_argument("--window_size", dest="window_size", required=False, help="window size", type=int)
    return parser.parse_args(args)


def dispatch(args):
    if args.input_file and args.window_size:
        command.handle_input_file_and_window_size(args.input_file, args.window_size)
    elif args.input_file:
        command.handle_input_file_and_window_size(args.input_file, 10)


def main():
    args = parse_arguments(sys.argv[1:])
    dispatch(args)
