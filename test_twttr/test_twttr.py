from twttr import shorten


def test():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("hello!") == "hll!"
