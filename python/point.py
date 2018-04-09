class Point:
    def __init__( self, x0, y0):
        self.x = x0
        self.y = y0

    def move( self, dx, dy ):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def display(self):
        print(p.x, p.y)

    def screen(self):
        for i in range(1,10):
            for j in range(1,10):
                if p.x == j and p.y == i:
                    print('*', end='')
                else:
                    print('_', end='')

            print('\n', end='')


        
p = Point(1,2)
p.display()
p.screen()
p.move(3,1)
p.display()
p.screen()
