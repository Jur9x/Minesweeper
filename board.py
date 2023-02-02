import random
from piece import Piece
# importy

class Board:
    def __init__(self, size, prob):
        # Velikost pole
        self.size = size
        # Seznam seznamů, kde každý podseznam reprezentuje řádek na plánu
        self.board = []
        # Boolean proměnná, která udává, jestli hráč vyhrál
        self.won = False
        # Boolean proměnná, která udává, jestli hráč prohrál
        self.lost = False
        # Vygenerování pole s náhodnými minami
        for row in range(size[0]):
            row = []
            for col in range(size[1]):
                # Náhodné určení, jestli na této pozici bude mína
                bomb = random.random() < prob
                piece = Piece(bomb)
                row.append(piece)
            self.board.append(row)
        # Nastavení sousedů pro všechny políčka na poli
        self.setNeighbors()
        # Nastavení počtu min okolo každého políčka
        self.setNumAround()

    # Funkce pro výpis pole
    def print(self):
        for row in self.board:
            for piece in row:
                print(piece, end=" ")
            print()

    # Funkce, která vrátí seznam se seznamy reprezentujícími jednotlivé řádky plánu
    def getBoard(self):
        return self.board

    # Funkce, která vrátí velikost pole
    def getSize(self):
        return self.size

    # Funkce, která vrátí políčko na zadané pozici
    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    # Funkce pro provedení tahu na zadané pozici s možností označení/odznačení miny
    def handleClick(self, piece, flag):
        # Pokud je políčko již otevřený nebo je označený a nemá označení
        if piece.getClicked() or (piece.getFlagged() and not flag):
            return
        # Pokud je zadáno označení/odznačení miny
        if flag:
            piece.toggleFlag()
            return
        piece.handleClick()
        # Pokud není okolo žádná bomba
        if piece.getNumAround() == 0:
            for neighbor in piece.getNeighbors():
                self.handleClick(neighbor, False)
       # Pokud má bombu
        if piece.getHasBomb():
            self.lost = True
        else:
            self.won = self.checkWon()

    def checkWon(self):
        # Kontroluje, jestli byly kliknuty všechny políčka bez bomb
        for row in self.board:
            for piece in row:
                if not piece.getHasBomb() and not piece.getClicked():
                    # Pokud je nějaké políčko bez bomby, které nebylo zakliknuté, vraťí False
                    return False
        # Všechny políčka bez bomb byly zakliknuty, vraťí True
        return True

    def getWon(self):
        # Získá hodnotu atributu 'won'
        return self.won

    def getLost(self):
        # Získá hodnotu atributu 'lost'
        return self.lost

    def setNeighbors(self):
        # Projde všechny políčka na poli
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.board[row][col]
                neighbors = []
                # Najde všechny sousedy pro aktuální políčko
                self.addToNeighborsList(neighbors, row, col)
                piece.setNeighbors(neighbors)

    def addToNeighborsList(self, neighbors, row, col):
        # Projde všechny políčka v oblasti 3x3 kolem aktuálního políčka
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r == row and c == col:
                    # Přeskočí aktuální políčko
                    continue
                if r < 0 or r >= self.size[0] or c < 0 or c >= self.size[1]:
                    # Přeskí políčka mimo oblast
                    continue
                neighbors.append(self.board[r][c])

    def setNumAround(self):
        # Projde všechny políčka na poli
        for row in self.board:
            for piece in row:
                piece.setNumAround()