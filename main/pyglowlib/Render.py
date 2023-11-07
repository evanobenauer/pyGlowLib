class Color:
    red: int
    green: int
    blue: int
    alpha: int

    def __init__(self, red: int, green: int, blue: int, alpha: int = 255):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __str__(self) -> str:
        return "[" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ", " + str(self.alpha) + "]"

    def __eq__(self, color: 'Color') -> bool:
        return self.red == color.red and self.green == color.green and self.blue == color.blue and self.alpha == color.alpha