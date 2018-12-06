cmds = []

class Command(object):
    def __init__(self):
        self._keys = []
        self.description = ""
        cmds.append(self)

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, news):
        self._keys.extend(map(lambda x: x.lower(), news))

    def process(self):
        pass