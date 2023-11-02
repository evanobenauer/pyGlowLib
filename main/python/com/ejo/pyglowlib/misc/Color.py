class Color:
    red = None
    green = None
    blue = None
    alpha = None

    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __str__(self):
        return "[" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ", " + str(self.alpha) + "]"

    def __eq__(self, color):
        return self.red == color.red and self.green == color.green and self.blue == color.blue and self.alpha == color.alpha


class ColorRGB(Color):

    def __init__(self, red, green, blue):
        super().__init__(red, green, blue, 255)
