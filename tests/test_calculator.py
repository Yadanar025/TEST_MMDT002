import pytest
from src.calculator import calculate_average, find_maximum, is_prime, factorial, power


def test_calculate_average():
    assert calculate_average([70,80,90])==80

def test_average_emptylist():
    with pytest.raises(ValueError):
        calculate_average([])

@pytest.mark.parametrize("scores,expected",
[
    ([1,2,3],2), #correct
    ([0,1,2,3,4,5,6,7,8,9,10],5),  #correct
])
def test_average(scores,expected):
    assert calculate_average(scores) == expected

@pytest.mark.parametrize("scores,expected",
[
    ([-1,1,0],ValueError),  #negpos
    (['a',0,1],TypeError), #string error
    ([True,2,3],TypeError), #boolean
    ("abc",TypeError),  #string
    ([10,1,150], ValueError) #over100
])

def test_average_invalid(scores,expected):
    with pytest.raises(expected):
        calculate_average(scores)


#maximum
@pytest.mark.parametrize("scores,expected",
[
    ([3,8,5],8), #correct
    ([0,-2,-4,1,2],2),  #correct
    ([-1,-2,-4],-1),  #correct
    ([6],6),
    ([7,7,1,3,4],7)
])
def test_maximum(scores,expected):
    assert find_maximum(scores) == expected

@pytest.mark.parametrize("scores,expected",
[
    ([],ValueError),  #empty
    ("abc",TypeError),  #string
    (['a',0,1],TypeError), #string error
    ([True,2,3],TypeError), #boolean
])

def test_maximum_invalid(scores,expected):
    with pytest.raises(expected):
        find_maximum(scores)

#prime
@pytest.mark.parametrize("scores,expected",
[
    (-1,False), #correct
    (0,False), #correct
    (2,True), #correct
    (1,False), #correct
    (3,True), #correct
    (4,False), #correct
    (9,False), #correct
    (15,False), #correct
    (25,False), #correct
    (29,True), #correct
    (49,False), #correct
    (97,True), #correct
    (7,True), #correct
    (5,True), #correct
    (63,False) #correct
])
def test_prime(scores,expected):
    assert is_prime(scores) == expected

@pytest.mark.parametrize("scores,expected",
[
    ([],TypeError),  #empty
    ("abc",TypeError),  #string
    (3.5,TypeError), #string error
    (True,TypeError), #boolean
])

def test_prime_invalid(scores,expected):
    with pytest.raises(expected):
        is_prime(scores)

#factorial
@pytest.mark.parametrize("scores,expected",
[
    (0,1), #correct
    (1,1), #correct
    (5,120), #correct
    (3,6), #correct
])
def test_factorial(scores,expected):
    assert factorial(scores) == expected

@pytest.mark.parametrize("scores,expected",
[
    (-1,ValueError),  #empty
    (3.5,TypeError),  #string
    ("a",TypeError), #string error
    (True,TypeError), #boolean
])

def test_factorial_invalid(scores,expected):
    with pytest.raises(expected):
        factorial(scores)

#power
@pytest.mark.parametrize("scores,expected",
[
    ((2,3),8), #correct
    ((5,2),25), #correct
    ((7,0),1), #correct
    ((0,0),1), #correct
    ((2,-1),0.5), #correct
    ((-2,2),4) #correct
])
def test_power(scores,expected):
    assert power(*scores) == expected

@pytest.mark.parametrize("scores,expected",
[
    ((0,-1),ValueError),  #string
    ("a",TypeError), #string error
    ((2,3.5),TypeError), #float
    ((True,2),TypeError), #boolean
    ((2,True),TypeError) #boolean
])

def test_power_invalid(scores,expected):
    with pytest.raises(expected):
        power(*scores)