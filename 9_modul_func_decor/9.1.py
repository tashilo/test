def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == 'grade':
        return get_grade
    elif option == 'description':
        return get_description
    else:
        return None
    
print(get_student_grade("grade")) # Вызовет функцию get_grade
print(get_student_grade("description")) # Вызовет функцию get_description
print(get_student_grade(3)) # Вернет None
print(get_student_grade("Satisfactorily")) # Вернет None