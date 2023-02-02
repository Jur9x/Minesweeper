class Solver:
    def __init__(self, board):
        self.board = board

    def move(self):
        # Projde všechny políčka v poli
        for row in self.board.getBoard():
            for piece in row:
                # Pokud není políčko zakliknuté, přeskočí ho
                if not piece.getClicked():
                    continue
                # Počítá počet bomb kolem políček
                around = piece.getNumAround()
                unknown = 0
                flagged = 0
                neighbors = piece.getNeighbors()
                for p in neighbors:
                    if not p.getClicked():
                        unknown += 1
                    if p.getFlagged():
                        flagged += 1
                # Pokud je počet bomb kolem políčka stejný jako počet označených políček, otevře neoznačené políčka
                if around == flagged:
                    self.openUnflagged(neighbors)
                # Pokud je počet bomb kolem políčka stejný jako počet neznámých políček, označí všechny políčka
                if around == unknown:
                    self.flagAll(neighbors)

    def openUnflagged(self, neighbors):
        # Otevírá všechny neoznačené políčka
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, False)