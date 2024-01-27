# Unbabel CLI
Welcome to my submission for Unbabel!

You will want to create a new python environment with python 3 to build, install and test this package.

Please look at my git history to see the development of this project.

## Build
Update the `build` package

    python -m pip install --upgrade build

Run the following command from the same directory as `pyproject.toml`

    python -m build

Install the built package to your pip ecosystem using the `.whl` file which should have been built in the `dist/` directory. Yours might have a different name

    python -m pip install dist/unbabel_cli-0.1.0-py3-none-any.whl

## Run
Run this example command. In `examples/` there is already an example JSON file to use as the input file

    unbabel_cli --input_file examples/events.json --window_size 10

This function will create a file called `output_file.json` in the current directory

## Test

Install tox

    pip install tox

Run this command from the same directory as `pyproject.toml`

    tox