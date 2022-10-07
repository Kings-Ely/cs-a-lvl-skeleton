from src.Player import Player


class Piece:
    """
    Class Piece:
    Properties:
    - _TypeOfPiece: string
    - _BelongsTo: Player
    - _PointsIfCaptured: number
    - _Symbol: string

    Methods:
    + constructor(TypeOfPiece, BelongsTo, PointsIfCaptured, Symbol)
    # __init__(TypeOfPiece, BelongsTo, PointsIfCaptured, Symbol)
    + GetSymbol(): string
    + GetTypeOfPiece(): string
    + GetBelongsTo(): Player
    + GetPointsIfCaptured(): number
    """

    _TypeOfPiece: str
    _BelongsTo: Player
    _PointsIfCaptured: int
    _Symbol: str

    def __init__(self, T: str, B: Player, P: int, S: str):
        self._TypeOfPiece = T
        self._BelongsTo = B
        self._PointsIfCaptured = P
        self._Symbol = S

    def GetSymbol(self) -> str:
        return self._Symbol

    def GetTypeOfPiece(self) -> str:
        return self._TypeOfPiece

    def GetBelongsTo(self) -> Player:
        return self._BelongsTo

    def GetPointsIfCaptured(self) -> int:
        return self._PointsIfCaptured
