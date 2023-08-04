HBNB_ENV = "test"
class Base(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"[Base] {self.id} {self.name}"

