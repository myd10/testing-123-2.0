#testing-123.20/my_test.py

from my_script import enlarge

def test_enlarge():
    result = enlarge(3)
    assert result == 300
