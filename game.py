import pygame
from board import Board
import os
from solver import Solver
from time import sleep
# importy

class Game:
    def __init__(self, size, prob):
        # Inicializace herní desky
        self.board = Board(size, prob)
        # Inicializace knihovny pygame
        pygame.init()
        # Nastavení velikosti obrazovky
        self.sizeScreen = 800, 800
        self.screen = pygame.display.set_mode(self.sizeScreen)
        # Velikost jednotlivých políček
        self.pieceSize = (self.sizeScreen[0] / size[1], self.sizeScreen[1] / size[0])
        # Načtení obrázků
        self.loadPictures()
        # Inicializace hráče hry
        self.solver = Solver(self.board)

    def loadPictures(self):
        # Inicializace slovníku obrázků
        self.images = {}
        # Adresář s obrázky
        imagesDirectory = "images"
        # Procházení souborů v adresáři
        for fileName in os.listdir(imagesDirectory):
            if not fileName.endswith(".png"):
                continue
            # Cesta k obrázku
            path = imagesDirectory + r"/" + fileName
            # Načtení obrázku
            img = pygame.image.load(path)
            # Převod obrázku do formátu pro zobrazování
            img = img.convert()
            # Změna velikosti obrázku
            img = pygame.transform.scale(img, (int(self.pieceSize[0]), int(self.pieceSize[1])))
            # Uložení obrázku do listu
            self.images[fileName.split(".")[0]] = img

    def run(self):
        # Proměnná určující, zda se hra stále hraje
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not (self.board.getWon() or self.board.getLost()):
                    # Zjištění, zda bylo kliknuto pravým tlačítkem myši
                    rightClick = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handleClick(pygame.mouse.get_pos(), rightClick)
                if event.type == pygame.KEYDOWN:
                    self.solver.move()
            # Vyplnění obrazovky barvou
            self.screen.fill((0, 0, 0))
            # Vykreslení hrací plochy
            self.draw()
            # Aktualizace obrazovky
            pygame.display.flip()
            # Pokud je hra vyhrána, spustí se funkce win() a cyklus se ukončí
            if self.board.getWon():
                self.win()
                running = False
        # Ukončení pygame knihovny
        pygame.quit()

    # Funkce pro vykreslení hrací plochy
    def draw(self):
        # Počáteční souřadnice
        topLeft = (0, 0)
        # Procházení jednotlivých řádků hrací plochy
        for row in self.board.getBoard():
            # Procházení jednotlivých políček
            for piece in row:
                # Vytvoření obdélníku pro dané políčko
                rect = pygame.Rect(topLeft, self.pieceSize)
                # Načtení obrázku pro dané políčko
                image = self.images[self.getImageString(piece)]
                # Vykreslení obrázek na určené souřadnice
                self.screen.blit(image, topLeft)
                # Posun na další pozici
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            # Posun na další řádek
            topLeft = (0, topLeft[1] + self.pieceSize[1])

    # Funkce pro určení názvu obrázku
    def getImageString(self, piece):
        # Pokud je políčko označeno, vrátí se počet min kolem něj
        if piece.getClicked():
            return str(piece.getNumAround()) if not piece.getHasBomb() else 'bomb-at-clicked-block'
        # Pokud hra skončila prohrou, zobrazí se odhalené bomby
        if (self.board.getLost()):
            if (piece.getHasBomb()):
                return 'unclicked-bomb'
            return 'wrong-flag' if piece.getFlagged() else 'empty-block'
        # Jinak se zobrazí vlajka, pokud je políčko označeno
        return 'flag' if piece.getFlagged() else 'empty-block'

    # Funkce pro kontrolu kliknutí na hrací plochu
    def handleClick(self, position, flag):
        # Určení indexu políčka na základě souřadnic
        index = tuple(int(pos // size) for pos, size in zip(position, self.pieceSize))[::-1]
        # Zpracování kliknutí
        self.board.handleClick(self.board.getPiece(index), flag)
    def win(self):
        #Počká 3 sekundy
        sleep(3)