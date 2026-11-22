import hashlib


def test_md5():
    assert hashlib.md5(b"").hexdigest()
