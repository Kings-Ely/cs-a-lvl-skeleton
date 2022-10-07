from src.MoveOption import MoveOption


class MoveOptionQueue:
    """
    class MoveOptionQueue:
    Properties:
    - __Queue: MoveOption[]

    Methods:
    + constructor()
    # __init__()
    + Add(NewMoveOption)
    + Replace(Position, NewMoveOption)
    + MoveItemToBack(Position)
    + GetMoveOptionInPosition(Pos): MoveOption
    + GetQueueAsString(): string
    """

    __Queue: list[MoveOption]

    def __init__(self):
        self.__Queue = []

    def GetQueueAsString(self) -> str:
        QueueAsString = ""
        Count = 1
        for M in self.__Queue:
            QueueAsString += str(Count) + ". " + M.GetName() + "   "
            Count += 1
        return QueueAsString

    def Add(self, NewMoveOption: MoveOption) -> None:
        self.__Queue.append(NewMoveOption)

    def Replace(self, Position: int, NewMoveOption: MoveOption) -> None:
        self.__Queue[Position] = NewMoveOption

    def MoveItemToBack(self, Position: int) -> None:
        Temp = self.__Queue[Position]
        self.__Queue.pop(Position)
        self.__Queue.append(Temp)

    def GetMoveOptionInPosition(self, Pos: int) -> MoveOption:
        return self.__Queue[Pos]
