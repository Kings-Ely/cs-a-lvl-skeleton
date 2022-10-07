from src.Piece import Piece
from src.Player import Player


class Square:
    """
    Class Square:
    Properties:
    - _PieceInSquare: None | Piece
    - _BelongsTo: None | Player
    - _Symbol

    Methods:
    + constructor()
    # __init__()
    + SetPiece(): None
    + RemovePiece(): Piece
    + GetPieceInSquare(): None | Piece
    + GetSymbol(): string
    + GetPointsForOccupancy(CurrentPlayer): int
    + GetBelongsTo(): Player
    + ContainsKotla(): bool
    """

    _PieceInSquare: Piece | None
    _BelongsTo: Player | None
    _Symbol: str

    def __init__(self):
        self._PieceInSquare = None
        self._BelongsTo = None
        self._Symbol = " "

    def SetPiece(self, P):
        self._PieceInSquare = P

    def RemovePiece(self):
        PieceToReturn = self._PieceInSquare
        self._PieceInSquare = None
        return PieceToReturn

    def GetPieceInSquare(self):
        return self._PieceInSquare

    def GetSymbol(self):
        return self._Symbol

    def GetPointsForOccupancy(self, CurrentPlayer: Player) -> int:
        return 0

    def GetBelongsTo(self):
        return self._BelongsTo

    def ContainsKotla(self):
        return False


class Kotla(Square):
    """
    Class Kotla extends Square:
    Properties:
    - _BelongsTo
    - _Symbol

    Methods:
    + constructor(P, S)
    + GetPointsForOccupancy(CurrentPlayer)
    + ContainsKotla()
    """
    _BelongsTo: Player
    _Symbol: str

    def __init__(self, P: Player, S: str):
        super(Kotla, self).__init__()
        self._BelongsTo = P
        self._Symbol = S

    def GetPointsForOccupancy(self, CurrentPlayer: Player) -> int:
        if self._PieceInSquare is None:
            return 0
        elif self._BelongsTo.SameAs(CurrentPlayer):
            if CurrentPlayer.SameAs(self._PieceInSquare.GetBelongsTo()) and (
                    self._PieceInSquare.GetTypeOfPiece() == "piece" or self._PieceInSquare.GetTypeOfPiece() == "mirza"):
                return 5
            else:
                return 0
        else:
            if CurrentPlayer.SameAs(self._PieceInSquare.GetBelongsTo()) and (
                    self._PieceInSquare.GetTypeOfPiece() == "piece" or self._PieceInSquare.GetTypeOfPiece() == "mirza"):
                return 1
            else:
                return 0

    def ContainsKotla(self) -> bool:
        return self._Symbol == "K" or self._Symbol == "k"
