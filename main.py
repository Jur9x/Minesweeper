from game import Game

def main():
    size = (5, 5)
    prob = (0.2)
    g = Game(size, prob)
    g.run()

if __name__ == '__main__':
    main()