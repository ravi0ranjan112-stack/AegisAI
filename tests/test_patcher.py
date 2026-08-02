from aegis.patch.diff import DiffGenerator


def test_diff():
    diff = DiffGenerator().create(
        "hello\n",
        "world\n",
    )
    assert diff
