from main import str_most_freq_helper


def test_normal_string():
    normal_string = "normal string"
    assert str_most_freq_helper(normal_string) == {
        "frequency": 2,
        "most_frequent_key": "r",
    }


def test_empty_string():
    empty_str = ""
    assert str_most_freq_helper(empty_str) is None


def test_symbol_string():
    symbol_string = ",,,,,,,....."
    assert str_most_freq_helper(symbol_string) == {
        "frequency": 7,
        "most_frequent_key": ",",
    }
