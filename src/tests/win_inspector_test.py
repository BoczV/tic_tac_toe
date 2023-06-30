import pytest
import pdb
from ..logic.win_inspector import Win_inspector

class Test_Win_inspector:
    win_inspector = None

    @pytest.fixture(autouse=True)
    def get_win_inspector(self):
        needed_part_of_alphabet = ['a', 'b', 'c']
        size = 3
        value_switcher = {"user": "X", "robot": "O"}
        self.win_inspector = Win_inspector(needed_part_of_alphabet, size, value_switcher)
        yield


    @pytest.fixture
    def get_winning_board_record(self) -> dict:
        return {"a1": "X", "a2": ".", "a3": ".", "b1": "O", "b2": "X", "b3": "O", "c1": "O", "c2": ".", "c3": "X"}


    @pytest.fixture
    def get_in_progress_board_record(self) -> dict:
        return {"a1": ".", "a2": "X", "a3": ".", "b1": "O", "b2": "X", "b3": "O", "c1": "O", "c2": ".", "c3": "X"}


    def test_check_if_someone_wins_vertically_returns_true_for_user(self, get_winning_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_vertically("X", get_winning_board_record)
        assert win is True


    def test_check_if_someone_wins_vertically_returns_false(self, get_in_progress_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_vertically("X", get_in_progress_board_record)
        assert win is False