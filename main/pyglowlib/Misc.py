class DoOnce:
    shouldRun: bool

    action = None  # Lambda Statement

    def __init__(self, action=None):
        self.shouldRun = True
        self.action = action

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
