#!/usr/bin/python3

# Instantiates a storage object.

from os import getenv


# If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # Otherwise, instantiates a file storage engine (FileStorage).
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
