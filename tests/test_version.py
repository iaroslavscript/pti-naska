
from tests import common

import ptinaska
import ptinaska.version


def test_version():

    assert ptinaska.__version__ == ptinaska.version.__version__
    assert common.pattern_semver.match(ptinaska.version.__version__)
