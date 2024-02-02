import sys
import argparse

from . import command


def is_valid_json_file(arg):
    if not arg.lower().endswith('.json'):
        raise argparse.ArgumentTypeError(f"{arg} is not a JSON file.")
    return arg


def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", dest="input_file", required=True, type=is_valid_json_file, help="Path to JSON file full of events", metavar="JSON_FILE")
    parser.add_argument("--window_size", dest="window_size", required=False, type=int, help="Averaging window size of event durations in minutes", metavar="INT")
    return parser.parse_args(args)


def dispatch(args):
    if args.input_file and args.window_size:
        command.handle_input_file_and_window_size(args.input_file, args.window_size)
    elif args.input_file:
        command.handle_input_file_and_window_size(args.input_file, 10)


def main():
    args = parse_arguments(sys.argv[1:])
    dispatch(args)
