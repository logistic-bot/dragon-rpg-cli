class Room:
    def __init__(self, name, description="", items=None):
        if items is None:
            items = []

        self.name = name
        self.description = description
        self.items = items

    def _describe(self):
        return self.description

    def describe(self, fast=False):
        """Slowprints a description of the room, including all its items, to the user"""
        slowprint(self._describe(), fast=fast)

        for item in self.items:
            slowprint(item.description)
