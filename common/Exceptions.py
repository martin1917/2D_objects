class MatrixCreateException(Exception):
    def __str__(self) -> str:
        return "Это не матрица"

class MultOfMatrixException(Exception):
    def __str__(self) -> str:
        return "Невозможно умножить матрицы"

class ObjectCreateException(Exception):
    def __str__(self) -> str:
        return f"Не хватает частей для создания объекта"