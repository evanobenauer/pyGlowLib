class Container:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other: 'Container') -> bool:
        return self.value == other.value


class Setting(Container):

    def __init__(self, value, manager: 'SettingManager' = None):
        super().__init__(value)
        self.settingManager: 'SettingManager' = manager

    def save(self):
        self.settingManager.saveAll()

    def load(self):
        self.settingManager.loadAll()


class SettingManager:
    def loadAll(self):
        pass

    def saveAll(self):
        pass
