import pytest
from ..logic.win_inspector import Win_inspector


@pytest.fixture
def get_win_inspector() -> Win_inspector:
    needed_part_of_alphabet = ['a', 'b', 'c']
    size = 3
    value_switcher = {"user": "X", "robot": "O"}
    win_inspector = Win_inspector(needed_part_of_alphabet, size, value_switcher)
    return win_inspector


@pytest.fixture
def get_board_record() -> dict:
    return {"a1": "X", "a2": "X", "a3": "X", "b1": ".", "b2": "O", "b3": "O", "c1": "O", "c2": ".", "c3": "."}


def test_check_if_someone_wins_vertically_returns_true_for_user(get_win_inspector: Win_inspector, get_board_record: dict):
    win = get_win_inspector.check_if_someone_wins_vertically("X", get_board_record)
    assert win is True