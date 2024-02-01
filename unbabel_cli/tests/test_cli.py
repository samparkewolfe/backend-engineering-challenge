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