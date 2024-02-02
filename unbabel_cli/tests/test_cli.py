from importlib import import_module
from importlib.metadata import version
from os import linesep
from unittest.mock import patch

import pytest
from cli_test_helpers import ArgvContext, shell

import unbabel_cli.cli


def test_main_module():
    """
    Exercise (most of) the code in the ``__main__`` module.
    """
    import_module("unbabel_cli.__main__")


def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    result = shell("python -m unbabel_cli --help")
    assert result.exit_code == 0


def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    result = shell("unbabel_cli --help")
    assert result.exit_code == 0


@patch("unbabel_cli.cli.dispatch")
def test_usage(mock_dispatch):
    """
    Does CLI abort w/o arguments, displaying usage instructions?
    """
    with ArgvContext("unbabel_cli"), pytest.raises(SystemExit):
        unbabel_cli.cli.main()

    assert not mock_dispatch.called, "CLI should stop execution"

    result = shell("unbabel_cli")

    assert "usage:" in result.stderr


@patch("unbabel_cli.cli.dispatch")
def test_dispach_gets_called(mock_dispatch):
    """
    Does CLI call dispatch with correct arguments?
    """
    with ArgvContext("unbabel_cli", "--input_file", "example.json", "--window_size", "10"):
        unbabel_cli.cli.main()

    assert mock_dispatch.called, "Dispatch should have been called"


def test_input_file():
    """
    Can set the argument input file?
    """
    parser = unbabel_cli.cli.parse_arguments(["--input_file", "example.json"])
    assert parser.input_file != None


def test_window_size():
    """
    Can set the argument window size?
    """
    parser = unbabel_cli.cli.parse_arguments(["--input_file", "example.json", "--window_size", "10"])
    assert parser.window_size != None


@patch("unbabel_cli.cli.dispatch")
def test_missing_input_file_argument(mock_dispatch):
    """
    Does CLI abort w/o arguments, displaying usage instructions if input file is missing?
    """
    with ArgvContext("unbabel_cli", "--window_size", "10"), pytest.raises(SystemExit):
        unbabel_cli.cli.main()

    assert not mock_dispatch.called, "CLI should stop execution"

    result = shell("unbabel_cli --window_size 10")

    assert "usage:" in result.stderr


def test_window_size_correct_type():
    """
    Does window size end up as an int?
    """
    parser = unbabel_cli.cli.parse_arguments(["--input_file", "example.json", "--window_size", "10"])
    assert isinstance(parser.window_size, int)


@patch("unbabel_cli.cli.dispatch")
def test_window_size_wrong_type(mock_dispatch):
    """
    Does CLI abort w/o arguments, displaying usage instructions if window size is a non-int value?
    """
    with ArgvContext("unbabel_cli", "--input_file", "example.json", "--window_size", "blahblahblah"), pytest.raises(SystemExit):
        unbabel_cli.cli.main()

    assert not mock_dispatch.called, "CLI should stop execution"

    result = shell("unbabel_cli --input_file example.json --window_size blahblahblah")

    assert "usage:" in result.stderr


@patch("unbabel_cli.cli.dispatch")
def test_input_file_not_json(mock_dispatch):
    """
    Does CLI abort w/o arguments, displaying usage instructions if input files is not a json file?
    """
    with ArgvContext("unbabel_cli", "--input_file", "example.txt"), pytest.raises(SystemExit):
        unbabel_cli.cli.main()

    assert not mock_dispatch.called, "CLI should stop execution"