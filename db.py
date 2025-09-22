from flask_sqlalchemy import SQLAlchemy
# Single, shared SQLAlchemy instance for the app
# - models import this:   from db import db
# - app initializes it:   db.init_app(app)  (done in app.py)
db = SQLAlchemy()