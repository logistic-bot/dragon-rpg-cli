class Room:
    def __init__(self, name, description="", items=None):
        if items is None:
            items = []

        self.name = name
        self.description = description
        self.items = items

    def _describe(self):
        return self.description

    def describe(self):
        print(self._describe())
