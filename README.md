# Chancery

This repository defines a **PIP package** which facilitates the generation of **letters patent** on behalf of His Majesty The King of Cyprus.

## Installation

Download this resposity, and then run:

```sh
pip install .
```

from the same directory as this file.

It may also be necessary to install the fonts used in the codebase, in which case run `sh install_fonts.sh` from the same directory.

## Command Line Interface

To generate a letters patent, first create an inputs JSON file. You can find examples of these in the `example_input_files` directory. Then run:

```sh
compile-patent path/to/input.json
```
