class Container:
    value = None

    def __init__(self, value):
        self.value = value

    def __eq__(self, other: 'Container') -> bool:
        return self.value == other.value


class Setting(Container):
    settingManager: 'SettingManager'

    def __init__(self, value, manager: 'SettingManager' = None):
        super().__init__(value)
        self.settingManager = manager

    # TODO: Add
    def save(self):
        pass

    def load(self):
        pass


class SettingManager:
    def loadAll(self):
        pass

    def saveAll(self):
        pass
