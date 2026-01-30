from student import Student

def test_grade_A():
    s = Student("001", "Test", 85)
    assert s.grade() == "A"

def test_grade_B():
    s = Student("002", "Test", 75)
    assert s.grade() == "B"

def test_grade_C():
    s = Student("003", "Test", 65)
    assert s.grade() == "C"

def test_grade_D():
    s = Student("004", "Test", 55)
    assert s.grade() == "D"

def test_grade_F():
    s = Student("005", "Test", 40)
    assert s.grade() == "F"
