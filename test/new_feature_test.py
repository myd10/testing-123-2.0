#this is to test the new feature

from app.new_feature import announce

def test_new_feature():
    result = announce()
    assert result == "Hello World"
