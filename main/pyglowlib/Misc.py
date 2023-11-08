class DoOnce:

    def __init__(self, action=None):
        self.shouldRun: bool = True
        self.action = action  # Lambda Statement

    def run(self):
        if self.shouldRun:
            self.action()
            self.shouldRun = False

    def setAction(self, action) -> 'DoOnce':
        self.action = action
        return self

    def reset(self) -> 'DoOnce':
        self.shouldRun = True
        return self
