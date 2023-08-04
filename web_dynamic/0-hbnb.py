from sqlalchemy import create_engine
import pymysql
from models import storage, DBStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
from models.sqlitestorage import SqliteStorage
import sys
sys.path.append("./models")
sys.path.append("./models/engine")
from models.engine.db_storage import Storage
def list_all():
    all_objects = Storage.all()
    for obj in all_objects:
        if isinstance(obj, BaseModel):
            print(obj)
        elif isinstance(obj, User):
            print(obj)
        elif isinstance(obj, Place):
            print(obj)
        elif isinstance(obj, Review):
            print(obj)


if __name__ == "__main__":
    list_all()


app = Flask(__name__)

engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(
    environ['HBNB_MYSQL_USER'],
    environ['HBNB_MYSQL_PWD'],
    environ['HBNB_MYSQL_HOST'],
    environ['HBNB_MYSQL_DB']))

storage = SqliteStorage(engine)
storage.init_app(app)



@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
			   cache_id=uuid.uuid4())

def __main__():
    print("This is the main function of the 0-hbnb module.")

if __name__ == "__main__":
    __main__()
    __name__ = "0-hbnb"

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

