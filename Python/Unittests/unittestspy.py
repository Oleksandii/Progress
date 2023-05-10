import pytest
from unittests import square , hello

############ top method with pytest for now
def test_hello():
    assert hello('David')=='Hello David'

def test_positive():
    assert square(8)== 64
    assert square(10)== 100
def test_negative():
    assert square(-5)== 25
    assert square(-3)== 9
def test_zero():
    assert square(0)== 0
def test_str():
    with pytest.raises(TypeError):
        square('cat')






############ pytest retriew only 1 problem (running by pytest <name of file> in dirictory)
def testbypytest():
    assert square(8)== 64
    assert square(10)== 100
    assert square(9)== 81
    assert square(-1)== 1
    assert square(0)== 0


######## Dumb method with a lot of code 

def test():
    try:
        assert square(8)== 64
        
    except AssertionError:
        print('Square function working not properly 8*8!=64')
    try:
        assert square(10) == 100
    except AssertionError:
        print('Square function working not properly 10*10 !=100')
