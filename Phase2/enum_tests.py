from enum import Enum

class Degree(Enum):
    BSC = "Bachelor"
    MSC = "Master"
    PHD = "PhD"

class ExamType(Enum):
    KLAUSUR = "Klausur"
    PORTFOLIO = "Portfolio"