from src.data_validator import InvalidEmailError, WeakPasswordError, InvalidUsernameError, InvalidAgeError, ValidationError, validate_email, validate_password, validate_username, validate_age, validate_registration
import pytest

#email
@pytest.mark.parametrize("email,expected",
[
    ("aung@gmail.com",True), #correct
    ("aung@yahoo.co.com",True), #correct
    ("aung+yadanar@gmail.com",True), #correct
])
def test_email(email,expected):
    assert validate_email(email) == expected

@pytest.mark.parametrize("email,expected",
[
    ("",InvalidEmailError),  #empty
    ("aunggmail.com",InvalidEmailError), #@miss
    ("user@gmail",InvalidEmailError), #missing .com
    ("user@gmail..com",InvalidEmailError), #additional ..
    ("user @gmail.com",InvalidEmailError), #additional space
    (123,TypeError) #number

])

def test_email_invalid(email,expected):
    with pytest.raises(expected):
        validate_email(email)


#password
@pytest.mark.parametrize("password,expected",
[
    ("Str0ng!Pass",True), #correct
])
def test_password(password,expected):
    assert validate_password(password) == expected

@pytest.mark.parametrize("password,expected",
[
    ("Sh0rt",WeakPasswordError),  #weak
    ("A1!" + "a"*128,WeakPasswordError), #many char
    ("lower1!only",WeakPasswordError), #Lower
    ("UPPER1!ONLY",WeakPasswordError), #Upper 
    ("NoDigits!",WeakPasswordError), #No Number
    ("Has Space1!",WeakPasswordError), #have space
    (123456,TypeError) #number only

])

def test_user_invalid(password,expected):
    with pytest.raises(expected):
        validate_password(password)


#username
@pytest.mark.parametrize("name,expected",
[
    ("Aung",True), #correct
    ("a"*20,True), #20 char
    ("Aung_01",True)
])
def test_username(name,expected):
    assert validate_username(name) == expected

@pytest.mark.parametrize("name,expected",
[
    ("ab",InvalidUsernameError),  #less than 3 char
    ("a"*21,InvalidUsernameError), #more than 20 char
    ("1aung",InvalidUsernameError), #start with number
    ("_aung",InvalidUsernameError), #start with _ 
    ("aung!",InvalidUsernameError), #include special char
    ("Au ng",InvalidUsernameError), #include space
    (123456,TypeError) #number only

])

def test_name_invalid(name,expected):
    with pytest.raises(expected):
        validate_username(name)


#age
@pytest.mark.parametrize("age,expected",
[
    (13,True), #correct
    (120,True), #120 
    (34,True)
])
def test_age(age,expected):
    assert validate_age(age) == expected

@pytest.mark.parametrize("age,expected",
[
    (12,InvalidAgeError),  #less than 13
    (121,InvalidAgeError), #more than 120 
    (13.5,TypeError), #float 
    (True,TypeError), #boolean

])

def test_age_invalid(age,expected):
    with pytest.raises(expected):
        validate_age(age)

#validate regristeration
base_user = {"username": "Aung01", "email": "aung@gmail.com", "password": "Str0ng!Pass", "age": 30}
missing_age = {k: v for k, v in base_user.items() if k != "age"}
bad_age = {**base_user, "age": -5}

def test_registration():
    assert validate_registration(base_user) == True

@pytest.mark.parametrize("registeration,expected",
[
    (missing_age,ValidationError),  #less than 13
    (bad_age,InvalidAgeError), #more than 120 
    ("Not a dict",TypeError), #float 
])

def test_registeration_invalid(registeration,expected):
    with pytest.raises(expected):
        validate_registration(registeration)

def test_password_nospecial_char(sample_student=None):
    with pytest.raises(WeakPasswordError):
        validate_password("NoSpecial1")
