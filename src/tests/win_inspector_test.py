import pytest
from ..logic.win_inspector import WinInspector

class TestWinInspector:
    win_inspector = None

    @pytest.fixture(autouse=True)
    def get_win_inspector(self):
        needed_part_of_alphabet = ['a', 'b', 'c']
        size = 3
        value_switcher = {"first": "X", "second": "O"}
        self.win_inspector = WinInspector(needed_part_of_alphabet, size, value_switcher)
        yield


    @pytest.fixture
    def get_diagonally_board_record(self) -> dict:
        return {
            "a1": "X", "a2": ".", "a3": ".", 
            "b1": "O", "b2": "X", "b3": "O", 
            "c1": "O", "c2": ".", "c3": "X"
            }


    @pytest.fixture
    def get_vertically_board_record(self) -> dict:
        return {
            "a1": ".", "a2": "X", "a3": "O", 
            "b1": "O", "b2": "X", "b3": "O", 
            "c1": "O", "c2": "X", "c3": "X"
            }
    

    @pytest.fixture
    def get_horizontally_board_record(self) -> dict:
        return {
            "a1": "O", "a2": "O", "a3": "O", 
            "b1": "X", "b2": ".", "b3": ".", 
            "c1": "X", "c2": "X", "c3": "."
            }
    

    @pytest.fixture
    def get_incomplete_board_record(self) -> dict:
        return {
            "a1": "O", "a2": ".", "a3": "O", 
            "b1": "X", "b2": ".", "b3": ".", 
            "c1": "X", "c2": ".", "c3": "."
            }


    def test_check_if_someone_wins_diagonally_returns_true_for_user(self, get_diagonally_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_cross_diagonally("X", get_diagonally_board_record)
        assert win is True


    def test_check_if_someone_wins_diagonally_returns_false_for_robot(self, get_diagonally_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_cross_diagonally("O", get_diagonally_board_record)
        assert win is False


    def test_check_if_someone_wins_vertically_returns_true_for_user(self, get_vertically_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_vertically("X", get_vertically_board_record)
        assert win is True

    
    def test_check_if_someone_wins_vertically_returns_false_for_robot(self, get_vertically_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_vertically("O", get_vertically_board_record)
        assert win is False

    
    def test_check_if_someone_wins_horizontally_returns_false_for_user(self, get_horizontally_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_horizontally("X", get_horizontally_board_record)
        assert win is False


    def test_check_if_someone_wins_horizontally_returns_true_for_robot(self, get_horizontally_board_record: dict):
        win = self.win_inspector.check_if_someone_wins_horizontally("O", get_horizontally_board_record)
        assert win is True
    

    def test_check_if_someone_wins_returns_none(self, get_incomplete_board_record: dict):
        win = self.win_inspector.check_if_someone_wins(get_incomplete_board_record)
        assert win is None
    

    def test_check_if_someone_wins_returns_x(self, get_vertically_board_record: dict):
        win = self.win_inspector.check_if_someone_wins(get_vertically_board_record)
        assert win == "X"
    

    def test_check_if_someone_wins_returns_o(self, get_horizontally_board_record: dict):
        win = self.win_inspector.check_if_someone_wins(get_horizontally_board_record)
        assert win == "O"