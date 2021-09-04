"""An example of a test module in pytest"""

from pytest_lessons.ls1_module import total, join


def test_total_empty() -> None:
    """Total of empty list should be 0.0."""
    assert total([]) == 0.0


def test_total_single_item() -> None:
    """Total of a single item list should be the first item's value."""
    assert total([110.0]) == 110.0


def test_total_many_items() -> None:
    """Total of a list with many items should be their sum."""
    assert total([1.0, 7.0, 3.0]) == 11.0


def test_join_use_case() -> None:
    assert join([1,2,3], ", ") == "1, 2, 3"


def test_join_edge_single_item() -> None:
    assert join([1], ", ") == "1"


def test_join_edge_empty_delimiter() -> None:
    assert join([1,2,3], "") == "123"