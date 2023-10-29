class Container:
    value = None

    def __init__(self, value):
        self.value = value


class Setting(Container):
    def __init__(self, value):
        super().__init__(value)

    def save(self):
        pass

    def load(self):
        pass
