from models.engine.db_storage import DBStorage

class Storage:
    __engine = DBStorage()

    @staticmethod
    def all():
        return __engine.all()

    @staticmethod
    def new(obj):
        return __engine.new(obj)

    @staticmethod
    def save(obj):
        return __engine.save(obj)

    @staticmethod
    def delete(obj):
        return __engine.delete(obj)

