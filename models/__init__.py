#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from models.base import HBNB_ENV
import sys
from models.base import Base
sys.path.append("./models")

env = HBNB_ENV
if env == "test":
    print("The code is running in a test environment.")
else:
    print("The code is running in a production environment.")



storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
