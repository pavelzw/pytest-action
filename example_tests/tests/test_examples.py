import random
import pytest
import main


@pytest.mark.skip(reason="This test would fail")
def test_failed():
    assert "emoji" == "hello world"


@pytest.mark.xfail
def test_xfailed():
    assert random.random() == 1.0


@pytest.mark.xfail
def test_xpassed():
    assert 0.0 < random.random() < 1.0


@pytest.mark.skip(reason="don't run this test")
def test_skipped():
    assert "pytest-emoji" != ""


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Sara", "Hello Sara!"),
        ("Mat", "Hello Mat!"),
        ("Annie", "Hello Annie!"),
    ],
)
def test_passed(name, expected):
    assert f"Hello {name}!" == expected


@pytest.fixture
def number():
    return 1234 / 0


@pytest.mark.skip(reason="This test would raise an error")
def test_error(number):
    assert number == number


def test_coverage():
    main.covered()
    assert True
