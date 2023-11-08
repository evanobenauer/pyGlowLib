class Color:

    def __init__(self, red: int, green: int, blue: int, alpha: int = 255):
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self.alpha: int = alpha

    def __str__(self) -> str:
        return f"[{self.red}, {self.green}, {self.blue}, {self.alpha}]"

    def __eq__(self, color: 'Color') -> bool:
        return self.red == color.red and self.green == color.green and self.blue == color.blue and self.alpha == color.alpha
