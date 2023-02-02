from game import Game
# importy

def main():
    # Velikost pole
    size = (10, 10)
    # Pravděpodobnost min
    prob = (0.2)
    # Vytvoření nové hry s danými parametry
    g = Game(size, prob)
    # Spustí hru
    g.run()

if __name__ == '__main__':
    main()