from Phase2.enum_tests import ExamType

# public variablen:
class Module:
    def __init__(self, module_id: str, title: str, ects: int):
        self.module_id = module_id   
        self.title = title
        self.ects = ects

class Exam:
    def __init__(self, grade: float, attempt: int):
        self.grade = grade
        self.attempt = attempt

class Module:
    def __init__(self, module_id: str, title: str, ects: int, exam_type: ExamType, exam: Exam = None):
        self.module_id = module_id
        self.title = title
        self.ects = ects
        self.exam_type = exam_type
        self.exam = exam  # Komposition: gehört fest zum Modul, max. 0..1

class Semester:
    def __init__(self, number: int):
        self.number = number
        self.modules = []  # Aggregation: Module können zugeordnet, aber auch ohne Semester existieren

class Exam:
    def __init__(self, grade):
        self.grade = grade

class Klausur(Exam):
    pass