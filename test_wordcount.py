from wordcount import count


def test_count():
    assert count("one two\nthree\n") == (2, 3, 14)


def test_empty():
    assert count("") == (0, 0, 0)


if __name__ == "__main__":
    test_count()
    test_empty()
    print("ok")
