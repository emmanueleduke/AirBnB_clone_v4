class DBStorage(Storage):

    def __init__(self, engine):
        super().__init__(engine)

    def all(self):
        return []

    def create(self, obj):
        pass

    def update(self, obj):
        pass

    def delete(self, obj):
        pass

