import pytest
from seasons import totext

def test_seasons():
    assert totext("525600") == "Five hundred twenty-five thousand, six hundred minutes"