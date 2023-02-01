from src.MoveOptionQueue import MoveOptionQueue


class Player:
    """
    class Player:
    Properties:
    - __Score: int
    - __Name: string
    - __Direction: int
    - __Queue: MoveOptionQueue

    Methods:
    + constructor(Name, Direction)
    # __init__(Name, Direction)
    + SameAs(APlayer: Player): bool
    + GetPlayerStateAsString(): string
    + AddToMoveOptionQueue(NewMoveOption)
    + UpdateQueueAfterMove(Position: int)
    + UpdateMoveOptionQueueWithOffer(Position, NewMoveOption)
    + GetScore(): int
    """

    __Score: int
    __Name: str
    __Direction: int
    __Queue: MoveOptionQueue

    def __init__(self, N, D):
        self.__Score = 100
        self.__Name = N
        self.__Direction = D
        self.__Queue = MoveOptionQueue()

    def SameAs(self, APlayer) -> bool:
        if APlayer is None:
            return False
        return APlayer.GetName() == self.__Name

    def GetPlayerStateAsString(self):
        return self.__Name + "\n" + "Score: " + str(
            self.__Score) + "\n" + "Move option queue: " + self.__Queue.GetQueueAsString() + "\n"

    def AddToMoveOptionQueue(self, NewMoveOption):
        self.__Queue.Add(NewMoveOption)

    def UpdateQueueAfterMove(self, Position):
        self.__Queue.MoveItemToBack(Position - 1)

    def UpdateMoveOptionQueueWithOffer(self, Position, NewMoveOption):
        self.__Queue.Replace(Position, NewMoveOption)

    def GetScore(self) -> int:
        return self.__Score

    def GetName(self):
        return self.__Name

    def GetDirection(self):
        return self.__Direction

    def ChangeScore(self, Amount):
        self.__Score += Amount

    def CheckPlayerMove(self, Pos, StartSquareReference, FinishSquareReference):
        Temp = self.__Queue.GetMoveOptionInPosition(Pos - 1)
        return Temp.CheckIfThereIsAMoveToSquare(StartSquareReference, FinishSquareReference)
