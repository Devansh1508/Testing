from main import get_weather
from main import add, divide
import pytest

def test_get_weather():
    assert get_weather(21)=="Warm"
    assert get_weather(15)=="Cold"


def test_add():
    assert add(2,3)==5
    assert add(1,-1)==0
    # assert add(2,3)==5


def test_divide():
    with pytest.raises(ValueError,match="divide by zero"):
        divide(10/0)
    
    