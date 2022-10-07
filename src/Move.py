# same as just having a tuple of (dX, dY)

class Move:
    """
    class Move:
    Properties:
    - _RowChange: int
    - _ColumnChange: int

    Methods:
    + constructor(R: int, C: int)
    # __init__(R: int, C: int)
    + GetRowChange(): int
    + GetColumnChange(): int
    """

    _RowChange: int
    _ColumnChange: int

    def __init__(self, R: int, C: int):
        self._RowChange = R
        self._ColumnChange = C

    def GetRowChange(self) -> int:
        return self._RowChange

    def GetColumnChange(self) -> int:
        return self._ColumnChange
