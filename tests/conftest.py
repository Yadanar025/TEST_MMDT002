import pytest
from src.student_manager import Student, StudentManager



#empty
@pytest.fixture
def empty_manager():
    return StudentManager()

#sample
@pytest.fixture
def sample_student():
    return Student(student_id="MMDT002",name="Yadanar",email="aung@gmail.com")

#populate
@pytest.fixture
def populated_manager():
    student = StudentManager()
    student.add_student("MMDT001","Aye", "aye@gmail.com")
    student.add_student("MMDT002","Aung", "aung@gmail.com")
    student.add_student("MMDT003","Su", "su@gmail.com")
    student.add_student("MMDT004","Sat", "sat@gmail.com")
    student.add_student("MMDT005","Hla", "hla@gmail.com")
    student.add_student("MMDT006","Kyaw", "kyaw@gmail.com")

    student.update_grade("MMDT001","PHYSIS",99) #high
    student.update_grade("MMDT002","PHYSIS",80) #high
    student.update_grade("MMDT003","PHYSIS",70) #mid
    student.update_grade("MMDT004","PHYSIS",72) #mid
    student.update_grade("MMDT005","PHYSIS",40) #low
    student.update_grade("MMDT006","PHYSIS",44) #low
    return student

@pytest.fixture
def valid_registration_data():
    return {"username":"Yadanar","email":"aung@gmail.com", "password": "Str0ng!Pass", "age": 30}