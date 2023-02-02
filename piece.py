class Piece:
    def __init__(self, hasBomb):
        #Inicializace objektu Piece
        self.hasBomb = hasBomb
        self.around = 0
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def __str__(self):
        # Vrátí hodnotu atributu 'hasBomb' jako string
        return str(self.hasBomb)

    def getNumAround(self):
        # Vrátí hodnotu atributu 'around'
        return self.around

    def getHasBomb(self):
        # Vrátí hodnotu atributu 'hasBomb'
        return self.hasBomb

    def getClicked(self):
        # Vrátí hodnotu atributu 'clicked'
        return self.clicked

    def getFlagged(self):
        # Vrátí hodnotu atributu 'flagged'
        return self.flagged

    def toggleFlag(self):
        # Invertuje hodnotu atributu 'flagged'
        self.flagged = not self.flagged

    def handleClick(self):
        # Nastaví hodnotu atributu 'clicked' na True
        self.clicked = True

    def setNumAround(self):
        # Nastaví hodnotu atributu 'around' na počet sousedů s bombou
        num = 0
        for neighbor in self.neighbors:
            if neighbor.getHasBomb():
                num += 1
        self.around = num

    def setNeighbors(self, neighbors):
        # Nastaví seznam sousedů (atribut 'neighbors') pro konkrétní políčko
        self.neighbors = neighbors

    def getNeighbors(self):
        # Vrátí seznam sousedů (atribut 'neighbors') pro konkrétní políčko
        return self.neighbors