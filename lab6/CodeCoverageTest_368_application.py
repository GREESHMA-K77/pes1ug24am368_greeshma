
import pytest

from vending_machine import select_item, make_change, purchase


def test_invalid_item():
    assert select_item("water", {}, 200) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"


def test_valid_item_selection():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


def test_no_change_needed():
    assert make_change(0) == []


def test_make_change_single_coin():
    assert make_change(25) == [25]


def test_make_change_multiple_coins():
    assert make_change(185) == [100, 50, 25, 10]


def test_make_change_unrepresentable_amount():
    assert make_change(3) is None


def test_negative_change():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-5)


def test_purchase_invalid_item():
    assert purchase("water", {}, 200) == ("invalid", [])


def test_purchase_sold_out():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])


def test_purchase_insufficient_credit():
    assert purchase("cola", {"cola": 5}, 100) == ("insufficient", [])


def test_purchase_no_exact_change():
    stock = {"candy": 5}
    assert purchase("candy", stock, 76) == ("no_exact_change", [])
    assert stock["candy"] == 5


def test_successful_purchase():
    stock = {"cola": 5}
    result = purchase("cola", stock, 200)

    assert result == ("dispensed", [50])
    assert stock["cola"] == 4


def test_successful_purchase_exact_amount():
    stock = {"chips": 3}
    result = purchase("chips", stock, 100)

    assert result == ("dispensed", [])
    assert stock["chips"] == 2
