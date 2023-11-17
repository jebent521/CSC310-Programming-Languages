class Vector:
    def __init__(self, items) -> None:
        self.items = list(items)
        if not all(isinstance(i, int) or isinstance(i, float) for i in self.items):
            raise ValueError('Vector items must be numerical')
    def __repr__(self) -> str:
        return f'Vector({self.items})'
    def __abs__(self):
        return
    def __len__(self):
        return len(self.items)

class Vector2d(Vector):
    def __init__(self, items):
        super().__init__()
        if len(self) != 2:
            raise ValueError('must have 2 components')
    def angleWithHorizontal(self):
        pass
    def getQuadrant(self):
        pass

class Vector3d(Vector):
    def __init__(self):
        super().__init__()
