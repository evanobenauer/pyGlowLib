class ColorRGBA:
    red = None
    green = None
    blue = None
    alpha = 255

    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __str__(self):
        return "[" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ", " + str(self.alpha) + "]"

    def __eq__(self, color):
        return self.red == color.red and self.green == color.green and self.blue == color.blue and self.alpha == color.alpha


class ColorRGB(ColorRGBA):

    def __init__(self, red, green, blue):
        ColorRGBA.__init__(self, red, green, blue, 255)
