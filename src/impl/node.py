class Node:
    WHITE = 1
    BLACK = 2
    GRAY = 3

    def __init__(self, key: int, pos=None):
        self.key = key
        self.pos = pos
        self.edges_in = {}
        self.edges_out = {}
        self.w = 0
        self.tag = Node.WHITE

    def __str__(self):
        return f'key: {self.key} , w {self.w} ,pos : {self.pos}'

    def __repr__(self):
        return f'key: {self.key}, w {self.w} , pos : {self.pos}'

    def __dict__(self):
        return {
            'pos': f'{self.pos[0]},{self.pos[1]},{self.pos[2]}',
            'id': self.key
        }
