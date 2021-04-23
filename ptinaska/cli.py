#!/bin/env python3

import argparse
import sys
from typing import List

from ptinaska import version


def create_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(prog='ptinaska')
    parser.add_argument('--version', action='version', version=version.__version__)

    return parser


def main(args: List[str]) -> None:

    parser: argparse.ArgumentParser = create_parser()
    parser.parse_args(args)


if __name__ == "__main__":  # noqa
    main(sys.argv[1:])
