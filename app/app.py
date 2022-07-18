from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__, static_folder='static')
app.config.from_object(Configuration)

db = SQLAlchemy(app)


migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)



