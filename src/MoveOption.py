from src.Move import Move


class MoveOption:
    """
    class MoveOption:
    Properties:
    - _Name: string
    - _PossibleMoves: Move[]

    Methods:
    + constructor(N: string)
    # __init__(N: string)
    + AddToPossibleMoves(M: Move)
    + CheckIfThereIsAMoveToSquare(StartSquareReference: int, FinishSquareReference: int): bool
    + GetName(): string
    """

    _Name: str
    _PossibleMoves: list[Move]

    def __init__(self, name: str):
        self._Name = name
        self._PossibleMoves = []

    def AddToPossibleMoves(self, move: Move) -> None:
        self._PossibleMoves.append(move)

    def GetName(self) -> str:
        return self._Name

    def CheckIfThereIsAMoveToSquare(self, StartSquareReference: int, FinishSquareReference: int) -> bool:
        StartRow = StartSquareReference // 10
        StartColumn = StartSquareReference % 10
        FinishRow = FinishSquareReference // 10
        FinishColumn = FinishSquareReference % 10
        for M in self._PossibleMoves:
            if StartRow + M.GetRowChange() == FinishRow and StartColumn + M.GetColumnChange() == FinishColumn:
                return True
        return False
