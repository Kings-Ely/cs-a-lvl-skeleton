import random

from src.Player import Player
from src.Square import Square, Kotla
from src.Piece import Piece
from src.Move import Move
from src.MoveOption import MoveOption


class Dastan:
    """
    class Dastan:
    Properties:
    # _Board: list
    # _Players: list
    # _MoveOptionOffer: list
    # _NoOfRows: int
    # _NoOfColumns: int
    # _MoveOptionOfferPosition: int
    # _CurrentPlayer: Player

    Methods:
    + PlayGame(): void
    + constructor(rows: int, columns: int, NoOfPieces: int)
    # __init__(rows: int, columns: int, NoOfPieces: int)
    - __DisplayBoard()
    - __DisplayState()
    - __GetIndexOfSquare(SquareReference: int): int
    - __CheckSquareInBounds(SquareReference: int): bool
    - __CheckSquareIsValid(SquareReference: int, StartSquare: bool): bool
    - __CheckIfGameOver(): bool
    - __GetSquareReference(message: str): int
    - __UseMoveOptionOffer()
    - __GetPointsForOccupancyByPlayer(CurrentPlayer: Player): int
    - __UpdatePlayerScore(PointsForPieceCapture: int)
    - __CalculatePieceCapturePoints(FinishSquareReference: int)
    """

    _Board: list
    _Players: list[Player]
    _MoveOptionOffer: list[str]
    _NoOfRows: int
    _NoOfColumns: int
    _MoveOptionOfferPosition: int
    _CurrentPlayer: Player

    def __init__(self, rows: int, columns: int, NoOfPieces: int):
        self._Board = []
        self._Players = [
            Player("Player One", 1),
            Player("Player Two", -1)
        ]
        self._MoveOptionOffer = []
        self.__CreateMoveOptions()
        self._NoOfRows = rows
        self._NoOfColumns = columns
        self._MoveOptionOfferPosition = 0
        self.__CreateMoveOptionOffer()
        self.__CreateBoard()
        self.__CreatePieces(NoOfPieces)
        self._CurrentPlayer = self._Players[0]

    def PlayGame(self) -> None:
        GameOver = False
        # keep running this loop until the game exits
        while not GameOver:

            # 'print' the current state of the game
            self.__DisplayState()

            SquareIsValid = False
            Choice = 0
            while Choice < 1 or Choice > 3:
                Choice = int(input("Choose move option to use from queue (1 to 3) or 9 to take the offer: "))
                if Choice == 9:
                    self.__UseMoveOptionOffer()
                    self.__DisplayState()

            while not SquareIsValid:
                StartSquareReference = self.__GetSquareReference("containing the piece to move")
                SquareIsValid = self.__CheckSquareIsValid(StartSquareReference, True)

            SquareIsValid = False

            while not SquareIsValid:
                FinishSquareReference = self.__GetSquareReference("to move to")
                SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)

            MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)

            if MoveLegal:
                PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
                self._CurrentPlayer.ChangeScore(-(Choice + (2 * (Choice - 1))))
                self._CurrentPlayer.UpdateQueueAfterMove(Choice)
                self.__UpdateBoard(StartSquareReference, FinishSquareReference)
                self.__UpdatePlayerScore(PointsForPieceCapture)
                print("New score: " + str(self._CurrentPlayer.GetScore()) + "\n")

            if self._CurrentPlayer.SameAs(self._Players[0]):
                self._CurrentPlayer = self._Players[1]
            else:
                self._CurrentPlayer = self._Players[0]

            GameOver = self.__CheckIfGameOver()
        self.__DisplayState()
        self.__DisplayFinalResult()

    def __DisplayBoard(self) -> None:
        print("\n" + "   ", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print(str(Column) + "  ", end="")
        print("\n" + "  ", end="")
        for Count in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print("-")
        for Row in range(1, self._NoOfRows + 1):
            print(str(Row) + " ", end="")
            for Column in range(1, self._NoOfColumns + 1):
                Index = self.__GetIndexOfSquare(Row * 10 + Column)
                print("|" + self._Board[Index].GetSymbol(), end="")
                PieceInSquare = self._Board[Index].GetPieceInSquare()
                if PieceInSquare is None:
                    print(" ", end="")
                else:
                    print(PieceInSquare.GetSymbol(), end="")
            print("|")
        print("  -", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print()
        print()

    def __DisplayState(self) -> None:
        self.__DisplayBoard()
        print("Move option offer: " + self._MoveOptionOffer[self._MoveOptionOfferPosition])
        print()
        print(self._CurrentPlayer.GetPlayerStateAsString())
        print("Turn: " + self._CurrentPlayer.GetName())
        print()

    def __GetIndexOfSquare(self, SquareReference: int) -> int:
        Row = SquareReference // 10
        Col = SquareReference % 10
        return (Row - 1) * self._NoOfColumns + (Col - 1)

    def __CheckSquareInBounds(self, SquareReference: int) -> bool:
        Row = SquareReference // 10
        Col = SquareReference % 10
        if Row < 1 or Row > self._NoOfRows:
            return False
        elif Col < 1 or Col > self._NoOfColumns:
            return False
        else:
            return True

    def __CheckSquareIsValid(self, SquareReference: int, StartSquare: int) -> bool:
        if not self.__CheckSquareInBounds(SquareReference):
            return False
        PieceInSquare = self._Board[self.__GetIndexOfSquare(SquareReference)].GetPieceInSquare()
        if PieceInSquare is None:
            return not StartSquare
        elif self._CurrentPlayer.SameAs(PieceInSquare.GetBelongsTo()):
            return not not StartSquare
        else:
            return not StartSquare

    def __CheckIfGameOver(self) -> bool:
        Player1HasMirza = False
        Player2HasMirza = False
        for S in self._Board:
            PieceInSquare = S.GetPieceInSquare()
            if PieceInSquare is not None:
                if S.ContainsKotla() and PieceInSquare.GetTypeOfPiece() == "mirza" and not PieceInSquare.GetBelongsTo().SameAs(
                        S.GetBelongsTo()):
                    return True
                elif PieceInSquare.GetTypeOfPiece() == "mirza" and PieceInSquare.GetBelongsTo().SameAs(
                        self._Players[0]):
                    Player1HasMirza = True
                elif PieceInSquare.GetTypeOfPiece() == "mirza" and PieceInSquare.GetBelongsTo().SameAs(
                        self._Players[1]):
                    Player2HasMirza = True
        return not (Player1HasMirza and Player2HasMirza)

    def __GetSquareReference(self, Description: str) -> int:
        SelectedSquare = int(input("Enter the square " + Description + " (row number followed by column number): "))
        return SelectedSquare

    def __UseMoveOptionOffer(self) -> None:
        ReplaceChoice = int(input("Choose the move option from your queue to replace (1 to 5): "))
        self._CurrentPlayer.UpdateMoveOptionQueueWithOffer(ReplaceChoice - 1, self.__CreateMoveOption(
            self._MoveOptionOffer[self._MoveOptionOfferPosition], self._CurrentPlayer.GetDirection()))
        self._CurrentPlayer.ChangeScore(-(10 - (ReplaceChoice * 2)))
        self._MoveOptionOfferPosition = random.randint(0, 4)

    def __GetPointsForOccupancyByPlayer(self, CurrentPlayer: Player) -> int:
        ScoreAdjustment = 0
        for S in self._Board:
            ScoreAdjustment += (S.GetPointsForOccupancy(CurrentPlayer))
        return ScoreAdjustment

    def __UpdatePlayerScore(self, PointsForPieceCapture: int) -> None:
        self._CurrentPlayer.ChangeScore(
            self.__GetPointsForOccupancyByPlayer(self._CurrentPlayer) + PointsForPieceCapture)

    def __CalculatePieceCapturePoints(self, FinishSquareReference: int) -> int:
        if self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare() is not None:
            return self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare().GetPointsIfCaptured()
        return 0

    def __UpdateBoard(self, StartSquareReference: int, FinishSquareReference: int):
        self._Board[self.__GetIndexOfSquare(FinishSquareReference)].SetPiece(
            self._Board[self.__GetIndexOfSquare(StartSquareReference)].RemovePiece())

    def __DisplayFinalResult(self):
        if self._Players[0].GetScore() == self._Players[1].GetScore():
            print("Draw!")
        elif self._Players[0].GetScore() > self._Players[1].GetScore():
            print(self._Players[0].GetName() + " is the winner!")
        else:
            print(self._Players[1].GetName() + " is the winner!")

    def __CreateBoard(self):
        for Row in range(1, self._NoOfRows + 1):
            for Column in range(1, self._NoOfColumns + 1):
                if Row == 1 and Column == self._NoOfColumns // 2:
                    S = Kotla(self._Players[0], "K")
                elif Row == self._NoOfRows and Column == self._NoOfColumns // 2 + 1:
                    S = Kotla(self._Players[1], "k")
                else:
                    S = Square()
                self._Board.append(S)

    def __CreatePieces(self, NoOfPieces: int) -> None:
        for Count in range(1, NoOfPieces + 1):
            CurrentPiece = Piece("piece", self._Players[0], 1, "!")
            self._Board[self.__GetIndexOfSquare(2 * 10 + Count + 1)].SetPiece(CurrentPiece)
        CurrentPiece = Piece("mirza", self._Players[0], 5, "1")
        self._Board[self.__GetIndexOfSquare(10 + self._NoOfColumns // 2)].SetPiece(CurrentPiece)
        for Count in range(1, NoOfPieces + 1):
            CurrentPiece = Piece("piece", self._Players[1], 1, '"')
            self._Board[self.__GetIndexOfSquare((self._NoOfRows - 1) * 10 + Count + 1)].SetPiece(CurrentPiece)
        CurrentPiece = Piece("mirza", self._Players[1], 5, "2")
        self._Board[self.__GetIndexOfSquare(self._NoOfRows * 10 + (self._NoOfColumns // 2 + 1))].SetPiece(CurrentPiece)

    def __CreateMoveOptionOffer(self) -> None:
        self._MoveOptionOffer.append("jazair")
        self._MoveOptionOffer.append("chowkidar")
        self._MoveOptionOffer.append("cuirassier")
        self._MoveOptionOffer.append("ryott")
        self._MoveOptionOffer.append("faujdar")

    def __CreateRyottMoveOption(self, Direction: int) -> MoveOption:
        NewMoveOption = MoveOption("ryott")
        NewMove = Move(0, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateFaujdarMoveOption(self, Direction: int) -> MoveOption:
        NewMoveOption = MoveOption("faujdar")
        NewMove = Move(0, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateJazairMoveOption(self, Direction: int) -> MoveOption:
        NewMoveOption = MoveOption("jazair")
        NewMove = Move(2 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2 * Direction, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2 * Direction, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateCuirassierMoveOption(self, Direction: int) -> MoveOption:
        NewMoveOption = MoveOption("cuirassier")
        NewMove = Move(1 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateChowkidarMoveOption(self, Direction: int) -> MoveOption:
        NewMoveOption = MoveOption("chowkidar")
        NewMove = Move(1 * Direction, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateMoveOption(self, Name: str, Direction: int) -> MoveOption:
        if Name == "chowkidar":
            return self.__CreateChowkidarMoveOption(Direction)
        elif Name == "ryott":
            return self.__CreateRyottMoveOption(Direction)
        elif Name == "faujdar":
            return self.__CreateFaujdarMoveOption(Direction)
        elif Name == "jazair":
            return self.__CreateJazairMoveOption(Direction)
        else:
            return self.__CreateCuirassierMoveOption(Direction)

    def __CreateMoveOptions(self) -> None:
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("ryott", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("chowkidar", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("cuirassier", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("faujdar", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("jazair", 1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("ryott", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("chowkidar", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("jazair", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("faujdar", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("cuirassier", -1))
