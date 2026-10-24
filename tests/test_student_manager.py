from src.student_manager import StudentManager,Student
import pytest

def test_add_grade_valid(sample_student):
    sample_student.add_grade("MATH101",85)
    assert sample_student.grades["MATH101"]==85

def test_student_valid_construction():
    s = Student("MMDT01","Aung","aung@gmail.com")
    assert s.student_id == "MMDT01"
    assert s.name == "Aung"
    assert s.email == "aung@gmail.com"

def test_student_invalid_empty_id():
    with pytest.raises(ValueError):
        Student("", "Aung", "aung@gmail.com")

def test_student_invalid_empty_nonstring():
    with pytest.raises(ValueError):
        Student(123, "Aung", "aung@gmail.com")

def test_student_invalid_name():
    with pytest.raises(ValueError):
        Student("MMDT01", "", "aung@gmail.com")

def test_student_invalid_email():
    with pytest.raises(ValueError):
        Student("MMDT01", "Aung", "")

def test_student_invalid_email_format():
    with pytest.raises(ValueError):
        Student("MMDT01", "Aung", "aunggmail.com")


#grade
@pytest.mark.parametrize("course,scores",
[
    ("PHYSIS",85), #correct
    ("PHYSIS",0), #correct
    ("PHYSIS",100), #correct
])
def test_grade(sample_student,course,scores):
    sample_student.add_grade(course,scores)
    assert sample_student.grades[course] == float(scores)

@pytest.mark.parametrize("course,scores,expected",
[
    ("PHYSIS",-1,ValueError),  #under0
    ("PHYSIS",101,ValueError), #over100
    ("",85,ValueError), #no course
    ("PHYSIS","a",TypeError), #string
    ("PHYSIS",True,TypeError), #Boolean
])

def test_average_invalid(sample_student,course,scores,expected):
    with pytest.raises(expected):
        sample_student.add_grade(course,scores)

#gpa
@pytest.mark.parametrize("score,expected", [
    (95, 4.0),
    (85, 3.0),
    (75, 2.0),
    (65, 1.0),
    (50, 0.0),
])
def test_gpa(sample_student, score, expected):
    sample_student.add_grade("PHYSICS", score)
    assert sample_student.get_gpa() == expected

def test_gpa_no_grades(sample_student):
    assert sample_student.get_gpa() == 0.0

def test_gpa_multiple_courses(sample_student):
    sample_student.add_grade("PHYSICS", 95)
    sample_student.add_grade("MATH", 75)
    assert sample_student.get_gpa() == 3.0


def test_add_student_by_params(empty_manager):
    empty_manager.add_student("S2","Su","su@gmail.com")
    assert empty_manager.get_total_students()==1

def test_add_duplicate_id(empty_manager):
    empty_manager.add_student("S1", "Aung", "aung@gmail.com")
    with pytest.raises(ValueError):
        empty_manager.add_student("S1", "Aung", "aung@gmail.com")

def test_add_student_missing_name(empty_manager):
    with pytest.raises(ValueError):
        empty_manager.add_student("S3")

def test_add_student_by_instance(empty_manager):
    s = Student("S1","Aung","aung@gmail.com")
    empty_manager.add_student(s)
    assert empty_manager.get_total_students()==1


def test_get_student(populated_manager):
    student = populated_manager.get_student("MMDT001")
    assert student.student_id == "MMDT001"

def test_get_student_not_found(populated_manager):
    with pytest.raises(KeyError):
        populated_manager.get_student("UNKNOWN")

def test_update_grade(populated_manager):
    gpa = populated_manager.update_grade("MMDT003", "CHEM101", 95)
    assert gpa == 3.0

def test_update_grade_not_found(populated_manager):
    with pytest.raises(KeyError):
        populated_manager.update_grade("UNKNOWN", "CHEM101", 90)

def test_remove_student(populated_manager):
    count_before = populated_manager.get_total_students()
    populated_manager.remove_student("MMDT001")
    assert populated_manager.get_total_students() == count_before - 1    
    with pytest.raises(KeyError):
        populated_manager.get_student("MMDT001")

def test_remove_student_not_found(populated_manager):
    with pytest.raises(KeyError):
        populated_manager.remove_student("UNKNOWN")

def test_top_gpa3(populated_manager):
    top3 = populated_manager.get_top_performers(3)
    ids = [s.student_id for s in top3]
    assert ids==["MMDT001","MMDT002","MMDT003"]

def test_top_gpa2(populated_manager):
    top2 = populated_manager.get_top_performers(2)
    ids = [s.student_id for s in top2]
    assert ids==["MMDT001","MMDT002"]

def test_top_performerszero(populated_manager):
    with pytest.raises(ValueError):
        populated_manager.get_top_performers(0)

def test_top_performersneg(populated_manager):
    with pytest.raises(ValueError):
        populated_manager.get_top_performers(-1)

def test_filter_min_gpa(populated_manager):
    min = populated_manager.filter_by_min_gpa(3.0)
    ids = {s.student_id for s in min}
    assert ids == {"MMDT001","MMDT002"}

def test_filter_mingpa_zero(populated_manager):
    min = populated_manager.filter_by_min_gpa(0.0)
    assert len(min) == 6

def test_filter_min_gpa_max(populated_manager):
    max = populated_manager.filter_by_min_gpa(4.0)
    ids = {s.student_id for s in max}
    assert ids == {"MMDT001"}

def test_filter_mingpa_neg(populated_manager):
    with pytest.raises(ValueError):
        populated_manager.filter_by_min_gpa(-0.1)

def test_filter_mingpa_over(populated_manager):
    with pytest.raises(ValueError):
        populated_manager.filter_by_min_gpa(4.1)

