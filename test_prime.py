from prime import isPrime
import pytest

@pytest.mark.parametrize("num, expected",[
    (1,False),
    (2,True),
    (3,True),
    (4,False),
    (5,True),
    (16,False),
    (17,True),
    (18,False),
    (19,True),
    (20,False)
])
def test_is_prime(num,expected):
    assert isPrime(num)==expected