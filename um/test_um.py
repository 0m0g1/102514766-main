import pytest
from um import count


def test():
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1
