
import argparse

import pytest

from tests import common
from ptinaska import cli
from ptinaska import version


def test_create_parser():

    assert isinstance(cli.create_parser(), argparse.ArgumentParser)


def test_main(capfd):

    with pytest.raises(SystemExit) as e:
        assert cli.main(["--version"])

    assert e.value.code == 0

    out, err = capfd.readouterr()

    assert err == ""
    assert out.strip() == version.__version__
    assert common.pattern_semver.match(out.strip())
