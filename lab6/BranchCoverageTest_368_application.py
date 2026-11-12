
import pytest

from vending_machine import select_item, make_change, purchase


def test_select_item_all_branches():
    assert select_item("water", {}, 200) == "invalid"
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"
    assert select_item("cola", {"cola": 2}, 100) == "insufficient"
    assert select_item("cola", {"cola": 2}, 150) == "ok"


def test_make_change_all_branches():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-5)

    assert make_change(0) == []
    assert make_change(25) == [25]
    assert make_change(185) == [100, 50, 25, 10]
    assert make_change(3) is None


def test_purchase_error_branches():
    assert purchase("water", {}, 200) == ("invalid", [])
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])
    assert purchase("cola", {"cola": 2}, 100) == ("insufficient", [])

    stock = {"candy": 5}
    assert purchase("candy", stock, 76) == ("no_exact_change", [])
    assert stock["candy"] == 5


def test_purchase_success_branches():
    stock = {"cola": 5}
    assert purchase("cola", stock, 200) == ("dispensed", [50])
    assert stock["cola"] == 4

    stock = {"chips": 3}
    assert purchase("chips", stock, 100) == ("dispensed", [])
    assert stock["chips"] == 2
